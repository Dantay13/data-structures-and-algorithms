from data_structures.linked_list import LinkedList, Node


def zip_lists(a, b):
    """
    Zips two linked lists together into one, alternating between nodes.
    Returns a reference to the zipped list.
    """
    if not a.head and not b.head:
        # If both lists are empty, return an empty list
        return LinkedList()
    elif not a.head:
        # If the first list is empty, return the second list as it is
        return b
    elif not b.head:
        # If the second list is empty, return the first list as it is
        return a

    # Initialize variables for the current nodes of the two lists
    current_a = a.head
    current_b = b.head
    # Initialize a new linked list to store the zipped list
    zipped_list = LinkedList()

    while current_a or current_b:
        if current_a:
            # Append the node from the first list to the zipped list
            zipped_list.append(current_a.value)
            current_a = current_a.next

        if current_b:
            # Append the node from the second list to the zipped list
            zipped_list.append(current_b.value)
            current_b = current_b.next

    return zipped_list

