#include <Python.h>

/**
 * print_python_list_info - Takes a PyObject list as its argument
 * and prints out basic information about the list.
 * @p: A PyObject list.
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size, i;
    PyObject *obj;

    size = PyList_Size(p);

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        printf("Element %ld: ", i);

        obj = PyList_GetItem(p, i);
        printf("%s\n", Py_TYPE(obj)->tp_name);
    }
}
