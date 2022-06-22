spam = ['apples', 'bananas', 'tofu', 'cats']

def print_list(list):
    for item in list:
        if item != list[-1]:
            print(item + ', ', end='' )
        elif item == list[-1]:
            print('and ' + list[-1])

print_list(spam)
