#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.size = 0
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty.
        TODO: Running time: O(1) Why and under what conditions?
        one step, no loopage"""

        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(1) Why and under what conditions?
        one step, no loopage"""
        # TODO: Loop through all nodes and count one for each
        # node = self.head
        # size = 0
        # while node is not None:
        #     size += 1
        #     node = node.next
        return self.size


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
        because we only change the tail...no loopage"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        new_node = Node(item)
        old_tail = self.tail
        self.tail = new_node
        if old_tail is not None:
          old_tail.next = new_node
        if self.head is None:
            self.head = new_node
        self.size += 1


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(1) Why and under what conditions?
        because we only change the first node and never loop"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        new_node = Node(item)
        first_node = self.head
        self.head = new_node
        new_node.next = first_node
        if self.tail is None:
            self.tail = new_node
        self.size += 1

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        cur_node = self.head
        while cur_node:
            if quality(cur_node.data):
                return cur_node.data
            cur_node = cur_node.next
        return None

    def replace(self, word, replacement):
        cur_node = self.head
        while cur_node:
            if curr_node.data == word:
                cur_node.data = replacement
                return
            curr_node = cur_node.next
        return None


    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        '''
        loop throgh the linked list
        - store the previous node
        - when you find the node:
            - take its pointer and replace the previous node's pointer with its pointer'''

        # if were deleting the first item in the list:
        if self.is_empty():
            raise ValueError('Linked List is empty.')
        if self.head.data == item:
            if self.head.next == None:
                self.head = None
                self.tail = None
                self.size -= 1
                return
            self.head = self.head.next
            self.size -= 1
            return
        # Create two variables called prev_node and curr_node
        prev_node = self.head
        curr_node = self.head.next


        # this while loop will check if the current node is the item.
        # if it is then prev_node.next = cur_node.next, deleting currnode.
        while curr_node:
            if curr_node is None:
                self.tail = prev_node
                self.size -= 1
                return
            if curr_node.data == item:
                if curr_node == self.tail:
                    self.tail = prev_node
                    prev_node.next = None
                    self.size -= 1
                    return
                prev_node.next = curr_node.next
                self.size -= 1
                return
            prev_node = curr_node
            curr_node = curr_node.next
        raise ValueError('Item not found: {}'.format(item))






def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))


if __name__ == '__main__':
    test_linked_list()
