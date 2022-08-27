#include "lists.h"
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
/**
 * reverse - reverse single list sequence;
 * @second_head: second half single list head
 *
 * Return: alwaya none
 */
void reverse(listint_t **second_head)
{
	listint_t *prev = NULL, *next, *current = *second_head;

	while (current)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*second_head = prev;
}
/**
 * compare - checks if the single lis is palindrome or not
 * @head: single list head
 * @second_head: second half single list head pointer
 * Return: 1 on success and 0 on failure
 */

bool compare(listint_t **head, listint_t *second_head)
{
	listint_t *first = *head, *second = second_head;

	while (first && second)
	{
		if (first->n != second->n)
			return (0);
		first = first->next;
		second = second->next;
	}
	return (1);
}
/**
 * is_palindrome - checks if the single lis is palindrome or not
 * @head: single list head
 *
 * Return: 1 on success and 0 on failure
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *mid = NULL, *slowprev, *second;
	bool check = true;

	slow = *head;
	fast = *head;
	if (*head == NULL)
		return (1);
	while (fast && fast->next)
	{
		fast = fast->next->next;
		slowprev = slow;
		slow = slow->next;
	}
	if (fast != NULL)
	{
		mid = slow;
		slow = slow->next;
	}
	second = slow;
	slowprev->next = NULL;
	reverse(&second);
	check = compare(head, second);
	reverse(&second);
	if (mid)
	{
		slowprev->next = mid;
		mid->next = second;
	}
	else
		slowprev->next = second;
	if (check)
		return (1);
	else
		return (0);
}
