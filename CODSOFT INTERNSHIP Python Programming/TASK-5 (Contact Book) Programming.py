import json
import os

CONTACTS_FILE = "contacts.json"

# Load contacts from file
def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, 'r') as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    print("\n📇 Add New Contact")
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("✅ Contact added successfully!")

# View all contacts
def view_contacts(contacts):
    print("\n📒 Contact List")
    if not contacts:
        print("No contacts available.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['name']} | 📞 {contact['phone']}")

# Search contact by name or phone
def search_contact(contacts):
    query = input("\n🔍 Enter name or phone number to search: ").strip().lower()
    found = False

    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\n👤 Contact Found:")
            print(f"Name: {contact['name']}")
            print(f"Phone: {contact['phone']}")
            print(f"Email: {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True

    if not found:
        print("❌ No contact found with that name or number.")

# Update contact details
def update_contact(contacts):
    name = input("\n✏️ Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave blank to keep old value.")
            new_phone = input(f"New phone ({contact['phone']}): ").strip() or contact['phone']
            new_email = input(f"New email ({contact['email']}): ").strip() or contact['email']
            new_address = input(f"New address ({contact['address']}): ").strip() or contact['address']

            contact['phone'] = new_phone
            contact['email'] = new_email
            contact['address'] = new_address
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")

# Delete a contact
def delete_contact(contacts):
    name = input("\n🗑️ Enter the name of the contact to delete: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print("🗑️ Contact deleted successfully!")
            return
    print("❌ Contact not found.")

# Main menu loop
def main():
    contacts = load_contacts()

    while True:
        print("\n📱 Contact Management System")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("💾 Contacts saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
