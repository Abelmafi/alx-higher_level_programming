#include "lists.h"
/**
 * insert_dnodeint_at_index - insert not at the index position
 * @h: linkedlist head pointer
 *
 * Return: new linked list pointer;
 */
dlistint_t *insert_dnodeint_at_index(dlistint_t **h, unsigned int idx, int n)
{
	dlistint_t *new, *current = *h;
	unsigned int num = 0;

	new = malloc(sizeof(dlistint_t));
	new->n = n;
	if (idx == 0)
	{
		new->next = *h;
		new->prev = NULL;
		(*h)->prev = new;
		*h = new;
	}
	idx--;
	while (num < idx && current)
	{
		current = current->next;
		num++;
	}
	if (num != idx)
		return (NULL);
	else
	{
		new->next = current->next;
		current->next = new;
		new->prev = current;
		if (new->next != NULL)
			new->next->prev = new;
	}
	return (new);
}
