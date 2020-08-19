# quick component to conver degrees F to C.
#Function takes in value does conversion and puts answer into a list


def to_c(from_f):
    celsius = (from_f - 32) / (9/5)
    return celsius


#Main routine
temperatures = [0, 32, 100]
converted = []

for item in temperatures:
    answer = to_c(item)
    ans_statement = "{} degrees C is {} degrees F".format(item, answer)
    converted.append(ans_statement)


print(converted)