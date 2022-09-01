#include "lists.h"
/**
 * add_dnodeint - add new node at the begining of linked list
 * @head: linked list head pointer
 * @n: noode value to be added
 * Return: address of new element
 */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
{
	dlistint_t *new = *head;

	new = malloc(sizeof(dlistint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	new->next = (*head);
	new->prev = NULL;
	if (*head)
		(*head)->prev = new;
	*head = new;
	return (new);
}
