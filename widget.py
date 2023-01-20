class State:
    def __init__(self, suc, transitions = []):
        self.success = suc                  # boolean indicating whether State is a success state
        self.transitions = transitions     # nextStates is array of (char, State) tuples capturing the outgoing transitions
        # print(f"Created State representing with {len(self.transitions)} output transitions and success = {self.success}.")

class Widget:
    def __init__(self, start, outStates):
        self.start = start
        self.outStates = outStates
        # print(f"Created widget with {len(outStates)} output states")
   
# points the dangling arrows of a widget to a given target state
def glue(widget, target):
    for state in widget.outStates:
        for trans in state.transitions:
            if(trans[1] == None):
                trans[1] = target
            
            
            
            
# takes a character and returns a Widget corresponding to that character
def char_widget(char):
    newState = State(False, [[char, None]])
    return Widget(newState, [newState])

# takes two widgets and returns a new Widget corresponding to their concatenation
def concat_widget(w1, w2):
    glue(w1, w2.start)
    return Widget(w1.start, w2.outStates)

# takes two widgets and returns a new Widget corresponding to their disjunction            
def or_widget(w1, w2):
    newStart = State(False, [["eps", w1.start], ["eps", w2.start]])
    return Widget(newStart, w1.outStates + w2.outStates)

# takes a widget and returns a new Widget corresponding to its Kleene star
def star_widget(w1):
    newStart = State(False, [["eps", w1.start],["eps", None]])
    glue(w1, newStart)
    return Widget(newStart, [newStart])


    