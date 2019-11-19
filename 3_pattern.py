#pattern program

def pattern(n):
    for i in range(1, n+1):
        for j in range(1, i+1):
            if i==j:
                print(3*i, end=" ")
            else:
                print('_', end=" ")
        print('\n')

n = int(input('enter the value of n: '))
pattern(n)

