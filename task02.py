students = [
    ("Ali", ["Fizika", "Matematika"]),
    ("Laylo", ["Ingliz tili"]),
    ("Jasur", ["Matematika", "Informatika"])
]

soni = 0
for ism, fanlar in students:
    if "Matematika" in fanlar:
        soni += 1

print(f"{soni} talaba Matematika fanini tanlagan.")