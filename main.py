#convert a dictionary representation of a graph to a list representation.
def dict_to_list(d):
  l = []
  for key, value in d.items():
    for vert in value:
      if (vert, key) not in l:
        l.append((key, vert))
  return l

d = {0: [1, 2], 1: [0, 2, 4], 2: [0, 1, 3], 3: [2, 4], 4: [1, 3]}
print(dict_to_list(d))
#result is
#[(0, 1), (0, 2), (1, 2), (1, 4), (2, 3), (3, 4)]



#convert a list representation of a graph to a dictionary representation.
def list_to_dict(l):
  d = {}
  for edge in l:
    if edge[0] not in d:
      d[edge[0]] = []
    if edge[1] not in d:
      d[edge[1]] = []
    d[edge[0]].append(edge[1])
    d[edge[1]].append(edge[0])
  return d

l = [(0, 1), (0, 2), (1, 2), (1, 4), (2, 3), (3, 4)]
print(list_to_dict(l))
#result is
#d = {0: [1, 2],
# 1: [0, 2, 4],
# 2: [0, 1, 3],
# 3: [2, 4],
# 4: [1, 3]}


#convert a list representation of a graph to a matrix representation.
def list_to_matrix(l):
  m = [[]]
  for edge in l:
    m[edge[0]][edge[1]] = 1
    m[edge[1]][edge[0]] = 1
  return m

# Your code goes here.
l = [(0, 1), (0, 2), (1, 2), (1, 4), (2, 3), (3, 4)]
result = list_to_matrix(l)
for row in result:
  print(row)

#result is
# [0, 1, 1, 0, 0]
# [1, 0, 1, 0, 1]
# [1, 1, 0, 1, 0]
# [0, 0, 1, 0, 1]
# [0, 1, 0, 1, 0]

#convert a matrix representation of a graph to a dictionary representation.
def matrix_to_dict(m):
  return

# Your code goes here.
m = [[0, 1, 1, 0, 0],
[1, 0, 1, 0, 1],
[1, 1, 0, 1, 0],
[0, 0, 1, 0, 1],
[0, 1, 0, 1, 0]]

print(matrix_to_dict(m))
#result is
# d = {0: [1, 2],
# 1: [0, 2, 4],
# 2: [0, 1, 3],
# 3: [2, 4],
5
# 4: [1, 3]}


#convert a matrix representation of a graph to a list representation.
def matrix_to_list(m):
  return 

# Your code goes here.
m = [[0, 1, 1, 0, 0],
[1, 0, 1, 0, 1],
[1, 1, 0, 1, 0],
[0, 0, 1, 0, 1],
[0, 1, 0, 1, 0]]

print(matrix_to_list(m))
#result is
#l = [(0, 1), (0, 2), (1, 2), (1, 4), (2, 3), (3, 4)]