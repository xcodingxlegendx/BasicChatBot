def greet(bot_name, birth_year):
    print('Hello! My name is ' + bot_name + '.')
    print('I was created by xcodingxlegendx in ' + birth_year + '.')


def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, ' + name + '!')


def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is " + str(age))


def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1



    print("Let's test your general knowledge.")
    # write your code here
    def q(n):
        if n == 2:
            print("Correct answer!")
            return(1)
        else:
            print("Please try again")
            return(0)

    while True:
        x = int(input("What was Hitler's party known as? \n 1. Wakanda 2. Nazi 3. Mortiz 4. Heil Germany \n"))
        result = q(x)
        if result == 1:
            break
        else:
            continue
    print('Congratulations, have a nice day!')


def end():
    print('Completed')


greet('PyRob', '2020')  # change it as you need
remind_name()
guess_age()
count()
# ...
end()
