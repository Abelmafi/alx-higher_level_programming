#include "lists.h"
/**
 * add_dnodeint_end - add node at the end of linked list
 * @head: linked list head pointer
 * @n: linked list value
 *
 * Return: linked list new node
 */
dlistint_t *add_dnodeint_end(dlistint_t **head, const int n)
{
	dlistint_t *new, *last = *head;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = NULL;

	if (*head == NULL)
	{
		new->prev = NULL;
		*head = new;
		return (new);
	}
	while (last->next)
		last = last->next;
	last->next = new;
	new->prev = last;
	return (new);
}
