# 1. Using a Variable
message = "Hi, this is my second program!"
print(f"[Variable Method] {message}")

# 2. Using a Function
def say_hi(name: str = "User") -> str:
    greeting = f"Hi {name}, this is my second program!"
    return greeting

print(f"[Function Method] {say_hi()}")

# 3. Using Object-Oriented Programming (OOP)
class Greeter:
    def __init__(self, program_number: str):
        self.program_number = program_number

    def display_message(self) -> None:
        print(f"[OOP Method] Hi! This is my {self.program_number} program using OOP.")

my_greeter = Greeter("second")
my_greeter.display_message()

# 4. Using File I/O (Writing and then Reading)
file_name = "greeting.txt"

# Writing to a file
with open(file_name, "w") as file:
    file.write("Hi from a file! This is my second program.")

# Reading from the file
with open(file_name, "r") as file:
    content = file.read()
    print(f"[File I/O Method] {content}")

# 5. Using a List Comprehension / Loop
messages = ["Hi", "this", "is", "my", "second", "program"]
print(f"[List Comprehension Method] {' '.join(messages)}!")
