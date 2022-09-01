#include "lists.h"
/**
 * free_dlistint - free double linked list
 * @head: linked list head pointer
 *
 * Return: alwaya nothing
 */
void free_dlistint(dlistint_t *head)
{
	dlistint_t *current;

	while (head)
	{
		current = head;
		head = head->next;
		free(current);
	}
}
