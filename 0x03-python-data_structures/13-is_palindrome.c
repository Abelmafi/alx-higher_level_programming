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
	int size = 0, j = 0, i = 0, mid, *s;

	if (*head == NULL)
		return (1);
	tmp = *head;
	tmp2 = *head;
	while (tmp)
	{
		tmp = tmp->next;
		size++;
	}
	s = (int *)malloc(sizeof(int) * size + 1);
	while (tmp2)
	{
		s[j] = tmp2->n;
		tmp2 = tmp2->next;
		j++;
	}
	j--;
	mid = j / 2;
	for (; j > mid; j--)
	{
		if (s[j] != s[i])
			return (0);
		i++;
	}
	return (1);
}
