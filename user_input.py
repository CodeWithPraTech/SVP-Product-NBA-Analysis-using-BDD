from nba import NBA
import random

def get_user_input():
    num_automata = int(input("Enter the number of NBAs (k): "))
    num_states = int(input("Enter the number of states for each NBA: "))
    alphabet_size = int(input("Enter the size of the alphabet for each NBA: "))
    
    return num_automata, num_states, alphabet_size

def generate_random_nba(num_states, alphabet_size):
    states = [f'q{i}' for i in range(num_states)]
    alphabet = {chr(ord('a') + i) for i in range(alphabet_size)}
    transitions = {state: {symbol: set() for symbol in alphabet} for state in states}

    for state in states:
        for symbol in alphabet:
            transitions[state][symbol] = {random.choice(states) for _ in range(random.randint(1, num_states))}

    initial_states = {random.choice(states) for _ in range(random.randint(1, num_states))}
    accepting_states = {random.choice(states) for _ in range(random.randint(1, num_states))}

    return NBA(states, alphabet, transitions, initial_states, accepting_states)




def main():
    
    num_automata, num_states, alphabet_size = get_user_input()
    nbas = [generate_random_nba(num_states, alphabet_size) for _ in range(num_automata)]

    # Display the generated NBAs
    for i, nba in enumerate(nbas, 1):
        print(f"Generated NBA {i}:")
        print(nba)

    return nbas
