# List of letters
letters = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'

# Key to shift the message_input
key = 26

# Asks for input and stores the data to a variable
message_input = input("Enter a message: \n")
encrypted_output = ""

# Find the length of user input
n = len(message_input)

# Converts user input then shifts it 
for i in range(n):
  character_value = message_input[i]
  char_location = letters.find(character_value)
  new_location = (char_location + key) % 52
  encrypted_output += letters[new_location]

# Prints the encrypted message_input
print("\nEncrypted message: ")
print(encrypted_output)