#include "main.h"
#include <stdlib.h>

/**
 * _calloc - Allocates memory for an array and initializes to zero
 * @nmemb: Number of elements in the array
 * @size: Size of each element
 * 
 * Return: Pointer to the allocated memory
 */
void *_calloc(unsigned int nmemb, unsigned int size)
{
    void *ptr;
    unsigned int i;

    if (nmemb == 0 || size == 0)
        return (NULL);

    ptr = malloc(nmemb * size);

    if (ptr == NULL)
        return (NULL);

    for (i = 0; i < nmemb * size; i++)
        *((char *)ptr + i) = 0;

    return (ptr);
}

