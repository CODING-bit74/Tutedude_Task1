ASSIGNMENT 4:
Module 5: Files, Exceptions, and Errors in Python
------------------------------------------------------------------
Code:

def read_file(sample_file):
    try:
        with open('/Users/arpitmishra/Documents/GitHub/python/ASSIGNMENT 4/sample1.txt', 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{sample_file}' does not exist.")
if __name__ == "__main__":
    read_file('sample.txt')
---------------------------------------------------------------------------------------------------
output
---------------------------------------------------------------------------------------------------

If the file does not exist:

Error: The file 'sample.txt' does not exist.

if file is exist:

Reading File Context:
Line 1: This is sample Text File
Line 2: It contains Multiple Line
-----------------------------------------------------------------------------------------------------------

Task 2: Write and Append Data to a File
 
Problem Statement: Write a Python program that:
1.   Takes user input and writes it to a file named output.txt.
2.   Appends additional data to the same file.
3.   Reads and displays the final content of the file.
------------------------------------------------------------------------------------------------------------
code:
def write_to_file(output_file, data):
    with open('/Users/arpitmishra/Documents/GitHub/python/ASSIGNMENT 4/output.txt', 'w') as file:
        file.write(data + '\n')
def append_to_file(output_file, data):
    with open('/Users/arpitmishra/Documents/GitHub/python/ASSIGNMENT 4/output.txt', 'a') as file:
        file.write(data + '\n')
def read_file(output_file):
    try:
        with open('/Users/arpitmishra/Documents/GitHub/python/ASSIGNMENT 4/output.txt', 'r') as file:
            content = file.read()
            print("Final content of the file:")
            print(content)
    except FileNotFoundError:
        print(f"Error: The file '{output_file}' does not exist.")
if __name__ == "__main__":
    output_file = 'output.txt'
    user_input = input("Enter data to write to the file: ")
    write_to_file(output_file, user_input)
    additional_data = input("Enter additional data to append to the file: ")
    append_to_file(output_file, additional_data)
    read_file(output_file)
------------------------------------------------------------------------------------------------------------
output:

Enter data to write to the file: Python 
Enter additional data to append to the file: good
Final content of the file:
Python 
good
