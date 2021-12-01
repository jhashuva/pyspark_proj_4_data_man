import data_man
count = 0
while count<3:

    choice = input("1.Display Data\n2.Show Missing Values\n3. Describe data")
    if choice == '1':
        data_man.display()
    elif choice == '2':
        data_man.is_missing()
    elif choice == '3':
        data_man.describe_data()
    else:
        count = count+1
        print("Try again with correct choice")




