class Node():
	def __init__(self, value=None, nextNode=None):
		self.value = value 
		self.next = nextNode
	def retrieve_value(self):
		return self.value # to return the value of the node
	def next_node(self):
		return self.next # returns the next node
	def set_next_node(self, next_node):
		self.next = next_node # set next node

## test for instances of Node class ##
node1 = Node(4)
node1.retrieve_value()
node2 = Node(6)
node1.set_next_node(node2)
node1.next_node().retrieve_value()

class LinkedList():
	def __init__(self, value=None):
		self.head = Node(value) # define value as an instance of Node class and assign it to the head of LinkedList
	def size(self):
		current = self.head # set to head node
		count = 0
		while current:
			count += 1 # add 1 to count everytime while loop is executed 
			current = current.next_node() # obtain the next node in the list, by referring to Node class (as above)
		return count
	def addNode(self, new_value):
		new_node = Node(new_value) # create a new instance of Node class for new_value
		current = self.head 
		while current: # loops over the list of nodes
			if current.next_node() is None: 
				current.set_next_node(new_node) # if next node is empty, then set new_node to next node
				break
			else:
				current = current.next_node() # if not go to the next node
	def addNodeAfter(self, new_value, after_node):
		current = self.head
		new_node = Node(new_value)
		while current: # loops over list of nodes
			if current.retrieve_value() == after_node: # if after_node is found, 
				if current.next_node() is None: # and if there are no nodes after after_node 
					current.set_next_node(new_node) # add new node in the next position
				else: # else if there are nodes after after_node
					new_node.set_next_node(current.next_node()) # set these nodes after new_node
					current.set_next_node(new_node) # then combine previous nodes (including after_node) with the new_node
				break
			else:
				current = current.next_node()
	def addNodeBefore(self, new_value, before_node):
		current = self.head
		new_node = Node(new_value)
		if current.retrieve_value() == before_node: # if before_node is the head node
			new_node.set_next_node(current) # then set before_node after new_node
			self.head = new_node # redefine new_node as the head node
		else: # else if before_node is not the head node
			count = 0
			while current:
				if current.retrieve_value() == before_node:
					break
				else:
					current = current.next_node()
					count += 1 
					# we want to find where the before_node is => so we set a counter to identify the index position
			current = self.head
			for i in range(count-1):
				current = current.next_node() # we want to move to the node just before before_node
			new_node.set_next_node(current.next_node()) # append before_node after new_node
			current.set_next_node(new_node) # combine previous nodes with new_node
	def removeNode(self, node_to_remove):
		current = self.head 
		if node_to_remove.retrieve_value() == current.retrieve_value(): # if node_to_remove is the head_node
			current = current.next_node() # go to the next node 
			current.set_next_node(current.next_node()) # add everything after next node to next node
			self.head = current # reassign a new head node
		else:
			count = 0
			after_nodes = None
			while current:
				if current.retrieve_value() == node_to_remove.retrieve_value(): # if node_to_remove is found
					after_nodes = current.next_node() # assign node after node_to_remove to after_nodes
					break
				else:
					current = current.next_node() # continue looping over next nodes to find node_to_remove
					count += 1
			current = self.head # start from beginning
			for i in range(count-1):
				current = current.next_node() # go to the node just before node_to_remove
			current.set_next_node(after_nodes) # append after_nodes to this node
	def removeNodesByValue(self, value):
		current = self.head 
		new_node = Node(value)
		while current: # recursion using removeNode => find and remove new_node, and return new list => do it again 
			self.removeNode(new_node)
			current = current.next_node()
	def reverse(self):
		# suppose we have 1,2,3,4 and we want 4,3,2,1
		previous = None 
		current = self.head # set 1 as the head node
		while current:
			next_node = current.next # assign 2 to next_node (in next iteration, 3)
			current.next = previous # assign None to current.next (in next iteration, 1)
			previous = current  # assign 1 to previous (in next iteration, 2)
			current = next_node # go to next node, which is 2 (in next iteration, 3)
			# so after two iterations, previous = 2,1
		self.head = previous
		# set head to previous
	def print_list(self):
		current = self.head
		while current: # loops over each node
			print(current.retrieve_value()) # prints the value for each node
			current = current.next_node() 

## test for instances of LinkedList class ##

list1 = LinkedList(4)
list1.size()
list1.addNode(6)
list1.addNode(8)
list1.size()
list1.print_list()
list1.addNodeAfter(3, 6)
list1.addNodeBefore(4, 8)
list1.print_list()
list1.removeNode(Node(6))
list1.removeNodesByValue(4)
list1.print_list()
list1.reverse()
list1.print_list()
