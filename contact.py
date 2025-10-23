#List to store contacts
contacts = []

# Function to add a new contact
def add_contact():
    name = input("Enter store name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter store address: ")
    
    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    
    contacts.append(contact)
    print(f"\nContact '{name}' added successfully!\n")

# Function to view all contacts
def view_contacts():
    if not contacts:
        print("\nNo contacts found.\n")
        return
    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, start=1):
        print(f"{i}. {contact['Name']} - {contact['Phone']}")
    print()

# Function to search a contact
def search_contact():
    query = input("Enter name or phone number to search: ")
    found = False
    for contact in contacts:
        if query.lower() in contact['Name'].lower() or query in contact['Phone']:
            print("\nContact Found:")
            print(f"Name: {contact['Name']}")
            print(f"Phone: {contact['Phone']}")
            print(f"Email: {contact['Email']}")
            print(f"Address: {contact['Address']}\n")
            found = True
    if not found:
        print("\nNo contact found with that information.\n")

# Function to update a contact
def update_contact():
    name = input("Enter the name of the contact to update: ")
    for contact in contacts:
        if name.lower() == contact['Name'].lower():
            print("Enter new details (leave blank to keep current value):")
            new_name = input(f"New Name ({contact['Name']}): ") or contact['Name']
            new_phone = input(f"New Phone ({contact['Phone']}): ") or contact['Phone']
            new_email = input(f"New Email ({contact['Email']}): ") or contact['Email']
            new_address = input(f"New Address ({contact['Address']}): ") or contact['Address']
            
            contact.update({
                "Name": new_name,
                "Phone": new_phone,
                "Email": new_email,
                "Address": new_address
            })
            print(f"\nContact '{new_name}' updated successfully!\n")
            return
    print("\nContact not found.\n")

# Function to delete a contact
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    for contact in contacts:
        if name.lower() == contact['Name'].lower():
            contacts.remove(contact)
            print(f"\nContact '{name}' deleted successfully!\n")
            return
    print("\nContact not found.\n")

# Main menu
def main():
    while True:
        print("=== Contact Management System ===")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Run the program
if __name__ == "__main__":
    main()
