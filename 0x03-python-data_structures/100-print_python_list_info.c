#include <Python.h>
#include <stdio.h>
#include <object.h>
#include <listobject.h>

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int i;
	/*PyListObject *obj = (PyListObject *)p;*/

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", (PyListObject *)p->allocated);
	for (i = 0; i < size; i++)
		printf("Element %i: %s\n", i, Py_TYPE((PyListObject *)p->ob_item[i])->tp_name);
}
