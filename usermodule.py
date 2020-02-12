# List of characters that provide the scope for user input data
lowercase = 'abc'

# Prompts the user for input and assigns a variable to store the data
string_input = input("Enter a message")
key = int(input("Enter a Key: "))

# Prints output data
string_output = " "

# Determines the length of user input data
n = len(string_input)

# Converts user input data then shifts it 
for i in range(n):
  character = string_input[i]
  location = lowercase.find(character)
  new_location = (location + key) % 26
  string_output += lowercase(new_location)

print(string_output)

# ENHANCEMENT IDEA - "CLASSIC" MODE OPTION
# Display Caesar facts/quotes and explain cipher history
# Assign Cipher key a static value of 13 (or 3?) like the original