def recognizes_ending_with_ab(input_string):
    # States:
    # 0: Initial / string does not end with 'a' or 'ab'
    # 1: String ends with 'a'
    # 2: String ends with 'ab' (Accepting state)
    
    current_state = 0

    # Transition table: (current_state, character) -> next_state
    transitions = {
        (0, 'a'): 1, (0, 'b'): 0,
        (1, 'a'): 1, (1, 'b'): 2,
        (2, 'a'): 1, (2, 'b'): 0,
    }

    for char in input_string:
        if (current_state, char) in transitions:
            current_state = transitions[(current_state, char)]
        else:
            # Transition to a non-accepting state on any other character
            current_state = 0

    return current_state == 2


# Example usage:
test_strings = ["cab", "abab", "aba", "b", "hello_ab", "abc"]

for s in test_strings:
    result = "Accepted" if recognizes_ending_with_ab(s) else "Rejected"
    print(f"'{s}': {result}")