#collatz sequence

def collatz(number):
    if number % 2 == 0:
        return number // 2
    elif number % 2 != 0:
        return number * 3 + 1
    else:
        print('something went wrong')
        return None
print('pick a number: ')
try:
    number = int(input())
    print('collatz sequence')
    print(number)
    while number != 1:
        number = collatz(number)
        print(number)

except ValueError:
    print('Error: pick another number')

