def main():
    #write your code below this line
    greatest = 0
    while True:
        details = input()
        if (details != ""):
            details_split = details.split(",")
            if (int(details_split[1]) > greatest):
                greatest = int(details_split[1])
        else:
            break
    print("Age of the oldest: " + str(greatest))

if __name__ == '__main__':
    main()
