PLACEHOLDER = "[name]"

with open("input/Names/invited_names.txt") as f:
    names = f.readlines()

with open("./input/Letters/starting_letter.txt") as l:
    letter_content = l.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/Ready to send/letter_for_{stripped_name}.txt", "w") \
                as complete_letter:
            complete_letter.write(new_letter)






