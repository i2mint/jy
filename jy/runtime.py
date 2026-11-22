"""Runtimes that execute the call strings jy builds, and return their values.

A runtime is any callable ``(call_text: str) -> value``. :class:`NodeRuntime`
runs the call in a fresh ``node`` process loaded with the JS source, and decodes
the JSON-serialized result (``Promise`` results are awaited).

>>> from jy import add_js_funcs
>>> from jy.runtime import NodeRuntime
>>> code = "function shout(s, n=1) { return s.toUpperCase() + '!'.repeat(n) }"
>>> js = add_js_funcs(code, runtime=NodeRuntime(code))  # doctest: +SKIP
>>> js.shout('say "hi"', 2)  # doctest: +SKIP
'SAY "HI"!!'
"""

from __future__ import annotations

import json
import shutil
import subprocess
from collections.abc import Sequence

#: Line prefix marking the JSON result among whatever else the JS prints.
RESULT_MARKER = "\x00jy-result\x00"


class JsRuntimeError(RuntimeError):
    """The JS call failed (non-zero exit); the message carries stderr."""


class NodeRuntime:
    """Execute jy call strings in ``node`` (one process per call, stateless).

    ``js_code`` is evaluated before each call (``prelude`` is extra code run
    first, e.g. a ``require``). ``node`` is the executable (or an argv prefix),
    ``timeout`` bounds one call in seconds.
    """

    def __init__(
        self,
        js_code: str = "",
        *,
        prelude: str = "",
        node: str | Sequence[str] = "node",
        timeout: float | None = 60,
    ):
        self.js_code = js_code
        self.prelude = prelude
        self.node = [node] if isinstance(node, str) else list(node)
        self.timeout = timeout

    def script(self, call_text: str) -> str:
        """The full program run for one call."""
        return (
            f"{self.prelude}\n{self.js_code}\n"
            f"Promise.resolve().then(() => {call_text}).then((r) => {{\n"
            f"  process.stdout.write('\\n{RESULT_MARKER}' + "
            f"JSON.stringify(r === undefined ? null : r) + '\\n');\n"
            f"}}).catch((e) => {{ console.error(e && e.stack || String(e)); "
            f"process.exit(1); }});\n"
        )

    def __call__(self, call_text: str):
        if not shutil.which(self.node[0]):
            raise JsRuntimeError(
                f"{self.node[0]!r} is not on PATH; install Node.js (https://nodejs.org)."
            )
        proc = subprocess.run(
            [*self.node, "-"],
            input=self.script(call_text),
            capture_output=True,
            text=True,
            timeout=self.timeout,
        )
        if proc.returncode != 0:
            raise JsRuntimeError(f"node failed: {proc.stderr.strip()}")
        for line in reversed(proc.stdout.splitlines()):
            if line.startswith(RESULT_MARKER):
                return json.loads(line[len(RESULT_MARKER) :])
        raise JsRuntimeError("the JS call produced no result")
