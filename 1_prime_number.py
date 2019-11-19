#python program to to print all prime numbers
n = int(input("enter any number n: "))
def prime_nos(n):
    prime_list = [1, 2]
    for a in range(3, n+1):
        for b in range(2, int(n+1/2)):
            if a%b == 0 and a!=b:
                break
        else:
         prime_list.append(a)
    return prime_list
print(prime_nos(n))
