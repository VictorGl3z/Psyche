def countdown_to_blastoff():
    for i in range(10,0,-1):
        if i == 1:
            print(f'{i}... Blastoff!')
        else:
            print(i)
        

# Don't edit below this line


def test():
    print("Counting down to blastoff:")
    countdown_to_blastoff()
    print("=====================================")


def main():
    test()


main()
