# jy.ts_parse

Tools to parse TS code

### Functions

| [`default_handler`](#jy.ts_parse.default_handler)(code, node)                       | Default handler for nodes that don't have a specific handler.                          |
|----------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [`extract_parameters`](#jy.ts_parse.extract_parameters)(code, parameters_node)         | Generator function that yields parameter dictionaries.                                 |
| [`find_function_type_node`](#jy.ts_parse.find_function_type_node)(node)                     | Recursively search for a 'function_type' node within a given node.                     |
| [`handle_interface_declaration`](#jy.ts_parse.handle_interface_declaration)(code, node)          | Handle 'interface_declaration' nodes by traversing their members.                      |
| [`handle_method_signature`](#jy.ts_parse.handle_method_signature)(code, node)               | Handle 'method_signature' nodes, yielding (method name, method info) tuples.           |
| [`handle_property_signature`](#jy.ts_parse.handle_property_signature)(code, node)             | Handle 'property_signature' nodes, yielding (property name, property info) tuples.     |
| [`parse_ts`](#jy.ts_parse.parse_ts)(code[, node])                            | Generator function that traverses the syntax tree and yields (name, info dict) tuples. |
| [`parse_ts_with_oa`](#jy.ts_parse.parse_ts_with_oa)(ts_code, \*[, schema_name, ...]) | Parse TypeScript code using the OpenAI API.                                            |
| `test_parse_ts`()                                                                                  |                                                                                        |

### jy.ts_parse.default_handler(code, node)

Default handler for nodes that don’t have a specific handler.

* **Return type:**
  [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]]]

### jy.ts_parse.extract_parameters(code, parameters_node)

Generator function that yields parameter dictionaries.

* **Return type:**
  [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]]

### jy.ts_parse.find_function_type_node(node)

Recursively search for a ‘function_type’ node within a given node.

* **Return type:**
  [`Any`](https://docs.python.org/3/library/typing.html#typing.Any) | [`None`](https://docs.python.org/3/builtins/constants.html#None)

### jy.ts_parse.handle_interface_declaration(code, node)

Handle ‘interface_declaration’ nodes by traversing their members.

* **Return type:**
  [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]]]

### jy.ts_parse.handle_method_signature(code, node)

Handle ‘method_signature’ nodes, yielding (method name, method info) tuples.

* **Return type:**
  [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]]]

### jy.ts_parse.handle_property_signature(code, node)

Handle ‘property_signature’ nodes, yielding (property name, property info) tuples.

* **Return type:**
  [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]]]

### jy.ts_parse.parse_ts(code, node=None)

Generator function that traverses the syntax tree and yields (name, info dict) tuples.

If ‘node’ is None, it parses the code and starts traversal from the root node.

### Example

```pycon
>>> code = '''
... interface Example {
...     prop1: string;
...     func1(a: number): void;
... }
... '''
>>> items = list(parse_ts(code))
>>> for name, info in items:
...     print(f"Name: {name}, Kind: {info['kind']}")
Name: prop1, Kind: property
Name: func1, Kind: function
```

* **Return type:**
  [`Iterator`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator)[[`tuple`](https://docs.python.org/3/builtins/stdtypes.html#tuple)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`dict`](https://docs.python.org/3/builtins/stdtypes.html#dict)[[`str`](https://docs.python.org/3/builtins/stdtypes.html#str), [`Any`](https://docs.python.org/3/library/typing.html#typing.Any)]]]

### jy.ts_parse.parse_ts_with_oa(ts_code, , schema_name='parsed_ts', strict=False, model='gpt-4o', extra_context='')

Parse TypeScript code using the OpenAI API.
