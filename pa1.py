import sys

dfa_dic = {}
input = tuple(open(sys.argv[1], "r"))
num_states = int(input[0])
alphabet = input[1].strip()
num_transitions = num_states*len(alphabet)
iterinput = iter(input)
next(iterinput)
next(iterinput)
print("number of states", num_states)
print("the alphabet", alphabet)
count = 0
print("NUM TRANSITIONS:", num_transitions)
for line in iterinput:
    if(count < num_transitions):
        count+=1
        print(line)
        continue
    else:
        start_state = int(line)
        break
accept_states = next(iterinput)
print("Start state", start_state)
print("accept states", accept_states)
print("iterating through the strings")
for line in iterinput:
    print(line)


