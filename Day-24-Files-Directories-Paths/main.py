temp_name = "[name]"

# Read the starting letter file
with open("./Input/Letters/starting_letter.txt", mode="r") as start_letter:
    letter = start_letter.read()
    # print(contents)

# read in the names from the names file
with open("./Input/Names/invited_names.txt", mode="r") as names:
    invited = names.readlines()

# Iterate through the names, generate and save the updated letters
for name in invited:
    updated_letter = letter.replace(temp_name, name.strip())
    with open(f"./Output/ReadyToSend/letter_for_{name.strip()}.txt", mode="w") as completed_letter:
        completed_letter.write(f"{updated_letter}")
