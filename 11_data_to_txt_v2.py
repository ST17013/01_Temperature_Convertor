import re

#data to be output
data = ["I", "love", "computers"]

has_error = True
while has_error:
    print()
    filename = input("Enter a filename: ")
    has_error = False

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue
        
        elif letter == " ":
            problem = "(no spaces allowed)"
        else:
            problem = ("(no {}'s allowed)".format(letter))
        has_error = True
    
    if filename == "":
        problem = "can't be blank"
        has_error = True
    
    if has_error == True:
        print("Invalid filename - {}".format(problem))
    
    else:
        print("You entered a valid filename.")


#add .txt suffix!
filename = filename + ".txt"

#create file to hold data 
f = open(filename, "w+")

#add new line at end of each item
for item in data:
    f.write(item + "\n")

#close file
f.close()