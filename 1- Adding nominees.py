#This is the first python script that should be run
#This script reads in a starting list of nominees
in_file = open('1-Start_authors_string.txt', 'r')
text = in_file.read()
in_file.close()

#this is writing the starting list into a new list
#This is also the outfile for nominees added to the list
out_file = open('2-appended_authors_string.txt', 'a')
out_file.write(text)

#The loop will allow the user to enter in all of the new nominees all at once
#the if, elif and else statements will check the starting list to see if the author is already in the list or not

entries = eval(input("Enter the number of nominees you need to add to the list.: "))
for nominee in range(entries):

    nominee = eval(input("Enter the name of your nominee for best author in the format of 'LastName, FirstName': "))
    if nominee in text:
        print("Your nominee has already been nominated for best author")

    elif nominee not in text:
        out_file.write('\n' + nominee)
        print("Thank you. Your nominated author has been added to the list of nominees for 'Best Author'")
    else:
        print("This shouldn't execute")

print("Thank you. All of your nominees have been entered")
#This print statement is only there to let the user know that they are done.



out_file.close()
