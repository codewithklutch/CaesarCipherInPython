# List of characters that provide the scope for user input data
lowercase = 'abcdefghijklmnopqrstuvwxyz'

# Key for shifting the data
key = 13

# Prompts the user for input and assigns variables to store the input data
string_input = input("Enter a Message: \n")

# Determines the length of user input data
n = len(string_input)

# Prints output data
string_output = ""

# Converts user input data then shifts it 
for i in range(n):
  character = string_input[i]
  location = lowercase.find(character)
  new_location = (location + key) % 26
  string_output += lowercase[new_location]

# Prints the ciphered message
print("\nCiphered Message: ")
print(string_output)
