#This is the third and final script that should be run for this project
in_file = open('3-narrowed_list.txt', 'r')
text = in_file.read()
in_file.close()
#This is a function that will remove duplicates from the list that is created
def remove_duplicates(names):
    output = []
    seen = set()
    for name in names:

        if name not in seen:
            output.append(name)
            seen.add(name)
    return output


#This section is turning the string into a list and removing the empty string
#Then it applies the function so that all duplicates are removed
#I added in the sorted to the list so that they appear alphabetically
authors_list = text.split("\n")
authors_list.remove('')
nodup_list = remove_duplicates(authors_list)
print(sorted(nodup_list))

#This does put a list into keys of a dictionary
#this part is for grammar rating
grammar_dict = {}

committee_num = eval(input("How many committee members are there?: "))
print("First we will rate the authors on grammar.")
for v in nodup_list:
    print("Author: " + v)
    authors_scores = []
    for score in range(committee_num):

        score = eval(input("On a scale of 1 to 10 with 10 being the highest, how would you rate this author on grammar?: "))
        authors_scores.append(score)
        grammar_dict[v] = authors_scores
print(grammar_dict)

#use this to add the values in the list and print a new dictionary that has the key and its one acumulated value

ranked_dict = {}
for key in grammar_dict:
    ranked_dict[key] = sum(grammar_dict[key])
print(ranked_dict)

print(max(ranked_dict.keys(), key=(lambda k: ranked_dict[k])) + " has the highest grammar score of the list." )

#This creates a dictionary for the ranking the authors on prose
print("Next, we will rate the authors on prose.")
prose_dict = {}


for i in nodup_list:
    print("Author: " + i)
    author_prose_scores = []
    for prose_score in range(committee_num):

        prose_score = eval(input("On a scale of 1 to 10 with 10 being the highest, how would you rate this author on prose?: "))
        author_prose_scores.append(prose_score)
        prose_dict[i] = author_prose_scores
print(prose_dict)

#use this to add the values in the list and print a new dictionary that has the key and its one acumulated value

ranked_prose_dict = {}
for key in prose_dict:
    ranked_prose_dict[key] = sum(prose_dict[key])
print(ranked_prose_dict)

print(max(ranked_prose_dict.keys(), key=(lambda k: ranked_prose_dict[k])) + " has the highest prose score of the list." )

#this combines the two dictionaries to get the combined scores
from collections import Counter
first_dict = Counter(ranked_dict)
second_dict = Counter(ranked_prose_dict)
acum_rank = (first_dict + second_dict)
print("These are the combined scores of the author rankings on grammar and prose.")
print(acum_rank)
print(max(acum_rank.keys(), key=(lambda k: acum_rank[k])) + " has the highest total score of the list and recieves the award." )
