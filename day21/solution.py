f = open("input.in")
reading = True
data = {}


while reading:
    line = f.readline()
    if line == '':
        reading = False
        break
    line = line.strip().split()

    if len(line) == 2:
        data[line[0][:-1]] = int(line[1])
    else:
        data[line[0][:-1]] = {'need': (line[1], line[3]), 'op': line[2]}

data['root']['op'] = '-'


def eval_monk(name, x):
    if name == 'humn':
        return x
    monk = data[name]
    if type(monk) is int:
        return monk 
    else:
        monk1, monk2 = monk['need']
        return eval('eval_monk(monk1, x) ' + monk['op'] 
                    + 'eval_monk(monk2, x)')


def secant(x1, x2, max_steps):
    y1 = eval_monk('root', x1)
    i, y2 = 0, 0
    while i < max_steps and x1 != x2:
        y2 = eval_monk('root', x2)
        delta = (y2 - y1)/(x2 - x1)
        x3 = x2 - y2 / delta
        y3 = eval_monk('root', x3)
        x1, x2 = x2, x3
        y1, y2 = y2, y3
        i += 1
    return (x2, y2, i)


print(secant(0, 1000, 100))    # 4 steps ... 

#  Test that this is the right value:
#  print(eval_monk('root', 3360561285172))
