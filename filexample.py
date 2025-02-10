contents = ["Buy Groceries", 
            "Clean House", 
            "Pay Bills"]

filenames = ["item0.txt", "item1.txt", "item2.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)


stringsplit = "This is a quite long string " \
            "splitted into" \
            "multiple lines"
print(stringsplit)