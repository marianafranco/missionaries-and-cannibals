import math

#______________________________________________________________________________
# Queues: FIFOQueue (source: http://aima-python.googlecode.com/svn/trunk/utils.py)

class Queue:
    """Queue is an abstract class/interface.
    Supports the following methods and functions:
        q.append(item)  -- add an item to the queue
        q.extend(items) -- equivalent to: for item in items: q.append(item)
        q.pop()         -- return the top item from the queue
        len(q)          -- number of items in q (also q.__len())
        item in q       -- does q contain item?
    If Python ever gets interfaces, Queue will be an interface."""

    def __init__(self):
        abstract

    def extend(self, items):
        for item in items: self.append(item)

class FIFOQueue(Queue):
    """A First-In-First-Out Queue."""
    def __init__(self):
        self.A = []; self.start = 0
    def append(self, item):
        self.A.append(item)
    def __len__(self):
        return len(self.A) - self.start
    def extend(self, items):
        self.A.extend(items)
    def pop(self):
        e = self.A[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.A)/2:
            self.A = self.A[self.start:]
            self.start = 0
        return e
    def __contains__(self, item):
        return item in self.A[self.start:]

#______________________________________________________________________________
# Missionaries and Cannibals Problem

class State():
	def __init__(self, cannibalLeft, missionaryLeft, boat, cannibalRight, missionaryRight):
		self.cannibalLeft = cannibalLeft
		self.missionaryLeft = missionaryLeft
		self.boat = boat
		self.cannibalRight = cannibalRight
		self.missionaryRight = missionaryRight
		self.parent = None

	def is_goal(self):
		if self.cannibalLeft == 0 and self.missionaryLeft == 0:
			return True
		else:
			return False

	def is_valid(self):
		if self.missionaryLeft >= 0 and self.missionaryRight >= 0 \
                   and self.cannibalLeft >= 0 and self.cannibalRight >= 0 \
                   and (self.missionaryLeft == 0 or self.missionaryLeft >= self.cannibalLeft) \
                   and (self.missionaryRight == 0 or self.missionaryRight >= self.cannibalRight):
			return True
		else:
			return False

def successors(cur_state):
	children = [];
	if cur_state.boat == 'left':
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 2, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 2)
		## Two missionaries cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 2, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 2, cur_state.missionaryRight)
		## Two cannibals cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight + 1)
		## One missionary and one cannibal cross left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft - 1, 'right',
                                  cur_state.cannibalRight, cur_state.missionaryRight + 1)
		## One missionary crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft - 1, cur_state.missionaryLeft, 'right',
                                  cur_state.cannibalRight + 1, cur_state.missionaryRight)
		## One cannibal crosses left to right.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	else:
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 2, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 2)
		## Two missionaries cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 2, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 2, cur_state.missionaryRight)
		## Two cannibals cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight - 1)
		## One missionary and one cannibal cross right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft, cur_state.missionaryLeft + 1, 'left',
                                  cur_state.cannibalRight, cur_state.missionaryRight - 1)
		## One missionary crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
		new_state = State(cur_state.cannibalLeft + 1, cur_state.missionaryLeft, 'left',
                                  cur_state.cannibalRight - 1, cur_state.missionaryRight)
		## One cannibal crosses right to left.
		if new_state.is_valid():
			new_state.parent = cur_state
			children.append(new_state)
	return children

def breadth_first_search():
	initial_state = State(3,3,'left',0,0)
	if initial_state.is_goal():
		return initial_state
	frontier = FIFOQueue()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop()
		if state.is_goal():
			return state
		explored.add(state)
		children = successors(state)
		for child in children:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print "(" + str(state.cannibalLeft) + "," + str(state.missionaryLeft) \
                              + "," + state.boat + "," + str(state.cannibalRight) + "," + \
                              str(state.missionaryRight) + ")"

def main():
	solution = breadth_first_search()
	print "Missionaries and Cannibals solution:"
	print "(cannibalLeft,missionaryLeft,boat,cannibalRight,missionaryRight)"
	print_solution(solution)
	
# if called from the command line, call main()
if __name__ == "__main__":
    main()
