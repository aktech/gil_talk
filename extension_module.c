#include <Python.h>
#include <stdio.h>
#include <math.h>

static PyObject* count(PyObject* self, PyObject* args)
{
    long long int value, i, j;
    double k = 0.0;

    /*  parse the input, from python integer to c long long int */
    if (!PyArg_ParseTuple(args, "L", &value))
        return NULL;
    /* if the above function returns -1, an appropriate Python exception will
     * have been set, and the function simply returns NULL
     */

    Py_BEGIN_ALLOW_THREADS
    long long int neg_value = -value;
    while (value > neg_value) {
        // Simply Count
        value -= 1;
    }
    Py_END_ALLOW_THREADS
    printf("%llu\n", value);

    return Py_BuildValue("L", k);
}

/*  define functions in module */
static PyMethodDef myModule[] =
{
     {"count", count, METH_VARARGS, "Count Loop"}
};

///* module initialization */
//PyMODINIT_FUNC
//initextension_module(void)
//{
//     (void) Py_InitModule("extension_module", myModule);
//}

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
