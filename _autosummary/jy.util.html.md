# jy.util

General utils

### Functions

| [`js_files_as_attrs`](#jy.util.js_files_as_attrs)(rootdir)   | Will make a JsFiles, but where the keys are available as attributes.   |
|-------------------------------------------------------------------------------|------------------------------------------------------------------------|

### Classes

| [`JsFiles`](#jy.util.JsFiles)(\*args[, delete_func, ...])   | A store of js files   |
|----------------------------------------------------------------------------------------|-----------------------|
| [`mk_js_files`](#jy.util.mk_js_files)                           |                       |

### *class* jy.util.JsFiles(\*args, delete_func=None, write_open_kwargs=None, write_func=None, \*\*kwargs)

Bases: `Store`

A store of js files

#### is_valid_key(k, \*args, \_\_name='is_valid_key', \*\*kwargs)

`is_valid_key` on the inner key – see `mk_relative_path_store`.

#### validate_key(k, \*args, \_\_name='validate_key', \*\*kwargs)

`validate_key` on the inner key – see `mk_relative_path_store`.

### jy.util.js_files_as_attrs(rootdir)

Will make a JsFiles, but where the keys are available as attributes.
To do so, any non alphanumerics of file name are replaced with underscore,
and there can be no two files that collide with that key transformation!

### jy.util.mk_js_files

alias of [`JsFiles`](#jy.util.JsFiles)
