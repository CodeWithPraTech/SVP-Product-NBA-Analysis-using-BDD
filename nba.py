class NBA:
    def __init__(self, states, alphabet, transitions, initial_states, accepting_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.initial_states = initial_states
        self.accepting_states = accepting_states

    def __repr__(self):
        return (f"States: {self.states} NoStates: {len(self.states)}\n"
                f"Alphabet: {self.alphabet if self.alphabet else '{}'}\n"
                f"Transitions: {self.transitions if self.transitions else '{}'}\n"
                f"Initial States: {self.initial_states if self.initial_states else '{}'}\n"
                f"Accepting States: {self.accepting_states if self.accepting_states else '{}'}\n")
