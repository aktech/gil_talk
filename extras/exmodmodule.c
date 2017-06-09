#include "Python.h"

// static PyObject *exmodError;

static PyObject* exmod_count(PyObject* self, PyObject *args) {
	long long int work;

	if (!PyArg_ParseTuple(args, "L", &work)) {
		return NULL;
	}

	Py_BEGIN_ALLOW_THREADS
	printf("%lld\n", work);
	long long int i = 0;
	while (work--) {
		i++;
	}
	printf("%lld\n", i);
    Py_END_ALLOW_THREADS
	return Py_BuildValue("i", 1);
}

static PyMethodDef exmod_methods[] = {
	// PythonName C-Func Name      Argument presentation  Description  
	{"count", exmod_count, METH_VARARGS,          "Count"}
};

static struct PyModuleDef exmodmodule = {
   PyModuleDef_HEAD_INIT,
   "exmod",   /* name of module */
   "doc", /* module documentation, may be NULL */
   -1,       /* size of per-interpreter state of the module,
                or -1 if the module keeps state in global variables. */
   exmod_methods
};

PyMODINIT_FUNC
PyInit_exmod(void)
{
    return PyModule_Create(&exmodmodule);
}
