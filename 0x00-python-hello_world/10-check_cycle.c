#include "lists.h"

/**
 * check_cycle - check if a linked list contains a cycle
 * @list: linked list
 * @head: listint_t arguments
 * Return: 0 if there is no cycle, 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = head, *fast = head;

	if (head && head->next)
	{
		while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (slow == fast)
		{
			slow = head;
			while (slow != fast)
			{
				slow = slow->next;
				fast = fast->next;
			}
			return (1);
		}
	}
	}
	return (0);
}
