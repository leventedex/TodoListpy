# Change . to - in each item of the list
filenames = ["1.Raw Data.txt", "2.Cleaned Data.txt", "3.Final Data.txt"]
print(filenames)
for filename in filenames:
    ind = filenames.index(filename)
    filename = filename.replace(".", "-", 1)
    filenames[ind] = filename
print(filenames)
# Lists are mutable but tuples are immutable
filenames_tuple = ("1.Raw Data.txt", "2.Cleaned Data.txt", "3.Final Data.txt")
for filename in filenames_tuple:
    ind = filenames_tuple.index(filename)
    filename = filename.replace(".", "-", 1)
    filenames_tuple[ind] = filename
print(filenames_tuple)