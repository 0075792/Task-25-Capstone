####################################################
# Third Capstone Project - Balonde's TASK MANAGER
####################################################

# Step 1 - import necessary packages
import os   # allow to interact with os
import time   # allow to make program wait/pause

# Step 2 - read in data files
#   open the 'user.txt' file
f_users = open('user.txt', 'r+')
#   open the 'tasks.txt' file
f_tasks = open('tasks.txt', 'r+')

# Step 3 - store user data using dict
user_content = f_users.read().split('\n')

users = dict()  # or could use = {}
# add users to dict
for user in user_content:
    user_info = user.split(',')

    user_name = user_info[0]
    password = user_info[1].strip()

    users[user_name] = password

# Step 4 - store tasks data
#   best seems dictionary - task number (key): task_list(value)
#   not want to use tuples
#   immutable so you could not change or edit
task_content = f_tasks.read().split('\n')
# store in list using list comprehension
tasks = [task.split(',') for task in task_content]
tasks = dict(zip(list(range(1, len(tasks)+1)), tasks))

# Step 5 - Welcome User
print("==========================================================")
print("\n\nWELCOME TO THE TASK MANAGER APP")
print("==========================================================")
print("\nYou are required to login to continue:")

# Step 6 - Check Login Details
while True:
    user_name = input("\n\nPlease enter your user name:    ").strip()
    password = input("Please enter your user password:    ").strip()

    # check if user registered
    if user_name in users.keys():
        # if registered and provide correct password - login
        if password == users[user_name]:
            print(f"\nThank you {user_name}, logging you in....... ")
            time.sleep(3)
            print("\nLogin Successful")

            break
        # registered but incorerect password - ask again to login
        else:
            print("\nYou entered the incorrect password")
            print("Please try again")
            continue
    # not registered
    elif user_name not in users.keys():
        print("\nYou are not registered on the system")
        print("Please contact an admin and ask them to register you")
        time.sleep(2)
        print("\n\nExiting Task Manager......")
        time.sleep(1)
        os._exit(0)

    # any exceptions to above
    else:
        # catch any un-forseen edge cases
        print("Error")
        print("Please try logging in again")
        continue

# Step 7 - Create Helpful Functions


def main_menu():
    print("Main Menu:")
    print("=============================================")
    print("Please select one of the following options:\n")
    print("r - register")
    print("a - add task")
    print("vm - view all my tasks")
    print("va - view all tasks")
    print("e - exit")
    print("=============================================")


def main_menu_admin():
    print("Main Menu:")
    print("=============================================")
    print("Please select one of the following options:\n")
    print("r - register")
    print("a - add task")
    print("vm - view all my tasks")
    print("va - view all tasks")
    print("ds - view statistics")
    print("e - exit")
    print("=============================================")


def reg_user():
    # print warning to admin
    print("\nWARNING!")
    print("As administrator of the database you have access to the users password.")
    print("Please do not share this information with anyone else.\n\n")
    # take username and password to register
    user_to_reg = input(
        "Please enter the user name being registered:   ").strip()
    user_pass_reg = input("Please enter the password for the user:   ").strip()

    # check if user registered
    if user_to_reg in users.keys():
        print("There is already a user registered with that username")
    else:
        print("Registering new user..............")
        users[user_to_reg] = user_pass_reg
        # users[key] = value
        f_users.write(f'\n{user_to_reg}, {user_pass_reg}')
        time.sleep(2)
        print("\nNew user registered successfully")


def add_task():
    person_responsible = input(
        "Please enter the user responsible for the task being registered ").strip()
    task_title = input("Please enter the task title ").strip()
    task_desc = input("Please enter the task description ").strip()
    task_issue = input(
        "Please enter todays date in the following format dd MMM YYYY ").strip()
    task_due = input(
        "Please enter the due date in the following format dd MMM YYYY ").strip()
    completed = "No"

    f_tasks.write(
        f"\n{person_responsible},{task_title},{task_desc},{task_issue},{task_due},{completed}")


def view_all():
    for task_info in tasks.items():
        task_num = task_info[0]
        task_deets = task_info[1]
        print("\n\n")
        print("=============================================")
        print(f"Task Number {task_num}")
        print("=============================================")
        print(f"\nAssigned User: {task_deets[0]}")
        print(f"Task Title: {task_deets[1]}")
        print(f"Task Description: {task_deets[2]}")
        print(f"Date Issued: {task_deets[3]}")
        print(f"Date Due: {task_deets[4]}")
        print(f"Complete: {task_deets[5]}")


def view_mine():
    for task_info in tasks.items():
        task_num = task_info[0]
        task_deets = task_info[1]
        # only if tasks belongs to current user then print
        if task_deets[0] == user_name:
            print("\n\n")
            print("=============================================")
            print(f"Task Number {task_num}")
            print("=============================================")
            print(f"\nAssigned User: {task_deets[0]}")
            print(f"Task Title: {task_deets[1]}")
            print(f"Task Description: {task_deets[2]}")
            print(f"Date Issued: {task_deets[3]}")
            print(f"Date Due: {task_deets[4]}")
            print(f"Complete: {task_deets[5]}")


def view_stats():
    num_tasks = len(tasks)
    num_users = len(users)
    print(f"Total users = {num_users}")
    print(f"Total tasks = {num_tasks}")

# Step 8 - Execute Main Program


# program execute this way if admin is user
if user_name == 'admin':
    while True:
        main_menu_admin()
        user_action = input("\n\nPlease enter your choice:   ").strip().lower()

        if user_action == 'r':
            reg_user()
            time.sleep(2)
            print("\nReturning to Main Menu\n")

        elif user_action == 'a':
            add_task()
            time.sleep(2)
            print("\nReturning to Main Menu\n")
        elif user_action == 'va':
            view_all()
            time.sleep(2)
            print("\nReturning to Main Menu\n")
        elif user_action == 'vm':
            view_mine()
            time.sleep(2)
            print("\nReturning to Main Menu\n")
        elif user_action == 'e':
            print("\nExiting the Program\n")
            break
        else:
            print("\n\nYou did not select a valid choice")
            print("\nReturning to Main Menu\n")

# program execute this way for all users besides admin
else:
    while True:
        main_menu()
        user_action = input("\n\nPlease enter your choice:   ").strip().lower()

        if user_action == 'r':
            print(
                "You are not an admin and therefore do not have access to this functionality")
            time.sleep(2)
            print("\nReturning to Main Menu\n")

        elif user_action == 'a':
            add_task()
            time.sleep(2)
            print("\nReturning to Main Menu\n")

        elif user_action == 'va':
            view_all()
            time.sleep(2)
            print("\nReturning to Main Menu\n")

        elif user_action == 'vm':
            view_mine()
            time.sleep(2)
            print("\nReturning to Main Menu\n")

        elif user_action == 'e':
            print("\nExiting the Program\n")
            break

        else:
            print("\n\nYou did not select a valid choice")
            print("\nReturning to Main Menu\n")

f_tasks.close()
f_users.close()
