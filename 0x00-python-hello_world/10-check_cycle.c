#include "lists.h"

/**
 * check_cycle - Function that checks if a linked
 * list contains a cylcle
 * @list: Linked list to be checked
 * Return: 1 on success and zero if not
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *sec = list;

	if (!list)
		return (0);
	while (first && sec && sec->next)
	{
		first = first->next;
		sec = sec->next->next;
		if (first == sec)
			return (1);
	}
	return (0);
}
