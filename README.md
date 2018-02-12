# GIL Talk

A talk on Global Interpreter lock.

## Contents

### Functions threads API

```bash
$ python function_threads.py
```

### Class based threads API

```bash
$ python class_threads.py
```

### Extension Module

Python C extension module is written in `extension_module.c` to build it on mac, run:

```bash
$ python setup.py build
```

The above will will compile `extension_module.c`, and produce an extension module
in the build directory. Depending on the system, the module file will end up in
a subdirectory `build/lib.system.extension_module.so`.

Copy the built `*.so` file in the current directory, for e.g.:

```bash
$ cp build/lib.macosx-10.7-x86_64-3.6/extension_module.cpython-36m-darwin.so .
```

The function defined in extensions module is used in `c_ext_gil_test.py`, run it
as following:

```bash
$ python c_ext_gil_test.py
Single Thread: 2.118302
Two Threads:   1.348021
```

### Compile and run C Threads

* compile

```bash
$ g++ c_threads.cpp -o c_threads
```

* run

```bash
$ ./c_threads
```

### Acknowledgement

Thanks to [Garvit](https://garvit.in/) and [Suhaib](https://suheb.in/), who played a vital role in the
preparation of this presentation.
