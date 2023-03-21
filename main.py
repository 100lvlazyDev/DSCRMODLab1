
import jsonimport
INF = 9999999
MIN = 0
#

G = jsonimport.getmatrix()
N = len(G)
selected_node = [0] * len(G)
no_edge = 0
selected_node[0] = True

# printing for edge and weight

print("Min\n")
print("Edge : Weight\n")
while (no_edge < N - 1):

    minimum = INF

    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    # not in selected and there is an edge
                    if minimum > G[m][n]:
                        minimum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1

print("\nMax\n")
print("Edge : Weight\n")
selected_node = [0, 0, 0, 0, 0, 0, 0, 0]
no_edge = 0
selected_node[0] = True

while (no_edge < N - 1):

    maximum = MIN

    a = 0
    b = 0
    for m in range(N):
        if selected_node[m]:
            for n in range(N):
                if ((not selected_node[n]) and G[m][n]):
                    # not in selected and there is an edge
                    if maximum < G[m][n]:
                        maximum = G[m][n]
                        a = m
                        b = n
    print(str(a) + "-" + str(b) + ":" + str(G[a][b]))
    selected_node[b] = True
    no_edge += 1