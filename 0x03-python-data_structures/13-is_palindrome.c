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
	tmp2 = *head;
	while (tmp->next)
	{
		tmp = tmp->next;
		size++;
	}
	/**
	 * s = (int *)malloc(sizeof(int) * size + 1);
	 * while (tmp2)
	 * {
	 * s[j] = tmp2->n;
	 * tmp2 = tmp2->next;
	 * j++;
	 * }
	 * j--;
	 */
	tmp->next = tmp2;
	mid = size / 2;
	for (i = 0; i < mid; i++)
	{
		if (tmp2->n != tmp->n)
			return (0);
		for (j = 0; j < size - 1; j++)
			tmp = tmp->next;
		tmp2 = tmp2->next;
	}
	return (1);
}
