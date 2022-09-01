#include "lists.h"
#include <stdlib.h>
/**
 * print_dlistint - print double linked list
 * h: linked list head pointer
 * Return: the number of node in list
 */
size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *new;
	int n = 0;

	new = h;
	if (h == NULL)
		return (0);
	while (new)
	{
		printf("%d\n", new->n);
		new = new->next;
		n++;
	}
	return (n);
}
