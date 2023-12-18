with open("input.txt") as f:
    lines = f.readlines()

def find_differences(history):
    deltas = []
    for i in range(len(history)-1):
        deltas.append(history[i+1] - history[i])
    print(deltas)
    if set(deltas) == {0}:
        return history[-1]
    else:
        return(find_differences(deltas) + history[-1])

histories = []
for line in lines:
    histories.append([int(x) for x in line.strip().split()])

last_terms=[]
for history in histories:
    last_terms.append(find_differences(history))

print(sum(last_terms))