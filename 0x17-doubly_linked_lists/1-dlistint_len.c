#include "lists.h"
/**
 * dlistint_len - returns list length
 * @h: list head pointer
 *
 * Return: number of nodes in the list
 */
size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *new = h;
	int n = 0;

	if (h == NULL)
		return (0);
	while (new)
	{
		n++;
		new = new->next;
	}
	return (n);
}
