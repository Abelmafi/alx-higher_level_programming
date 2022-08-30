#include <Python.h>
#include <object.h>
#include <listobject.h>
#include <stdio.h>
void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", PyList_Size(obj->tp_size));
	printf("[*] Allocated = %li\n", obj->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE(PyList_GetItem(p, i))->tp_name);
}
