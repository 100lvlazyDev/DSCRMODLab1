import json

with open('matrix.json', 'r') as file:
    data = json.load(file)
#print(type(data))

def getmatrix():
    mat = (data)
    return mat


# for row in data["var4"]:
#     for col in row:
#         print(col)
