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

Python C extension module is written in `src/python_c_extension/extension_module.c`.
To build and install it into the current environment, run from the repo root:

```bash
$ pip install .
```

The function defined in extensions module is used in `c_extension_gil.py`, run it
as following:

```bash
$ python -m python_c_extension.c_extension_gil
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
