print('----------Contacts_App----------')

while True:
    print('''Your Options:-
    1. Add contact
    2. Update contact
    3. Display contacts
    4. Delete contact
    5. Exit''')
    op = int(input('---->'))
    
    if op == 5:
        print('Goodbye')
        break
    elif op == 1:
        contact_name = input('Enter name:-').strip()
        contact_number = int(input('Enter contact number:-'))

        with open('contact_list.txt', 'a') as file:
            file.write(f'Name:- {contact_name}    Contact_number:- {contact_number}\n')
            print(f'{contact_name} contact details add successfully!!!')
