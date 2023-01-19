def collatz(num):
    while num != 1:
        if num % 2 == 0:
            num = num //2
            print(num)
        else:
            num = 3 * num + 1
            print(num)
try :
    num = int(input('Enter a number : '))
    collatz(num)
except ValueError:
    print('Cant enter a string value')