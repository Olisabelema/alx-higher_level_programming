/*
 * File: 103-python.c
 * Auth: Olisa Belema
 */

#include <Python.h>

void print_python_list(PyObject *list_object);
void print_python_bytes(PyObject *bytes_object);
void print_python_float(PyObject *float_object);

/**
 * print_python_list - This function prints essential
 * information about Python lists.
 * @list_object: A pointer to a PyObject representing a list object.
 */
void print_python_list(PyObject *list_object)
{
    Py_ssize_t size, alloc, j;
    const char *type;
    PyListObject *list_ptr = (PyListObject *)list_object;
    PyVarObject *var_ptr = (PyVarObject *)list_object;

    size = var_ptr->ob_size;
    alloc = list_ptr->allocated;

    fflush(stdout);

    printf("[*] Python list info\n");
    if (strcmp(list_object->ob_type->tp_name, "list") != 0)
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", alloc);

    for (j = 0; j < size; j++)
    {
        type = list_ptr->ob_item[j]->ob_type->tp_name;
        printf("Element %ld: %s\n", j, type);
        if (strcmp(type, "bytes") == 0)
            print_python_bytes(list_ptr->ob_item[j]);
        else if (strcmp(type, "float") == 0)
            print_python_float(list_ptr->ob_item[j]);
    }
}

/**
 * print_python_bytes - This function prints essential
 * information about Python byte objects.
 * @bytes_object: A pointer to a PyObject representing a byte object.
 */
void print_python_bytes(PyObject *bytes_object)
{
    Py_ssize_t size, j;
    PyBytesObject *bytes_ptr = (PyBytesObject *)bytes_object;

    fflush(stdout);

    printf("[.] bytes object info\n");
    if (strcmp(bytes_object->ob_type->tp_name, "bytes") != 0)
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    printf("  size: %ld\n", ((PyVarObject *)bytes_object)->ob_size);
    printf("  trying string: %s\n", bytes_ptr->ob_sval);

    if (((PyVarObject *)bytes_object)->ob_size >= 10)
        size = 10;
    else
        size = ((PyVarObject *)bytes_object)->ob_size + 1;

    printf("  first %ld bytes: ", size);
    for (j = 0; j < size; j++)
    {
        printf("%02hhx", bytes_ptr->ob_sval[j]);
        if (j == (size - 1))
            printf("\n");
        else
            printf(" ");
    }
}

/**
 * print_python_float - This function prints important
 * information about Python float objects.
 * @float_object: A pointer to a PyObject representing a float object.
 */
void print_python_float(PyObject *float_object)
{
    char *buffer = NULL;

    PyFloatObject *float_ptr = (PyFloatObject *)float_object;

    fflush(stdout);

    printf("[.] float object info\n");
    if (strcmp(float_object->ob_type->tp_name, "float") != 0)
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    buffer = PyOS_double_to_string(float_ptr->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", buffer);
    PyMem_Free(buffer)
