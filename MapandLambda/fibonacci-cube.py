#You have to generate a list of the first fibonacci numbers, being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

cube = lambda x: x*x*x # complete the lambda function 

def fibonacci(n):
    n1,  n2 = 0, 1
    count = 0
    lst = list()
    if n<=0:
        return lst(n1)
    elif n==1:
        return lst(n1, n2)
    else:
        while count < n:
            lst.append(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            count += 1
    #print lst
    return lst
      


    # return a list of fibonacci number
if __name__ == '__main__':
    n = int(raw_input())
    print map(cube, fibonacci(n))