
def spam():
    global eggs
    eggs = "spam"

eggs = "global"
spam()
print(eggs)

#the eggs = "spam" is set globally and no local statement is made

