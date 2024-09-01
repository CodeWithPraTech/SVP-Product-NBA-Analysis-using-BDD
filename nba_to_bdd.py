from dd.autoref import BDD


def nba_to_bdd(nba, bdd):
    # Declare variables for each state and symbol upfront
    state_vars = [f'state_{state}' for state in nba.states]
    symbol_vars = [f'symbol_{symbol}' for symbol in nba.alphabet]
    
    # Declare all variables in the BDD
    bdd.declare(*state_vars)
    bdd.declare(*symbol_vars)

    var_map = {}
    # Create a map from NBA states and symbols to BDD variables
    for state in nba.states:
        var_map[state] = bdd.var(f'state_{state}')

    for symbol in nba.alphabet:
        var_map[symbol] = bdd.var(f'symbol_{symbol}')

    # Initialize BDD with the logical encoding of the transitions
    transition_bdd = bdd.true  # Start with the true BDD (the identity element for AND)

    # Encode transitions into the BDD
    for state, transitions in nba.transitions.items():
        for symbol, next_states in transitions.items():
            for next_state in next_states:
                # Create the transition logic using implication (~A | B instead of A >> B)
                transition_bdd &= ~var_map[state] | (var_map[symbol] & var_map[next_state])

    return transition_bdd

def convert_nbas_to_bdds(nbas, bdd):
    return [nba_to_bdd(nba, bdd) for nba in nbas]
