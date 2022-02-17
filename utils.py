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

    def insert_data(self, data):
        # if we were to start with an empty linked list( head=None)
        # we would just create a new node with some data and set next node
        # of that new node to our head i.e head is nolonger none but the newly created node
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node


    def login_user(self, user_id, username):
        node = self.head

        while node:
            if node.data["id"] == int(user_id):
                if node.data["username"] == username:
                    # if a match is found, return the user data(dict)
                    return f"Welcome, you are logged in as {node.data['username']}"
            # if not, keep looking
            node = node.next_node
        # user id not found, we return none
        return f"Invalid login credentials"
