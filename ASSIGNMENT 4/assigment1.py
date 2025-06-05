# Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.
def read_file(sample_file):
    try:
        with open('/Users/arpitmishra/Documents/GitHub/python/ASSIGNMENT 4/sample.txt', 'r') as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{sample_file}' does not exist.")
if __name__ == "__main__":
    read_file('sample.txt')