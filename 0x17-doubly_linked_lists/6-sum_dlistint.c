#include "lists.h"
/**
 * sum_dlistint - returns some of linked list element data
 * @head: linked list head pointer
 *
 * Return: linked list data sum.
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *current = head;
	int sum = 0;

	if (head == NULL)
		return (0);
	while (current)
	{
		sum += current->n;
		current = current->next;
	}
	return (sum);
}
