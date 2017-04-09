T = int(input())

for i in range(0, T):

    # Variables
    style = 0
    models = 0

    # Input
    line = input().split()
    N = int(line[0])
    matrix = [['.' for x in range(N)] for y in range(N)]
    M = int(line[1])

    # Read models
    for j in range(0, M):
        line = input().split()

        model = line[0]
        if (model == '+' or model == 'x'):
            styles += 1
        if (model == 'o'):
            styles += 2

        X = (int(line[1]) - 1)
        Y = (int(line[2]) - 1)
        matrix[X][Y] = model
