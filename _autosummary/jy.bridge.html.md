# jy.bridge

Python portals to JS

### Functions

| [`add_js_funcs`](#jy.bridge.add_js_funcs)(js_code, \*[, obj, name, ...])   | Add js call functions as attributes to an object.   |
|------------------------------------------------------------------------------------------------|-----------------------------------------------------|
| `mk_py_binder_func`(name, params, \*[, prefix, ...])                                           |                                                     |

### Classes

| [`JsBridge`](#jy.bridge.JsBridge)()   | The default class to make instances that will contain methods that mirror JS function calls   |
|---------------------------------------------------------------|-----------------------------------------------------------------------------------------------|

### *class* jy.bridge.JsBridge

Bases: [`object`](https://docs.python.org/3/builtins/functions.html#object)

The default class to make instances that will contain methods that mirror JS
function calls

### jy.bridge.add_js_funcs(js_code, \*, obj=None, name=None, encoding=None, forbidden_method_names=(), apply_defaults=True, value_trans=<function dflt_py_to_js_value_trans>)

Add js call functions as attributes to an object.

If object is not given, `add_js_funcs` will use a new `JsBridge` instance.

```pycon
>>> js_code = """
... function foo(a, b="hello", c= 3) {
...     return a + b.length * c
... }
... const bar = (y, z = 1) => y * z
... func.assigned.to.nested.prop = function (x) {
...     return x + 3
... }
... """
>>> js = add_js_funcs(js_code)
>>> from inspect import signature
>>> list(vars(js))
['foo', 'bar', 'prop']
>>> signature(js.foo)
<Sig (a, b='hello', c=3)>
>>> js.foo(1, 'hi')
'foo(1, "hi", 3)'
>>> js.prop('up')
'func.assigned.to.nested.prop("up")'
```

### jy.bridge.iskeyword()

x._\_contains_\_(y) <==> y in x.
