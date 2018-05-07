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


print(text)
authors_list = text.split("\n")
authors_list.remove('')
print(authors_list)
nodup_list = remove_duplicates(authors_list)
print(nodup_list)

