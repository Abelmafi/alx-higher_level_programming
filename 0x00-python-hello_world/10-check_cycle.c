#include "lists.h"
/**
 * check_cycle - checks if a linked list has cycle or not
 * @list: linkedlist head
 *
 * Return: 0 if it has not 1 if it has
 */
int check_cycle(listint_t *list)
{
	listint_t *tmp, *current;
	int i, n = 1;

	if (list == NULL)
		return (0);
	tmp = list;
	tmp = tmp->next;
	if (tmp == NULL)
		return(0);
	current = list;
	while (tmp)
	{
		for (i = 0; i < n; i++)
		{
			if (tmp->next == current)
				return (1);
			current = current->next;
		}
		current = list;
		tmp = tmp->next;
		n++;
	}
	return (0);
}

