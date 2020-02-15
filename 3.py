# Function of countiing a character
def countChar(input_string,c):
    n_string = len(input_string)
    count = 0
    i = 0
    while (i < n_string):
        if (string[i] == char):
            count = count + 1
            output = count
            i = i + 1
        else:
            output = count
            i = i + 1

    if (output != 0):
        print("output\t\t:",output)
    else:
        print("output\t\t: Not Found!")

# Main program
string = str(input("Type the string\t\t\t\t:"))
char = str(input("What char do you want to find?\t\t:"))
print("String\t\t:",string)
print("Char\t\t:",char)

# Using Function
countChar(string,char)
