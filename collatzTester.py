def main(number):
    # initialNum = 295147905179352825856
    num = number
    steps = 0
    while True:
        if num == 1:
            print(str(number) + " reached the 4-2-1 loop and took " + str(steps) + " steps")
            break
        elif num % 2 == 0:
            num //= 2
            print(num)
            steps += 1
        else:
            num = (3 * num) + 1
            print(num)
            steps += 1


while True:
    print("0 to quit")
    number = int(input("Input number to test: "))
    if number == 0:
        break
    else:
        main(number)
