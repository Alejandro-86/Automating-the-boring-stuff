def collatz(number):
    result = 0
    if number%2 == 0:
        result = number/2
    else:
        result = 3*number +1
    return int(result)


while True:
    try:
        n = input("give me a number: ")
        n = int(n)
        while n != 1:
            n = collatz(n)
            print(n)
        break
    except:
        print("Thats not an integer")