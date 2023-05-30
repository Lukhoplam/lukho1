#=====importing libraries===========
'''Good day Sashlin Moonsamy . im failing to understand your review on Generate reports
The PDF literally says 'for each user also describe : THE TOTAL NUMBER OF TASKS ASSIGNED 
TO THAT USER . meaning if the logs in as 'lukho' , its only going to display lukohs number of tasks
in user_overview , please tell me if im incorrect , shkran lak .'''





'''This is the section where you will import libraries'''
import datetime
from datetime import datetime# for  current date options

username=[]  #username ADMIN is stored here from the user.txt 
password=[]  #password ADM1N is stored here from the user.txt 
file=open("user.txt","r")
for lines in file.readlines():
    #stripped the lines to remove the spaces from the begginning and at the end
    lines=lines.strip()
   # split the lines and automatically becomes a list which i splited the ","
    lines=lines.split(", ")
    # list username has the user.txt line is it
    username.append(lines[0])  
    #list password has the user.txt line is it
    password.append(lines[1]) 



# created a function that registers users 
def reg_user():
    while True:
        user_name =input("enter your username: ")
        if user_name in username:
            print("username already exist , enter a different username  !")
            user_name=input("enter username: ")
        else:
            break
    new_password =input("Enter your password: ")
    confirm =input("re-enter your password to confirm: ")
    while True:
        if new_password != confirm:
            print("passwords does not match try again?")
            new_password=input("Enter your password: ")
            confirm=input("re-enter your password to confirm: ")
                
        else:
            print("registering new user succesful...")
            with open("user.txt","a") as file:
                file.write(f"\n{user_name}, {new_password}")         
            break


# function adds a user and places it to tasks txt

def add_task():
    from datetime import date
    user=input(' what is the username of the person whom the task is assigned to?  ').lower()
    title_task=input(' what is the title of a task ?').lower()
    description=input('whats the description of the task?').lower()
    due_date=(input('whats the due date of the task (dd mm yyyy) ? '))
    today=datetime.now()# using current date 
    today=today.strftime('%d %b %Y')
    print('new user added .')
    with open('tasks.txt','a') as file:
        file.write(format(f'\n{user}, {title_task}, {description}, {due_date}, {today}, No'))
        print()


def view_all():
    file=open('tasks.txt','r') 
    for lines in  file.readlines():
        temp=lines.strip().split(', ')
        print(f'''
        task:  {temp[1]}
        assigned to:  {temp[0]}
        date assigned:  {temp[3]}
        due date:  {temp[4]}
        task completed: {temp[5]} 
        task description :  {temp[2]}
        ''')
        

        print('''------------------------------------''') 
        file.close()



def view_mine():
    file=open('tasks.txt','r')
    # list with all tasks
    allTask=[]
    for lines in file.readlines() :
        temp=lines.strip().split(', ')
        allTask.append(temp)  

    #create an empty list to store the user's task you extracted 
    user_task=[]
    for task in allTask:
        if task[0] == user_name:
            user_task.append(task)
            

    # enumerate and display the user_task        
    for i,task in enumerate(user_task):
        print(f'''
        taskNum : {i+1}
        task : {task[1]}
        assigned to : {task[0]}
        date assigned : {task[3]}
        due date :{task[4]}
        task completed : {task[5]}
        task descrption  : {task[2]}
        ''') 
        

     
    option=int(input("Enter the task number you want to edit :"))
      # this code extract the option you entered from the user_task
    task = user_task[option-1]
        # print a preview of the task you are about to edit 
    print(f'''task : {task[1]}
        assigned to : {task[0]}
        date assigned : {task[3]}
        due date :{task[4]}
        task completed : {task[5]}
        task descrption  : {task[2]}
        ''')

    print('1. Mark as complete ')
    print('2. Edit task ')
    print('Enter -1 for menu')

    choice=input('enter choice  :')
    if choice=='1':
        if task[5]=='yes':
            print(' task already completed')
        
        else :
            task[5]='yes'
    
              
    elif choice =='2':
        if task[5]=='yes':
            print('task already completed')
        else:
            print(' 1 .Re-assign to someone else')
            print('2 .change due date ')
            choose = input(' enter choice :')
            if choose =='1':
                assign = input('enter new username :')
                task[0]= assign
                print(user_task)
            elif choose=='2':
                new_date =input(' enter new date (day month year)')
                task[4]= new_date
                print(' due date updated ')
    

    with open('tasks.txt','w') as file:
        data=[]
        for task in allTask:
            content=f'{task[0]}, {task[1]}, {task[2]}, {task[3]}, {task[4]}, {task[5]}\n'
            data.append(content)
        file.writelines(data) 

    if choice =='-1':
        print(menu)
    



def generate_reports():


    # Open a new file called task_overview.txt for writing
    with open("task_overview.txt", "w") as f:
        # Count the total number of tasks in the tasks.txt file
        total_tasks = sum(1 for lines in open('tasks.txt'))
        # Count the total number of completed tasks in the tasks.txt file
        completed_tasks = sum(1 for lines in open('tasks.txt') if "yes" in lines)
     # Count the total number of uncompleted tasks in the tasks.txt file
        uncompleted_tasks = sum(1 for lines in open('tasks.txt') if ("no" in lines) or ("No" in lines))
        # calculating the percentage of tasks that are incomplete.
        percentage_incompleted_tasks= (uncompleted_tasks/total_tasks)*100
        # Count the total number of overdue tasks in the tasks.txt file

        tasks=[]
        with open('tasks.txt','r') as x:
            for line in x.readlines():
                file_content = line.strip().split(', ')
                tasks.append(file_content) 

        overdueTask=0
        for i in tasks:
            date = i[3]
            today=datetime.today()
        
            overdue_date = datetime.strptime(date,"%d %b %Y")
            if overdue_date < datetime.today():
                overdueTask+=1
       
        percentage_overdue=(overdueTask/total_tasks)*100
        
        # Write the results to the file in a user-friendly format
        f.write(f"Total number of tasks: {total_tasks}\n")
        f.write(f"Total number of completed tasks: {completed_tasks}\n")
        f.write(f"Total number of uncompleted tasks: {uncompleted_tasks}\n")
        f.write(f"Total number of overdue tasks: {overdueTask}\n")
        f.write(f'The percentage of tasks that are incomplete: {percentage_incompleted_tasks}\n')
        f.write(f'The percentage of tasks that are overdue: {percentage_overdue}')


# list with user information
    user_info=[]
    with open('user.txt','r') as file :
        for lines in file.readlines():
            file=lines.strip().split(', ')
            user_info.append(file)
        

    user_task_info =[]
    with open('tasks.txt','r') as file :
        for lines in file.readlines():
            file=lines.strip().split(', ')
            user_task_info.append(file)

            
            count = 0 
            completed = 0
            uncompleted = 0
            overdueTask = 0
        total_usertasks = sum(1 for lines in open('tasks.txt'))
        total_user = sum(1 for lines in open('user.txt'))
        tasks = [task for task in user_task_info if task[0] == user_name]
        for task in tasks:
            count += 1
            if task[5].lower() == 'no':
                completed += 1   
            elif task[5].lower() == 'yes':
                uncompleted += 1

            due_date = datetime.strptime(task[3], "%d %b %Y")
            if due_date < datetime.today():
                overdueTask += 1

            percentage_completed = (completed / (completed + uncompleted)) * 100
            percentage_uncompleted = 100 - percentage_completed

            

            with open('user_overview.txt','w') as file :
                file.write(f'total users :  {total_user}\n')
                file.write(f'total number of tasks :  {total_usertasks}\n')
                file.writelines(f"Total number of tasks assigned to the user : {count}\n")
                file.write(f"Total number of completed tasks assigned to the user: {completed}\n")
                file.write(f"Total number of uncompleted tasks assigned to the user: {uncompleted}\n")
                file.write(f"Total number of overdue tasks assigned to the user: {overdueTask}\n")
                file.write(f'The percentage of tasks that are complete assigned to the user: {percentage_completed}\n')
                file.write(f'The percentage of tasks that are uncompleted assigned to the user: {percentage_uncompleted}\n')
                
                




#import os
def display_statistics():
    with open('task_overview.txt', 'r') as task_file:
        task_data = task_file.read()
        
        # Code to display task data in a user-friendly manner goes here
        
    with open('user_overview.txt', 'r') as user_file:
        user_data = user_file.read()
        # Code to display user data in a user-friendly manner goes here

user_name=input(' what is your username ?\n')
while user_name not in username:  
    user_name=input('That is not a valid username. what is your username ?')

index=username.index(user_name)
pass_word = input("enter your password\n")

while password[index] != pass_word :
    pass_word = input('incorrect. enter a valid password : \n ')
    
              
file.close()

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input('''Select one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
gr - generate reports
ds - display statistics

e - Exit
: ''').lower()

    if menu == 'r':
        reg_user()
    elif menu == 'a':
        add_task()
    elif menu == 'va':
        view_all()
    elif menu == 'vm':
        view_mine()     
    elif menu =='gr':
        generate_reports()
    elif menu == 'ds':
        display_statistics()

    
        if user_name=='admin':
        
        # Code displays task data in a user-friendly manner 
              with open('task_overview.txt', 'r') as task_file:
                task_data = task_file.read()
                print(f'{task_data} \n \n The following is the user overview: \n')
        
        # Code  displays user data in a user-friendly manner 
              with open('user_overview.txt', 'r') as user_file:
                user_data = user_file.read()
                print(user_data)

        else:
             print('only admin have access to this information')
             print('\t')
            
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")


    


    
    