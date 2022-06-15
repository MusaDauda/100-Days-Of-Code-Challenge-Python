students = {
    "Male":["Tom","Charlie","Harry", "Musa", "Ibrahim"],
    "Female":["Sarah","Amrah", "Zainab", "Fatima"]
}
for key in students.keys():
    for name in students[key]:
        if "i" in name.lower():
            print(name)