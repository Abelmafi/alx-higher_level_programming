#include "lists.h"
/**
 * delete_dnodeint_at_index - delete liked list node at index
 * @head: linked list head pointer
 * @index: node index to be deleted
 *
 * Return: 1 on success and -1 on failure.
 */
int delete_dnodeint_at_index(dlistint_t **head, unsigned int index){
	dlistint_t *del_node = *head;
	unsigned int n = 0;

	if (*head == NULL || index < 0)
		return (-1);
	if (index == 0)
	{
		if (del_node->next != NULL)
			*head = del_node->next;
		else
			*head = NULL;
		free(del_node);
		return (1);
	}
	while (n < index && del_node)
	{
		del_node = del_node->next;
		n++;
	}
	if (del_node == NULL)
		return (-1);
	else
	{
		if (del_node->prev != NULL)
			del_node->prev->next = del_node->next;
		if (del_node->next != NULL)
			del_node->next->prev = del_node->prev;
		free(del_node);
	}
	return (1);
}


