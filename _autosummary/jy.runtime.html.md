# jy.runtime

Runtimes that execute the call strings jy builds, and return their values.

A runtime is any callable `(call_text: str) -> value`. [`NodeRuntime`](#jy.runtime.NodeRuntime)
runs the call in a fresh `node` process loaded with the JS source, and decodes
the JSON-serialized result (`Promise` results are awaited).

```pycon
>>> from jy import add_js_funcs
>>> from jy.runtime import NodeRuntime
>>> code = "function shout(s, n=1) { return s.toUpperCase() + '!'.repeat(n) }"
>>> js = add_js_funcs(code, runtime=NodeRuntime(code))
>>> js.shout('say "hi"', 2)
'SAY "HI"!!'
```

### Module Attributes

| [`RESULT_MARKER`](#jy.runtime.RESULT_MARKER)   | Line prefix marking the JSON result among whatever else the JS prints.   |
|------------------------------------------------------------------|--------------------------------------------------------------------------|

### Classes

| [`NodeRuntime`](#jy.runtime.NodeRuntime)([js_code, prelude, node, timeout])   | Execute jy call strings in `node` (one process per call, stateless).   |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------|

### Exceptions

| [`JsRuntimeError`](#jy.runtime.JsRuntimeError)   | The JS call failed (non-zero exit); the message carries stderr.   |
|-------------------------------------------------------------------|-------------------------------------------------------------------|

### *exception* jy.runtime.JsRuntimeError

Bases: [`RuntimeError`](https://docs.python.org/3/builtins/exceptions.html#RuntimeError)

The JS call failed (non-zero exit); the message carries stderr.

### *class* jy.runtime.NodeRuntime(js_code='', , prelude='', node='node', timeout=60)

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

Execute jy call strings in `node` (one process per call, stateless).

`js_code` is evaluated before each call (`prelude` is extra code run
first, e.g. a `require`). `node` is the executable (or an argv prefix),
`timeout` bounds one call in seconds.

#### script(call_text)

The full program run for one call.

* **Return type:**
  [`str`](https://docs.python.org/3/builtins/stdtypes.html#str)

### jy.runtime.RESULT_MARKER *= '\\x00jy-result\\x00'*

Line prefix marking the JSON result among whatever else the JS prints.
