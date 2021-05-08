
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
placeholder = "[name]"
list = []
name_list = []
with open("./Input/Names/invited_names.txt", mode ="r") as invite_list:
    list = invite_list.readlines()
    for name in list:
        new_name = name.strip("\n")
        name_list.append(new_name)

with open("./Input/Letters/letter.txt", mode= "r") as letter:
    text = letter.read()
    for name in name_list:

       new_text = text.replace(placeholder, name)

       with open(f"./Input/ready_to_send/letter_to_{name}.docx", mode="w") as file:
           file.write(f"{new_text}")

