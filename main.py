import operator

operators = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}


def calc(s):
    if s.startswith('='):
        s = s[1:]
    split_indexes = [s.find(x) for x in operators.keys() if s.find(x) > 0]
    if len(split_indexes) > 0:
        split_index = max(split_indexes)
        return operators[s[split_index]](calc(s[0:split_index]), calc(s[split_index + 1:]))
    if s.startswith('{'):
        return calc(value_array[int(s[1:-1])])
    return int(s)


for line in open('Input_file.txt'):
    value_array = line.replace(" ", "").strip().split(',')
    res = [str(calc(x)) for x in value_array]
    print("""Menu:
a. Print current state
b. Change a value

""")
    while True:
        step= input("# ")
        if step == 'a':
            print(', '.join(["[" + str(i) + ": " + x + "]" for i, x in enumerate(res)]))
        if step.startswith('b'):
            step=step.split()
            value_array[int(step[1])] = step[2]
            res = [str(calc(x)) for x in value_array]
            print(f'Cell #{step[1]} changed to {step[2]}')