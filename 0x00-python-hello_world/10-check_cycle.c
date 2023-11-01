#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
  *check_cycle - checks if lists is cyclical
  *@list: pointer to lists to check
  *Return: 1 if cyclical, or 0
  */

int check_cycle(listint_t *list)
{
	listint_t *slow = list, *fast = list;
	
	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
