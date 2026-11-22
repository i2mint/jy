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
