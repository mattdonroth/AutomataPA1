import sys

def runMachine(dfa, start, accept, string):
    state = str(start)
    for char in string:
        try:
            state = dfa[state][char]
        except:
            print("Could not find key: ", char, " in state: ", state)
    return str(state)

#declaring out dfa representation
dfa_dic = {}
#opening the input
input = tuple(open(sys.argv[1], "r"))
#pulling the number of states
num_states = int(input[0])
#pulling our alphabet
alphabet = input[1].strip()
#getting the number of transitions in our automata
num_transitions = num_states*len(alphabet)
#creating an iterable so we can skip the first two lines
iterinput = iter(input)
next(iterinput)
next(iterinput)
#error checking
print("number of states", num_states)
print("the alphabet", alphabet)
#count is used to stop inputing the transitions when we reach the start and accept states
count = 0
print("NUM TRANSITIONS:", num_transitions)
for line in iterinput:
    if(count < num_transitions):
        count+=1
        #splitting the transition
        a,b,c = line.split()
        a = a.replace('\'', '')
        b = b.replace('\'', '')
        c = c.replace('\'', '')
        #adding the transition to our 2d dictionary
        dfa_dic[a] = dfa_dic.get(a, {})
        dfa_dic[a][b] = c
        continue
    else:
        #setting the start state
        start_state = int(line)
        break
#grabbing the accept states
accept_states = next(iterinput)
print("Start state", start_state)
print("accept states", accept_states)
print("running the machine")
#iterating through the strings
for string in iterinput:
    string = string.strip()
    #print("attempting to run string: ", string)
    ans = runMachine(dfa_dic, start_state, accept_states, string)
    if ans in accept_states:
        print("Accept")
    else:
        print("Reject")

#error checking
#print(dfa_dic)


