#include "lists.h"
#include <stdlib.h>

/**
 * insert_node -insert node in incrising order.
 *
 * @head: linked list head.
 * @number: list data to be inserted
 * Return: new node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp, *current;

	new = malloc(sizeof(listint_t));

	new->n = number;
	new->next = NULL;

	current = *head;
	if (*head == NULL)
	{
		*head = new;
		return (new);
	}
	if (current->n > number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current)
	{
		tmp = current->next;
		if (tmp)
		{
			if (tmp->n > number)
			{
				current->next = new;
				new->next = tmp;
				return (new);
			}
		}
		else
		{
			current->next = new;
			return (new);
		}
		current = current->next;
	}
	return (NULL);
}
