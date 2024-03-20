#!/usr/bin/python3

# console.py

class Console:
    def __init__(self):
        # Your initialization logic here
        pass
    
    def cmdloop(self):
        # Your command loop implementation here
        while True:
            command = input("Enter a command: ")
            # Implement your command handling logic here

if __name__ == "__main__":
    console = Console()
    console.cmdloop()
