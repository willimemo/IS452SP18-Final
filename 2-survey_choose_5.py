#This is the second script in the project
#this file takes the list where people added their nominees and asks them to help narrow
#the list down by choosing their top five

in_file = open('2-appended_authors_string.txt', 'r')
text = in_file.read()
in_file.close()
print(text)

out_file = open('3-narrowed_list.txt', 'a')
#This writes the names into a new document as strings
for selection in range(5):

    selection = eval(input("Give me the name of a nominee to move to the next round (follow the same formating as in the list):"))
    out_file.write('\n' + selection)

print("thank you, you have selected all five of your nominees")
out_file.close()
