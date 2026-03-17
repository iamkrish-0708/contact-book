import csv
from datetime import datetime
FILENAME="contacts.csv"
FIELDNAME=["name", "phone", "date", "description"]

def load_contacts():
    try:
        with open(FILENAME,"r") as f:
            reader=csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        return []

contacts=load_contacts()

def save_contacts(contacts):
    with open(FILENAME,"w",newline="") as f:
        writer=csv.DictWriter(f,fieldnames=FIELDNAME)
        writer.writeheader()
        writer.writerows(contacts)

def add_contacts(contacts):
    name=input("Enter name of contact: ").strip()
    if not name:
        print("❌ Name cannot be empty!")
        return      
   
    phone=input("Enter contact number: ")
    if not phone.isdigit() or len(phone)<7:
        print("❌ Enter a valid number (min 7 digits)!")
        return
    description=input("Enter description about contact: ")
    if not description:
        print("❌ Description cannot be empty!")
        return
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    contacts.append({"date":date,"name":name,"phone":phone,"description":description})
    save_contacts(contacts)
    print(f"{name} saved successfully!")

def view_contacts(contacts):
    if not contacts:
        print("❌ No contacts found!")
        return
    
    print("\nSort by:\n1. Oldest to newest\n2. Newest to oldest\n3. Alphabetical")
    sort_choice = input("Enter choice (or press Enter to skip): ").strip()
    
    if sort_choice == "1":
        contacts = sorted(contacts, key=lambda x: x['date'])
    elif sort_choice == "2":
        contacts = sorted(contacts, key=lambda x: x['date'], reverse=True)
    elif sort_choice == "3":
        contacts = sorted(contacts, key=lambda x: x['name'].lower())
    elif sort_choice == "": 
        pass
    else:
        print("⚠️ Invalid choice. Showing unsorted list.")
    
    print(f"\n{'#':<4} {'Date':<12} {'Name':<15} {'Description':<20} {'Phone':>11}")
    print("-" * 67)
    for i, con in enumerate(contacts, 1):
        display_date = datetime.strptime(con['date'], "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
        print(f"{i:<4} {display_date:<12} {con['name']:<15} {con['description']:<20} {con['phone']:>11}")

def search_contact(contacts):
    if not contacts:
        print("❌ Contact list is empty!")
        return
    search=input("Enter Contact To Search: ").strip()
    if not search:
        print("❌ Search term can't be empty!")
        return
    results=[]
    for con in contacts:
        if search.lower() in con['name'].lower():
            results.append(con)
    if not results:
        print("❌ No contacts found!")
        return
    print(f"\n{'#':<4} {'Date':<12} {'Name':<15} {'Description':<20} {'Phone':>11}")
    print("-" * 67)
    for i, con in enumerate(results, 1):
        display_date = datetime.strptime(con['date'], "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
        print(f"{i:<4} {display_date:<12} {con['name']:<15} {con['description']:<20} {con['phone']:>11}")
        
def update_contacts(contacts):
    if not contacts:
        print("❌ No contacts found to update!")
        return
    print(f"\n{'#':<4} {'Date':<12} {'Name':<15} {'Description':<20} {'Phone':>11}")
    print("-" * 67)
    for i, con in enumerate(contacts, 1):
        display_date = datetime.strptime(con['date'], "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
        print(f"{i:<4} {display_date:<12} {con['name']:<15} {con['description']:<20} {con['phone']:>11}")
    choice=input("\nEnter # No. for contact to update: ").strip()
    if not choice.isdigit():
        print("❌ Invalid input! Enter a valid # No.")
        return
    idx=int(choice)-1
    if idx<0 or idx>=len(contacts):
        print("❌ Invalid input! Enter a valid # No.")
        return
    print("Options For Updating An Contact Details:\n1.Name.\n2.Phone.\n3.Description.")
    menu_choice=input("Enter a Choice (1-3): ").strip()
    if menu_choice=="1":
        new_name=input("Enter a new name: ").strip()
        if new_name:
            contacts[idx]['name']=new_name
        else:
            print("❌ Name cannot be empty!")
            return
    elif menu_choice=="2":
        new_phone=input("Enter updated phone number: ").strip()
        if new_phone.isdigit() and len(new_phone)>=7:
            contacts[idx]['phone']=new_phone
        else:
            print("❌ Enter a valid number (min 7 digits)!")
            return
    elif menu_choice=="3":
        new_description=input("Enter New Description: ").strip()
        if new_description:
            contacts[idx]['description']=new_description
        else:
            print("❌ Description cannot be empty!")
            return
    else:
        print("❌ Enter a valid input!")
        return
    save_contacts(contacts)
    print("✅ Contact updated successfully!")

def delete_contacts(contacts):
    if not contacts:
        print("❌ There are no contacts to delete!")
        return
    print(f"\n{'#':<4} {'Date':<12} {'Name':<15} {'Description':<20} {'Phone':>11}")
    print("-" * 67)
    for i, con in enumerate(contacts, 1):
        display_date = datetime.strptime(con['date'], "%Y-%m-%d %H:%M:%S").strftime("%d-%m-%Y")
        print(f"{i:<4} {display_date:<12} {con['name']:<15} {con['description']:<20} {con['phone']:>11}")
    choice=input("\nEnter # No. for deletion of contact: ").strip()
    if not choice.isdigit():
        print("❌ Enter a valid # No. !")
        return
    idx=int(choice)-1
    if idx<0 or idx>=len(contacts):
        print("❌ Enter a valid # No. !")
        return
    del_contact=contacts.pop(idx)
    print(f"{del_contact['name']} is deleted successfully✅")
    save_contacts(contacts)
    

while True:
    print("\n----------Contact Book----------")
    print("1.Add a contact.\n2.View contacts.\n3.Search contact.\n4.Update contact.\n5.Delete contact.\n6.Exit.")
    print("--------------------------------")
    try:
        choice=int(input("Enter a choice: "))
    except ValueError:
        print("Invalid choice! Enter number between 1-6.")
        continue
    if choice==1:
        add_contacts(contacts)
    elif choice==2:
        view_contacts(contacts)
    elif choice==3:
        search_contact(contacts)
    elif choice==4:
        update_contacts(contacts)
    elif choice==5:
        delete_contacts(contacts)
    elif choice==6:
        print("Goodbye! 👋")
        break
    else:
        print("❌ Invalid choice. Enter number between 1 to 6.")
