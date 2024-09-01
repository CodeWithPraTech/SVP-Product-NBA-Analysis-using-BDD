from nba import NBA
from itertools import product

def dfs_reachable_states_iterative(initial_states, transitions):
    visited = set()
    reachable_transitions = {}

    # Use a stack to replace the recursion
    stack = list(initial_states)

    while stack:
        state = stack.pop()

        if state in visited:
            continue

        visited.add(state)

        if state not in transitions:
            continue

        reachable_transitions[state] = transitions[state]

        for symbol in transitions[state]:
            for next_state in transitions[state][symbol]:
                if next_state not in visited:
                    stack.append(next_state)

    return visited, reachable_transitions

# Given the product_nba function
def product_nba(nbas):
    states = []
    transitions = {}
    initial_states = set()
    accepting_states = set()

    # Generate product state space with labels 1,2,...k+1
    def generate_product_states(state_tuple, label):
        return f"({','.join(state_tuple)},{label})"

    num_automata = len(nbas)
    label_count = num_automata + 1

    # Iterate through all possible state combinations
    for state_tuple in product(*(nba.states for nba in nbas)):
        for label in range(1, label_count + 1):
            state = generate_product_states(state_tuple, label)
            states.append(state)

    # Define transitions
    for state in states:
        state_tuple = tuple(state[1:-2].split(','))
        label = int(state[-2])
        transitions[state] = {}

        # Iterate through all possible symbols
        for symbol in nbas[0].alphabet:
            next_states = set()
            for next_state_tuple in product(*(nba.transitions[state_tuple[i]].get(symbol, {}) for i, nba in enumerate(nbas))):
                next_label = label
                if label < label_count:
                    if all(next_state_tuple[i] in nbas[i].accepting_states for i in range(label)):
                        next_label += 1
                if label == label_count:
                    next_label = 1

                next_states.add(generate_product_states(next_state_tuple, next_label))

            transitions[state][symbol] = next_states

    # Initial states
    for state_tuple in product(*(nba.initial_states for nba in nbas)):
        initial_states.add(generate_product_states(state_tuple, 1))

    # All states in transitions
    states = [state for state, symbol_dict in transitions.items()]

    # Accepting states
    for state in states:
        if int(state[-2]) == label_count:
            accepting_states.add(state)

    # Get reachable states using iterative DFS
    reachable_states, reachable_transitions = dfs_reachable_states_iterative(initial_states, transitions)

    # Filter accepting states that are reachable
    reachable_accepting_states = accepting_states.intersection(reachable_states)

    return NBA(reachable_states, nbas[0].alphabet, reachable_transitions, initial_states, reachable_accepting_states)
