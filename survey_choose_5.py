#this file takes the list where people added their nominees and asks them to help narrow
#the list down by choosing their top five

in_file = open('appended_authors_string.txt', 'r')
text = in_file.read()
in_file.close()
print(text)

list_names = []
for selection in range(5):
    selection = eval(input("Give me the name of a nominee to move to the next round (follow the same formating as in the list):"))
    list_names.append(selection)
print("thank you, you have selected all five of your nominees")
print(list_names)
