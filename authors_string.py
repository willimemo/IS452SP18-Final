in_file = open('Start_authors_string.txt', 'r')
text = in_file.read()

out_file = open('appended_authors_string.txt', 'w')
out_file.write(text)


in_file.close()
out_file.close()