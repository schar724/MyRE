from asyncio.windows_events import NULL
from typing_extensions import Self


class State:
    def __init__(self, suc, transitions = []):
        self.success = suc                  # boolean indicating whether State is a success state
        self.transitions = transitions     # nextStates is array of (char, State) tuples capturing the outgoing transitions
        print(f"Created State representing with {len(self.transitions)} output transitions and success = {self.success}.")

def epsilonClosure(nfa):
    epsilonStates = nfa.copy()
    checkStates = nfa.copy()
    while len(checkStates) > 0:
        currentState = checkStates.pop()
        for transition in currentState.transitions:
            if transition[0] == "eps" and transition[1] not in epsilonStates:
                epsilonStates.append(transition[1])
                checkStates.append(transition[1])
    return epsilonStates

           