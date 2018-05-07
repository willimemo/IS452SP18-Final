in_file = open('narrowed_list.txt', 'r')
text = in_file.read()
in_file.close()
def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output



authors_list = text.split("\n")
authors_list.remove('')
nodup_list = remove_duplicates(authors_list)
print(nodup_list)

#This does put a list into keys
grammar_dict = {}

committee_num = eval(input("How many committee members are there?: "))
for k in nodup_list:
    print("Author: " + k)
    authors_scores = []
    for score in range(committee_num):

        score = eval(input("On a scale of 1 to 10 with 10 being the highest, how would you rate this author on grammar?: "))
        authors_scores.append(score)
        grammar_dict[k] = authors_scores
print(grammar_dict)

#use this to add the values in the list and print a new dictionary that has the key and its one acumulated value

dict2 = {}
for key in grammar_dict:
    dict2[key] = sum(grammar_dict[key])
print(dict2)
