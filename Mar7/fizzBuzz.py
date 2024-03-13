
def main():
    # n = int(input("\nEnter a number to be evaluated for FizzBuzz:"))
    # for i in range(1, n+1):
    #     print(i)
    myArray = []
    myInteger = int(input("\nEnter a number for FizzBuzz:"))
    for j in range(1, myInteger+1):
        if j % 3 == 0 and j % 5 == 0:
            j = "FizzBuzz"
            myArray.append(j)
        elif j % 3 == 0:
            j = "Fizz"
            myArray.append(j)
        elif j % 5 == 0:
            j = "Buzz"
            myArray.append(j)
        else:
            myArray.append(j)
    print(myArray)
main()