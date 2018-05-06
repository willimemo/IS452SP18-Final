in_file = open('Start_authors_string.txt', 'r')
text = in_file.read()
in_file.close()

out_file = open('appended_authors_string.txt', 'a')
out_file.write(text)

nominee = eval(input("Enter the name of your nominee for best author in the format of 'LastName, FirstName': "))
if nominee in text:
    print("Your nominee has already been nominated for best author")

elif nominee not in text:
    out_file.write('\n' + nominee)
    print("Thank you. Your nominated author has been added to the list of nominees for 'Best Author'")
else:
    print("This shouldn't execute")






out_file.close()
