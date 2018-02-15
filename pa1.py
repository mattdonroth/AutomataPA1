import sys
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
print("iterating through the strings")
#iterating through the strings
for line in iterinput:
    print(line)

#error checking
print(dfa_dic)


