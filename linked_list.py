class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        # Check if linked list is empty, if so return an empty array
        llist = []
        if self.head is None:
            return llist

        # traverse thro the linked list

        node = self.head
        while node:
            llist.append(node.data)
            node = node.next_node

        return llist

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)

        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node

        ll_string += " None"
        print(ll_string)

    def insert_begining(self, data):
        # if we were to start with an empty linked list( head=None)
        # we would just create a new node with some data and set next node
        # of that new node to our head i.e head is nolonger none but the newly created node
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_end(self, data):
        # check if linked list is empty
        if self.head is None:
            self.insert_begining(data)

        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head

        while node:
            if node.data["id"] is int(user_id):
                # if a match is found, return the user data(dict)
                return node.data
            # if not, keep looking
            node = node.next_node
        # user id not found, we return none
        return None
