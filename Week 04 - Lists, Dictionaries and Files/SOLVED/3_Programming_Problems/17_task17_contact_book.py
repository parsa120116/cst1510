contacts = {
    "Mom": "555-1234",
    "Dad": "555-5678",
    "Friend": "555-9012"
}

# Add a new contact
new_name = input("New contact name: ").strip()
new_number = input("New contact number: ").strip()
contacts[new_name] = new_number
print(f"{new_name} has been added.")

# Look up a contact by name
search_name = input("Whose number do you want? ").strip()
if search_name in contacts:
    print(f"{search_name}: {contacts[search_name]}")
else:
    print(f"Sorry, {search_name} is not in your contacts.")

# Print all contacts
print("All contacts:")
for name, number in contacts.items():
    print(f"{name}: {number}")
