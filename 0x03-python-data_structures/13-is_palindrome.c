#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
/**
 * is_palindrome - checks if the single lis is palindrome or not
 * @head: single list head
 *
 * Return: 1 on success and 0 on failure
 */
int is_palindrome(listint_t **head)
{
	listint_t *tmp, *tmp2;
	int size = 1, j = 0, i = 0, mid;

	if (*head == NULL)
		return (1);
	tmp = *head;
	tmp2 = tmp;
	while (tmp->next)
	{
		tmp = tmp->next;
		size++;
	}
	tmp->next = tmp2;
	mid = size / 2;
	for (i = 0; i < mid; i++)
	{
		if (tmp2->n != tmp->n)
		{
			while (tmp->next != *head)
				tmp = tmp->next;
			tmp->next = NULL;
			return (0);
		}
		for (j = 0; j < size - 1; j++)
			tmp = tmp->next;
		tmp2 = tmp2->next;
	}
	while (tmp->next != *head)
		tmp = tmp->next;
	tmp->next = NULL;
	return (1);
}
