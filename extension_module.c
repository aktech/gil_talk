#include <Python.h>


static PyObject* count(PyObject* self, PyObject* args)
{
    volatile unsigned long long int value;
    /*  parse the input, from python integer to c long long int */
    if (!PyArg_ParseTuple(args, "L", &value))
        return NULL;
    /* if the above function returns -1, an appropriate Python exception will
     * have been set, and the function simply returns NULL
     */

    Py_BEGIN_ALLOW_THREADS
    while (value > 0) {
        // Simply Count
        value -= 1;
    }
    Py_END_ALLOW_THREADS

    return Py_BuildValue("i", 1);
}

/*  define functions in module */
static PyMethodDef myModule[] =
{
     {"count", count, METH_VARARGS, "Count Loop"}
};

static struct PyModuleDef extension_module = {
    PyModuleDef_HEAD_INIT,
    "extension_module",
    NULL,
    -1,
    myModule
};

PyMODINIT_FUNC
PyInit_extension_module(void)
{
    return PyModule_Create(&extension_module);
}
