
# Start

#=====importing libraries===========
from datetime import datetime

#====Login Section====
print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

# open the user.txt file and read the lines
user_read = open("user.txt", "r")
user_lines = user_read.readlines()

# empty lists to store the usernames and passwords
usernames = []
passwords = []

# formulate the lists of usernames and passwords
username = [line.split()[0].strip(", ") for line in user_lines]
usernames += username
password = [line.split()[1] for line in user_lines]
passwords += password

# while loop to input the correct username/s and password/s
while True:
    login = input("Enter 'username, password': ")

    if login == "":
        
        print("\nInvalid input, try again.\n")
        continue

    if len(login.split()) == 1:

        print("\nInvalid input, try again.\n")
        continue

    user_input = login.split(", ")[0]
    pass_input = login.split()[1]

    # for loop to find out which username is logging in
    for i in range(len(usernames)):
        if username[i] == user_input:
            acc_no = i
            user_pass = (f"{username[acc_no]}, {password[acc_no]}")
            break

        else:
            acc_no = 0
    
    # still checking the right username/s and pasword/s input is correct
    if login == (f"{username[acc_no]}, {password[acc_no]}"):

        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        print(f"Welcome {usernames[acc_no]}! ")
        break

    elif "," not in login:

        print("\nThe comma is missing.\n")
        continue

    elif user_input not in usernames:

        print("\nIncorrect username, try again.\n")
        continue
    
    elif username[acc_no] in login:
        
        print("\nIncorrect password, try again.\n")
        continue

    else:
        print("\nLogin information incorrect, try again.\n")
        continue

print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")


while True:
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: ''').lower()

    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

    if menu == 'r':
        pass

        # conditional to allow only 'admin' to register new users
        if user_input == "admin":

            # while loop for 'admin' specific menu
            while True:
                admin_choice = input("Enter 'users' to show the names of and how many users, 'new' to register a user or 'exit' to exit: ")

                # copying the username/s algorithm for new registered users
                # open and read data in user.txt
                user_read = open("user.txt", "r")
                users = user_read.readlines()

                # empty list for storing the username/s
                usernames = []

                # copying the username/s algorithm for new registered users and formulate the list again
                username = [line.split()[0].strip(", ") for line in users]
                usernames += username

                # display to 'admin' how many users are registered within the file
                if admin_choice == "users":
                    user_number = 0
                    for line in users:
                        user_number += 1
                    
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    print(f"There are {user_number} users registered.\n")
                    print(f"The registered users are: {usernames}")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

                    continue

                if admin_choice == "new":

                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    
                    # while loop to check if new username is free or not
                    while True:
                        new_user = input("Enter a new username: ")

                        # conditional to make sure a valid input is entered
                        if new_user == "":

                            print("\nInvalid input.\n")
                            continue

                        print("")

                        if new_user in usernames:

                            print("Username already in use, try a different username.\n")
                            continue

                        else:
                            break
                    
                    # while loop to enter the new password and confirm it
                    while True:
                        new_pass = input("Enter a password: ")

                        # conditional to make sure a valid input is entered
                        if new_pass == "":

                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                            print("Invalid input.")
                            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                            continue

                        else:
                            new_pass_confirm = input("Confirm the password: ")

                        # conditional to make sure the password/s match
                        if new_pass_confirm == new_pass:
                            # open the user.txt file and write the new username/s and password/s under the previous
                            with open("user.txt", "a") as user_write:
                                user_write.write(f"\n{new_user}, {new_pass}")
                                user_write.close()
                                break
                            
                        else:
                            print("\nThe passwords do not match, try again.\n")
                            continue

                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    print("New user added successfully. ")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    continue
                
                if admin_choice == "exit":
                    break

                else:
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    print("Invalid input, try again. ")
                    print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                    continue

        else:
            print("Access 'admin' specific. ")
            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            continue

        # close the user.txt file
        user_read.close()

        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")


    elif menu == 'a':
        pass
        
        # open the user.txt file and read the lines
        user_read = open("user.txt", "r")
        user_lines = user_read.readlines()

        # empty list to store the username/s
        usernames = []

        # repeating the username/s algorithm for any new registered users to formulate the list again
        username = [line.split()[0].strip(", ") for line in user_lines]
        usernames += username

        # open tasks.txt to add new tasks into the file
        tasks_write = open("tasks.txt", "a")
        
        # inputs for the all the variables needed for the assigned task/s
        # check to see if the user the task is being assigned to is registered inside the file
        while True:
            task_user = input("Enter the username the task is assigned to, or 'exit' to exit: ")

            if task_user == "exit":
                break

            if task_user not in usernames:

                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                print("Unknown user, try again.")
                print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                continue    

            task_title = input("Enter the title of the task: ")
            task_description = input("Enter the description of the task: ")
            # assigned date == current date
            current_date = datetime.today()
            due_date = input("Enter the due date of the task: ")
            task_completion = "No\n"

            # write the new task/s as a string into the file under the previous task/s
            tasks_write.write(str(f"{task_user}, {task_title}, {task_description}, {current_date:%d/%m/%Y}, {due_date}, {task_completion}"))

            # close the tasks.txt file
            tasks_write.close()
            user_read.close()

            print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            print("Task added successfully. ")

            break

        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")


    elif menu == 'va':
        pass
        
        # conditional to allow only 'admin' to view all tasks
        if user_input == "admin":
            # open the tasks.txt file and read the data
            tasks_read = open("tasks.txt", "r")
            tasks = tasks_read.readlines()

            # calculate how many total tasks are in the file
            number_of_lines = 0
            
            for line in tasks:
                number_of_lines += 1
            
            print(f"There are {number_of_lines} total tasks.\n")

            # to number the lines and tasks from the file
            for pos, line in enumerate(tasks, 1):
                tasks_split = line.split(", ")

                # output the task/s in the 
                output = (f"-=-=-=-=-=-=-=-=-=-[Task {pos}]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
                output += (f"Task:\t\t   {tasks_split[1]}\n")
                output += (f"Assigned to:\t   {tasks_split[0]}\n")
                output += (f"Date Assigned:\t   {tasks_split[3]}\n")
                output += (f"Due Date:\t   {tasks_split[4]}\n")
                output += (f"Task Complete?:\t   {tasks_split[5]}")
                output += (f"Task Description:  {tasks_split[2]}\n")

                print(output)

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            
            # while loop to interact with the numbered tasks
            while True:
                tasks_number = int(input("Select which task number you want to modify or enter '0' to exit: "))-1

                print("")

                if tasks_number == -1:
                    break

                if tasks_number > len(tasks) or tasks_number < -1:

                    print("Invalid input, try again. ")
                    continue
                
                # admin specific menu to modify the tasks
                while True:
                    tasks_choice = input("Enter 'date' to change the due date, 'complete' to mark as complete or 'exit' to exit: ").lower()

                    print("")

                    if tasks_choice == "date":
                        new_date = input("Enter the new due date: ")

                        print("")

                        # editing the date in the chosen task line
                        edit_date = tasks[tasks_number]
                        split_date = edit_date.split(", ")
                        split_date[-2] = new_date
                        change_date = ", ".join(split_date)

                        with open("tasks.txt", "r") as tasks_read:
                            date_lines = tasks_read.readlines()
                        date_lines[tasks_number] = change_date

                        # open and write the new date into the file
                        with open("tasks.txt", "r+") as tasks_write:
                            tasks_write.writelines(date_lines)
                            tasks_write.close()
                        tasks_read.close()

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print(f"Task {(tasks_number)+1}'s due date changed. ")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

                        continue

                    if tasks_choice == "complete":
                        # changing the completion of the chosen task
                        edit_tasks = tasks[tasks_number]
                        split_tasks = edit_tasks.split(", ")
                        split_tasks[-1] = "Yes\n"
                        complete_tasks = ", ".join(split_tasks)

                        with open("tasks.txt", "r") as tasks_read:
                            tasks_line = tasks_read.readlines()
                        tasks_line[tasks_number] = complete_tasks
                        
                        # open and write the new line into file
                        with open("tasks.txt", "r+") as tasks_write:
                            tasks_write.writelines(tasks_line)
                            tasks_write.close()
                        tasks_read.close()

                        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print(f"Task {(tasks_number)+1} has been marked as complete. ")
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

                        continue

                    if tasks_choice == "exit":
                        break
                    break                
                break

            # close the tasks.txt file
            tasks_read.close()
            
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
            print("End of tasks. ")
        
        else:
            print("Information 'admin' specific. ")

        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        

    elif menu == 'vm':
        pass
        
        # open the tasks.txt file and read the data
        task_read = open("tasks.txt", "r")
        my_task = task_read.readlines()

        # calculate the total number of personal tasks for the user
        my_number_task = 0
        for line in my_task:
            num_split_data = line.split(", ")
            num_word = line.split()
            if num_word[0].strip(", ") == user_input:
                my_number_task += 1
        
        print(f"You have {my_number_task} task/s avaliable.")

        # calculate the number to assign each task
        my_task_number = 0

        # while and for loop to output the users personal task/s 
        while True:
            for pos, line in enumerate(my_task, 1):
                split_data = line.split(", ")
                word = line.split()

                if word[0].strip(", ") == user_input:
                    my_task_number += 1
                    edit_data = line
                    my_task_split = line.split(", ")

                    output = (f"\n-=-=-=-=-=-=-=-=-=-[Task {my_task_number}]-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n")
                    output += (f"Task:\t\t   {my_task_split[1]}\n")
                    output += (f"Assigned to:\t   {my_task_split[0]}\n")
                    output += (f"Date Assigned:\t   {my_task_split[3]}\n")
                    output += (f"Due Date:\t   {my_task_split[4]}\n")
                    output += (f"Task Complete?:\t   {my_task_split[5]}")
                    output += (f"Task Description:  {my_task_split[2]}\n")
                    output += "\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n"        
                    
                    print(output)
                    # ask user how they want to interact with the task/s
                    choice = input("Enter 'next' to show next task, 'complete' to complete the task or 'exit' to exit: ").lower()

                    if choice == "next":
                        continue

                    # conditionals for the choice input
                    if choice == "complete":
                        # algorithm to replace the last word in the task ("No\n") with "Yes\n" when marked complete
                        edit_line = my_task[pos-1]
                        split_line = edit_line.split(", ")
                        split_line[-1] = "Yes\n"
                        new_line = ", ".join(split_line)

                        # open and read the tasks.txt file and implement the changed line
                        with open("tasks.txt", "r") as my_task_read:
                            task_line = my_task_read.readlines()
                        task_line[pos-1] = new_line

                        # open and write the new line into the tasks.txt file
                        with open("tasks.txt", "r+") as my_task_write:
                            my_task_write.writelines(task_line)
                            # close the read and write tasks.txt file
                            my_task_write.close()
                        my_task_read.close()
                        continue

                    if choice == "exit":
                        break

                    else:
                        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
                        print("Invalid choice, start again.")
                        break

            break
        
        # close the tasks.txt file
        task_read.close()

        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        print("End of tasks. ")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        
        
    elif menu == 'e':
        print('Goodbye!!!')
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")

        # close the user.txt file
        user_read.close()
        
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
        print("\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n")
        

# Stop
