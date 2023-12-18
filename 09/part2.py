with open("input.txt") as f:
    lines = f.readlines()

def find_differences(history):
    deltas = []
    for i in range(len(history)-1):
        deltas.append(history[i+1] - history[i])
    print(deltas)
    if set(deltas) == {0}:
        return history[0]
    else:
        return(history[0] - find_differences(deltas))

histories = []
for line in lines:
    histories.append([int(x) for x in line.strip().split()])

last_terms=[]
for history in histories:
    last_terms.append(find_differences(history))

print(last_terms)
print(sum(last_terms))