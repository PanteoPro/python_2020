


def draw_random():
    turtle.color("red")
    for i in range(1000):
        if randint(1,2) == 1:
            turtle.left(randint(1,180))
        else:
            turtle.right(randint(1,180))
        turtle.forward(randint(1,60))


string = "1 2 3 4 5"
A = list(map(int, string.split()))
print(A)
print('_'.join(map(str, A)))


# Files

output_ = open("./lectures/03_lab_file.txt", "w")
input_ = open("./lectures/02_lab.py", "r")

print(input_.readline()) # Reads one line while not meet simbol \n
list_lines = input_.readlines() # Create List with count elements by count lines in file
print(list_lines)

input_.close()
input_ = open("./lectures/02_lab.py", "r")
print(input_.read(10)) # Read 10 bytes
print(input_.read()) # Read all file


print(1,2,3,4,file=output_)

output_.close()