#Quick program with a function to check if it is an integer or not

def is_int(num):
    if num%1 == 0:
        return True
    else:
        return False

'''Numbers to round'''
numbers = [1.0, 0.5, 0.3333333333333]

for number in numbers:
    if is_int(number) == False:
        print(round(number, 1))
    else:
        print(int(number))