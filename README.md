# GIL Talk

[![GIL Talk Demo](https://github.com/aktech/gil_talk/actions/workflows/test.yml/badge.svg)](https://github.com/aktech/gil_talk/actions/workflows/test.yml)

A talk on Global Interpreter lock.

## Contents

### Functions threads API

```bash
$ python python_multithreading/function_threads.py
```

### Class based threads API

```bash
$ python python_multithreading/class_threads.py
```

### Extension Module

Python C extension module is written in `extension_module.c` to build it on mac, run:

```bash
$ python python_c_extension/setup.py build
```

The above will will compile `extension_module.c`, and produce an extension module
in the build directory. Depending on the system, the module file will end up in
a subdirectory `build/lib.system.extension_module.so`.

Copy the built `*.so` file in the current directory, for e.g.:

```bash
$ cp -r build/*/* python_c_extension
```

The function defined in extensions module is used in `c_ext_gil_test.py`, run it
as following:

```bash
$ python python_c_extension/c_extension_gil.py
Single Thread: 2.118302
Two Threads:   1.348021
```

### Compile and run C Threads

* compile

```bash
$ g++ cpp_multithreading/c_threads.cpp -o cpp_multithreading/c_threads
```

* run

```bash
$ ./cpp_multithreading/c_threads
```

### Acknowledgement

Thanks to [Garvit](https://garvit.in/) and [Suhaib](https://suheb.in/), who played a vital role in the
preparation of this presentation.
