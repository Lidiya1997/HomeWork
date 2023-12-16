n = int(input())

for n in range (1, n):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBizz")
    elif n % 3 == 0:
        print ("Fizz")
    elif n % 5 == 0:
        print("Bizz") 
    else:
        print(n)

