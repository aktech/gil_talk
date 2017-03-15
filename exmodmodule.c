#include "Python.h"

static PyObject *exmodError;

static PyObject* exmod_say_hello(PyObject* self, PyObject *args) {
	const char* msg;
	int sts = 0;

	if (!PyArg_ParseTuple(args, 's', &msg)) {
		return NULL;
	}

	else {
		printf("This is message from C %s\n", msg);
		sts = 21;
	}
	return Py_BuildValue("i", sts);
}

static PyMethodDef exmod_methods[] = {
	// PythonName C-Func Name      Argument presentation  Description  
	{"say_hello", exmod_say_hello, METH_VARARGS,          "Say Hello"},
	{NULL, NULL, 0, NULL} 
};

PyMODINIT_FUNC initexmod(void) {
	PyObject *m;
	m = Py_InitModule("exmod", exmod_methods);

	if (m != NULL) {
		exmodError = PyErr_NewException("exmod.error", NULL, NULL);
		Py_INCREF(exmodError);

		PyModule_AddObject(m, "error", "ExModError");
	}
}