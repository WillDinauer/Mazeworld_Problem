# astar_search
# William Dinauer, 2022

from SearchSolution import SearchSolution
from heapq import heappush, heappop

class AstarNode:
    # each search node except the root has a parent node
    # and all search nodes wrap a state object

    def __init__(self, state, heuristic, parent=None, transition_cost=0):
        # you write this part
        self.state = state
        self.heuristic = heuristic
        self.parent = parent
        self.transition_cost = transition_cost

    def priority(self):
        # you write this part
        return self.heuristic + self.transition_cost

    # comparison operator,
    # needed for heappush and heappop to work with AstarNodes:
    def __lt__(self, other):
        return self.priority() < other.priority()


# take the current node, and follow its parents back
#  as far as possible. Grab the states from the nodes,
#  and reverse the resulting list of states.
def backchain(node):
    result = []
    current = node
    while current:
        result.append(current.state)
        current = current.parent

    result.reverse()
    return result


def astar_search(search_problem, heuristic_fn):
    # I'll get you started:
    start_node = AstarNode(search_problem.start_state, heuristic_fn(search_problem.start_state))
    pqueue = []
    heappush(pqueue, start_node)

    solution = SearchSolution(search_problem, "Astar with heuristic " + heuristic_fn.__name__)

    visited_cost = {start_node.state: 0}

    # set to keep track of already seen states
    explored = set()
    explored.add(start_node.state)

    # keep looping while there are nodes to search (we break if we reach a goal state)
    while len(pqueue) > 0:
        curr_node = pop_node(pqueue, visited_cost)
        solution.nodes_visited += 1
        curr_state = curr_node.state

        # check for goal state
        if search_problem.goal_test(curr_state):
            solution.cost = curr_node.transition_cost
            solution.path = backchain(curr_node)
            break

        # for every successor of our current state,
        for child in search_problem.get_successors(curr_state):
            g = search_problem.transition_cost(child, curr_node)
            h = heuristic_fn(child)
            f = g+h
            if child not in explored:
                # Unseen state! Add it to the set and priority queue
                explored.add(child)
                child_node = AstarNode(child, h, curr_node, g)
                add_node(child_node, pqueue, visited_cost, f)
            elif child in pqueue and f < visited_cost[child]:
                # update state's value in priority queue
                child_node = AstarNode(child, h, curr_node, g)
                add_node(child_node, pqueue, visited_cost, f)

    return solution


# FUNCTIONS ADAPTED FROM https://docs.python.org/3/library/heapq.html#priority-queue-implementation-notes
# adding a node to the priority queue, 'removing' it from our dictionary if it's already there
def add_node(node, pq, vc, f):
    if node in vc:
        remove_node(node, vc)
    vc[node.state] = f
    heappush(pq, node)

# remove a node from the dictionary by marking its state as 'REMOVED'
def remove_node(node, vc):
    n = vc.pop(node.state)
    n.state = 'REMOVED'

# pop from the heap! Ignore 'REMOVED' states
def pop_node(pq, vc):
    while pq:
        node = heappop(pq)
        if node.state is not 'REMOVED':
            del vc[node.state]
            return node
    return KeyError('pop from an empty priority queue')
