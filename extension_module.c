#include <Python.h>

static PyObject* count(PyObject* self, PyObject* args)
{
    long long int value, i;

    /*  parse the input, from python integer to c long long int */
    if (!PyArg_ParseTuple(args, "L", &value))
        return NULL;
    /* if the above function returns -1, an appropriate Python exception will
     * have been set, and the function simply returns NULL
     */

    Py_BEGIN_ALLOW_THREADS
    for (i = 0; i < value; ++i) {
        // Simply Count
    }
    Py_END_ALLOW_THREADS

    return Py_BuildValue("i", 1);
}

/*  define functions in module */
static PyMethodDef myModule[] =
{
     {"count", count, METH_VARARGS, "Count Loop"}
};

/* module initialization */
PyMODINIT_FUNC initextension_module(void)
{
     (void) Py_InitModule("extension_module", myModule);
}
