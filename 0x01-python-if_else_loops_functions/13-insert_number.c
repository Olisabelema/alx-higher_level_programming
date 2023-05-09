#include "lists.h"
#include "stddef.h"
#include "stdlib.h"
/**
 * insert_node - inserts a node in a sorted singly linked list
 * @head: pointer to the head of the linked list
 * @number: the value to be inserted
 *
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	/* Declare pointers for new node and current node */
	listint_t *new_node, *current_node;

	/* Allocate memory for new node */
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);

	/* Initialize new node with value and NULL next pointer */
	new_node->n = number;
	new_node->next = NULL;

	/* Special case: empty list */
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	/* Special case: insert at beginning */
	if (number < (*head)->n)
	{
		new_node->next = *head;
		*head = new_node;
		return (new_node);
	}

	/* Traverse the list until we find the correct position */
	current_node = *head;
	while (current_node->next != NULL && current_node->next->n < number)
	current_node = current_node->next;

	/* Insert the new node in the correct position */
	new_node->next = current_node->next;
	current_node->next = new_node;

	return (new_node);
}
