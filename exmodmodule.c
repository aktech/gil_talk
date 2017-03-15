#include "Python.h"

// static PyObject *exmodError;

static PyObject* exmod_say_hello(PyObject* self, PyObject *args) {
	const char* msg;
	int sts = 0;

	if (!PyArg_ParseTuple(args, "s", &msg)) {
		return NULL;
	}

	else {
		printf("%s\n", msg);
		sts = 21;
	}
	return Py_BuildValue("i", sts);
}

static PyMethodDef exmod_methods[] = {
	// PythonName C-Func Name      Argument presentation  Description  
	{"say_hello", exmod_say_hello, METH_VARARGS,          "Say Hello"},
	{NULL, NULL, 0, NULL} 
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
