# jy.js_parse

Utils to parse JS

### Functions

| [`append_to_func_body`](#jy.js_parse.append_to_func_body)(func_def_code, ...)          | Append code to the body of a function definition                             |
|---------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| `dflt_py_to_js_value_trans`(x)                                                                    |                                                                              |
| [`extract_func_name_and_params`](#jy.js_parse.extract_func_name_and_params)(ast_node)           | Extract one or several function `(name, params)` pair(s) from an AST node    |
| [`extract_function_def_parts`](#jy.js_parse.extract_function_def_parts)(func_def_code)        | Extract the body of a function definition from its code                      |
| `extract_js_func_params`(params_list)                                                             |                                                                              |
| [`func_name_and_params_pairs`](#jy.js_parse.func_name_and_params_pairs)(js_code, \*[, ...])   | Get `(name, params)` pairs of function definitions extracted from `js_code`. |
| `if_none_output_raise_unknown_type`([context])                                                    |                                                                              |
| [`parse_js`](#jy.js_parse.parse_js)(js_code[, encoding, ingress, egress])   | Parse JavaScript source (or a path to a `.js` file) into an esprima AST.     |
| [`parse_js_code`](#jy.js_parse.parse_js_code)(js_code[, encoding, ingress, ...]) | Parse JavaScript source (or a path to a `.js` file) into an esprima AST.     |
| [`replace_ids_in_code`](#jy.js_parse.replace_ids_in_code)(code[, patterns])            | Replaces IDs in a mixed HTML, CSS, and JS string with unique versions.       |
| [`variable_declarations_pairs`](#jy.js_parse.variable_declarations_pairs)(src, \*[, encoding]) | Yield `(name, value)` pairs for the top-level variable declarations in JS.   |

### Exceptions

| [`UnknownNodeType`](#jy.js_parse.UnknownNodeType)(node_type[, context])   | To be raised when an AST node type wasn't handled by a function   |
|------------------------------------------------------------------------------------------|-------------------------------------------------------------------|

### *exception* jy.js_parse.UnknownNodeType(node_type, context='')

Bases: [`ValueError`](https://docs.python.org/3/builtins/exceptions.html#ValueError)

To be raised when an AST node type wasn’t handled by a function

### jy.js_parse.append_to_func_body(func_def_code, code_to_append)

Append code to the body of a function definition

* **Return type:**
  [`str`](https://docs.python.org/3/builtins/stdtypes.html#str)

### jy.js_parse.extract_func_name_and_params(ast_node)

Extract one or several function `(name, params)` pair(s) from an AST node

### jy.js_parse.extract_function_def_parts(func_def_code)

Extract the body of a function definition from its code

* **Return type:**
  [`str`](https://docs.python.org/3/builtins/stdtypes.html#str)

### jy.js_parse.func_name_and_params_pairs(js_code, , encoding=None)

Get `(name, params)` pairs of function definitions extracted from `js_code`.

```pycon
>>> js_code = '''
... function foo(a, b="hello", c= 3) {
...     return a + b.length * c
... }
... const bar = (y, z = 1) => y * z
... func.assigned.to.nested.prop = function (x) {
...     return x + 3
... }'''
>>> assert list(func_name_and_params_pairs(js_code)) == [
...     ('foo', [
...         {'name': 'a'},
...         {'name': 'b', 'default': 'hello'},
...         {'name': 'c', 'default': 3}
...     ]),
...     ('bar', [
...         {'name': 'y'},
...         {'name': 'z', 'default': 1}
...     ]),
...     ('func.assigned.to.nested.prop', [
...         {'name': 'x'}
...     ])
... ]
```

### jy.js_parse.parse_js(js_code, encoding=None, \*, ingress=<function <lambda>>, egress=<function <lambda>>)

Parse JavaScript source (or a path to a `.js` file) into an esprima AST.

`js_code` may be a string of JS or a filesystem path, in which case the
file is read (honoring `encoding`). `ingress` preprocesses the source
before parsing; `egress` post-processes the resulting AST.

```pycon
>>> tree = parse_js("const x = 42;")
>>> tree.body[0].type
'VariableDeclaration'
>>> tree.body[0].declarations[0].id.name
'x'
```

* **Return type:**
  `Script`

### jy.js_parse.parse_js_code(js_code, encoding=None, \*, ingress=<function <lambda>>, egress=<function <lambda>>)

Parse JavaScript source (or a path to a `.js` file) into an esprima AST.

`js_code` may be a string of JS or a filesystem path, in which case the
file is read (honoring `encoding`). `ingress` preprocesses the source
before parsing; `egress` post-processes the resulting AST.

```pycon
>>> tree = parse_js("const x = 42;")
>>> tree.body[0].type
'VariableDeclaration'
>>> tree.body[0].declarations[0].id.name
'x'
```

* **Return type:**
  `Script`

### jy.js_parse.replace_ids_in_code(code, patterns=('id="([^"]+)"', '#([a-zA-Z][\\\\w\\\\-]\*)', 'document\\\\.getElementById\\\\("([^"]+)"\\\\)'))

Replaces IDs in a mixed HTML, CSS, and JS string with unique versions.

### Args

- code (str): The input code containing HTML, CSS, and/or JS.
- patterns (tuple): A tuple of regex patterns to match IDs.

### Returns

- tuple: A tuple containing the modified code and a dictionary of old-to-new ID mappings.

This function is useful to make id-unique copies of HTML/JS components that have IDs.
This need was noticed and discussed in: [https://github.com/i2mint/jy/discussions/3#discussioncomment-6862843](https://github.com/i2mint/jy/discussions/3#discussioncomment-6862843)

* **Return type:**
  [`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)]

### jy.js_parse.variable_declarations_pairs(src, , encoding=None)

Yield `(name, value)` pairs for the top-level variable declarations in JS.

Literal, object, array and unary-minus initializers are evaluated to their
Python equivalents; other initializer kinds yield `None`. A leading
`export` on a declaration is stripped first, so ES-module sources parse.

```pycon
>>> list(variable_declarations_pairs("const a = 3; let b = 'hi';"))
[('a', 3), ('b', 'hi')]
>>> list(variable_declarations_pairs("export const config = {x: 1, y: [2, 3]};"))
[('config', {'x': 1, 'y': [2, 3]})]
>>> list(variable_declarations_pairs("var n = -5; const flag = true;"))
[('n', -5), ('flag', True)]
```
