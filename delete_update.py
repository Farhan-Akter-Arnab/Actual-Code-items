# This program deletes or updates a character at a specified index in a string.

# This function deletes a character at a specified index in a string.
def delete_character(input_string, index):
    if index < 1 or index > len(input_string):
        return "Index out of range."
    return input_string[:index - 1] + input_string[index:]

# This function updates a character at a specified index in a string.
def update_character(input_string, index, new_char):
    if index < 1 or index > len(input_string):
        return "Index out of range."
    return input_string[:index - 1] + new_char + input_string[index:]

# Driver code
string = str(input("Enter a string: "))
modif_index = int(input("Enter the index of the character to modify (the index of the first letter is 1): "))
modif_letter = str(input("Enter the new character: "))
# Deleting character
updated_string = delete_character(string, modif_index)
print("Updated string with deleted character:", updated_string)
# Updating character
updated_string = update_character(string, modif_index, modif_letter)
print("Updated string with modified character:", updated_string)