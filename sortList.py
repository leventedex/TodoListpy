waiting_list = ["sen", "ben", "ken", "zen", "pen"]
waiting_list.sort()
for i , name in enumerate(waiting_list):
    prtline = f"{i +1}. {name.capitalize()}"
    print(prtline)
# Sort the list in reverse order
print("Sorted in reverse order")
waiting_list.sort(reverse=True)
for i , name in enumerate(waiting_list):
    prtline = f"{i +1}. {name.capitalize()}"
    print(prtline)