guests = ["Ali", "Ebrahim", "Farrag", "Saad", "Hagar"]

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

guests[2] = "Mohammed"

guests.insert(0, "Ahmed")
guests.insert(3, "Elgatoul")
guests.append("Malki")

print("Updated guest list:")
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")

print("Due to limited space, only two guests can be invited.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, we can’t invite you to dinner.")

for guest in guests:
    print(f"Dear {guest}, you are still invited.")

del guests[:]

print("Final guest list:", guests)
