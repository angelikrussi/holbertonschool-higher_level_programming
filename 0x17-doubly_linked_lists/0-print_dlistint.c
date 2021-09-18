#include "lists.h"

/**
 * print_dlistint - this  function that prints all the elements
 *  of a dlistint_t list.
 * @h: ponter
 * Return: the number of nodes
 */

size_t print_dlistint(const dlistint_t *h)
{
	size_t counter = 0;

	for (counter; h; counter++)
	{
		printf("%d\n"h->n);
		h->next;
	}
	return (counter);
}
