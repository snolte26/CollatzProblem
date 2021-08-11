def main():
    initialNum = 1
    while True:
        num = initialNum
        steps = 0
        while True:
            if num == 1:
                print(str(initialNum) + " reached the 4-2-1 loop and took " + str(steps) + " steps")
                initialNum += 1
                break
            elif (num % 2) == 0:
                num //= 2
                steps += 1
            else:
                num = (3 * num) + 1
                steps += 1


main()
