with open("./Input/Letters/starting_letter.txt",mode="r") as letter:
    starting_letter=letter.read()

with open("./Input/Names/invited_names.txt") as name:
    for i in name:
        i=i.strip("\n")
        print(i)
        with open(f"./Output/Letter_for_{i}.txt",mode="w") as out:
            updated_letter=starting_letter.replace("[name]",i)
            out.write(f"{updated_letter}")


