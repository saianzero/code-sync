"""
GENERATOR
A function that behaves like an iterator (can be used in a for loop)
Pauses a function, returns a value, then resumes
Uses "yield" instead of "return"
"""

# ---------- EXAMPLE 1 ----------

def count_to(n):
    count = 1
    # numbers = []
    while count <= n:
        # numbers.append(count)
        yield count  # Pause here and return the current value
        count += 1
    # return numbers


n = int(input("Enter a number to count up to: "))

for c in count_to(n):
   print(c)

# ---------- EXAMPLE 2 ----------

def read_file(file_path):
   with open(file_path) as file:
       for line in file:
           yield line.strip()

filepath = "/Users/ankith/Documents/text.txt" #some random text file

for line in read_file(filepath):
   print(line)


"""
A generator is itself an iterator.
Generators provide lazy evaluation, so values are produced on demand rather than all being materialized in memory at once. 
This can significantly reduce memory usage for large datasets or stream.
"""