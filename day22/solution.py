f = open("input.in")
reading = True
data = {}
map_arr = []
instr = ''
map_read = False
map_width = 0
map_height = 0

while reading:
	line = f.readline()
	if line == '':
		reading = False
		break
	if line == '\n':
		map_read = True
	if map_read:
		instr = line.strip()
	else:
		map_arr += [line[:-1]]
		map_height += 1
		map_width = max(map_width, len(map_arr[-1]))

# Padding
for i in range(len(map_arr)):
	diff = (map_width-len(map_arr[i]))
	map_arr[i] = ' ' + map_arr[i] + ' '* diff + ' '
map_arr.insert(0, ' '*(map_width + 2))
map_arr.append(' '*(map_width + 2))

# Defining and gluing edges of map
edges = {}
edge_desc = {(1, 1,51,0,1), (2, 1,101,0,1), (3, 50,101,0,1), (4, 1,150,1,0), (5, 1,51,1,0), 
			 (6, 51,51,1,0), (7, 51,100,1,0), (8, 101,1,0,1), (9, 150,51,0,1), (10, 150,1,-1,0), 
			 (11, 150,100,-1,0), (12, 151,1,1,0), (13, 151,50,1,0), (14, 200,1,0,1)}

for (i,x,y,a,b) in edge_desc:
	edges[i] = [(x+a*c, y+b*c) for c in range(50)]

edge_pairs = [(1,12), (2,14), (3,7), (4,11), (5,10), (6,8), (9,13)]
# Remember.... 0 : > ... 1 : v ... 2 : < ... 3 : ^
edge_pairs_dir = [(3,0), (3,3), (1,2), (0,2), (2,0), (2,1), (1,2)]
edge_glue = {}

for i in range(7):
	e1, e2 = edge_pairs[i]
	d1, d2 = edge_pairs_dir[i]
	for j in range(50):
		x, y = edges[e1][j]
		s, t = edges[e2][j]
		edge_glue[(x,y,d1)] = (s,t,d2)
		edge_glue[(s,t,(d2+2)%4)] = (x,y,(d1+2)%4)


def next_instr(ins):
	i = 0
	while i < len(ins) and ins[i] not in {'R', 'L'}:
		i += 1
	if i == len(ins):
		return (int(ins), 'end', '')
	else:
		return (int(ins[0:i]), ins[i], ins[i+1:])


rem_instr = instr
(x, y) = (1, map_arr[1].index('.'))
z = 0
dirs = [(0,1), (1,0), (0,-1), (-1,0)]
action_dict = {'R': 1, 'L': -1}

while rem_instr != '':
	steps, action, rem_instr = next_instr(rem_instr)

	while steps > 0:
		(s,t) = (x + dirs[z][0], y + dirs[z][1])
		if map_arr[s][t] == '#':
			break
		elif map_arr[s][t] == '.':
			(x,y) = (s,t)
		elif map_arr[s][t] == ' ':
			(s,t,r) = edge_glue[(x,y,z)]
			if map_arr[s][t] == '#':
				break
			else:
				(x,y,z) = (s,t,r)
		steps -= 1
	if action != 'end':
		z = (z + action_dict[action]) % 4

print(1000*x + 4*y + z)
