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
$ make
```

The function defined in extensions module is used in `c_ext_gil_test.py`, run it
as following:

```bash
$ python c_ext_gil_test.py

Single Thread: 2.421997
Two Threads:   1.191459
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

