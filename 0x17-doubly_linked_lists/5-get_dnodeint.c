#include "lists.h"
/**
 * get_dnodeint_at_index - return linked list pointer at the index
 * @head: head pointer
 * @index: searched node index value
 * Return: return node pointer if it exist or NULL if it doesnt
 */
dlistint_t *get_dnodeint_at_index(dlistint_t *head, unsigned int index)
{
	dlistint_t *current = head;
	unsigned int n = 0;

	if (head == NULL)
		return (NULL);
	while (n < index && current->next != NULL)
	{
		current = current->next;
		n++;
	}
	if (n != index)
		return (NULL);
	return (current);
}
