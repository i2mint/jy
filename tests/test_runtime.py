import shutil

import pytest

from jy import add_js_funcs
from jy.js_parse import dflt_py_to_js_value_trans as trans
from jy.runtime import JsRuntimeError, NodeRuntime

CODE = """
function echo(x) { console.log('noise'); return x }
function shout(s, n=1) { return s.toUpperCase() + '!'.repeat(n) }
async function later(x) { return {x} }
function boom() { throw new Error('bad') }
"""


def test_value_trans_is_json():
    assert trans('a"b\\') == '"a\\"b\\\\"'
    assert trans([{"a": 1}, None, True]) == '[{"a": 1}, null, true]'


def test_call_text_without_runtime_unchanged():
    assert add_js_funcs(CODE).shout("hi", 2) == 'shout("hi", 2)'


@pytest.mark.skipif(not shutil.which("node"), reason="node not installed")
def test_node_runtime_round_trips():
    js = add_js_funcs(CODE, runtime=NodeRuntime(CODE))
    data = [{"a": 1, "b": [1, 2]}, {"q": 'he said "hi"\nok'}]
    assert js.echo(data) == data
    assert js.shout('say "hi"', 2) == 'SAY "HI"!!'
    assert js.later(3) == {"x": 3}
    with pytest.raises(JsRuntimeError, match="bad"):
        js.boom()


def _chromium_available():
    try:
        from playwright.sync_api import sync_playwright

        with sync_playwright() as p:
            p.chromium.launch().close()
        return True
    except Exception:
        return False


@pytest.mark.skipif(
    not _chromium_available(), reason="playwright chromium not installed"
)
def test_playwright_runtime_round_trips():
    from jy.runtime import PlaywrightRuntime

    js = add_js_funcs(CODE, runtime=PlaywrightRuntime(CODE))
    data = [{"a": 1, "b": [1, 2]}, {"q": 'he said "hi"\nok'}]
    assert js.echo(data) == data
    assert js.shout('say "hi"', 2) == 'SAY "HI"!!'
    assert js.later(3) == {"x": 3}
    with pytest.raises(JsRuntimeError, match="bad"):
        js.boom()


def test_playwright_runtime_without_playwright_names_the_extra(monkeypatch):
    import builtins

    from jy.runtime import PlaywrightRuntime

    real_import = builtins.__import__

    def no_playwright(name, *a, **k):
        if name.startswith("playwright"):
            raise ImportError(name)
        return real_import(name, *a, **k)

    monkeypatch.setattr(builtins, "__import__", no_playwright)
    with pytest.raises(JsRuntimeError, match="browser"):
        PlaywrightRuntime("")("1")


@pytest.mark.skipif(not shutil.which("node"), reason="node not installed")
@pytest.mark.parametrize("sep", [" ", " ", "\x85", "\x0b", "\x1c"])
def test_node_runtime_returns_strings_with_unicode_line_separators(sep):
    """JSON.stringify leaves these unescaped; the result line must not be split on them."""
    js = add_js_funcs(CODE, runtime=NodeRuntime(CODE))
    assert js.echo(f"a{sep}b") == f"a{sep}b"
    assert js.echo({"k": f"é{sep}"}) == {"k": f"é{sep}"}
