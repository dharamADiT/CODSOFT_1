# i am creating command line To-Do-List appllication in command line as question said.

# This is my list for my all task..
To_do_list = []
print("-----------------------------------")
print('\n')

print("TO-DO-LIST APPLICATION IN COMMAND LINE")
# I am giving here multiple choice for select..
while True:
    print('''     
    Press "1" For Add New Task.
    Press "2" For view Tasks.
    Press "3" For Task as Done.
    Press "4" For Exit.
      
    ''')
    option = int(input("Choose Any Choice :-"))
# this is for Add new task in your list..
    if option == 1:
        task =input("Enter your task here:-")
        To_do_list.append(task)
        print("Your task addded Successfully in To-do-list.")
# this is for showing your all tasks...
    elif option == 2:
        print("All task in your list.")
        for index, task in enumerate(To_do_list,start=1):
            print(f"{index}. {task}")
# if client done any task then he will click this option
    elif option == 3:
        print("Task in to-do-list..")
        for index, task in enumerate(To_do_list,start=1):
            print(f"{index}. {task} ") 
        task_index = int(input("Enter the task number to mark as done:-")) - 1
        if 0 <= task_index < len(To_do_list):
            del To_do_list[task_index]
            print("Task marked as done !")

        else:
            print("Please Enter valid input here!!")

# this is exit from "To-Do-List" application...
    elif option == 4:
        print("Exiting the To-Do-List application. Goodbye!")
        break
    
# if client give any invailid choice so this massige will come...
    else:
        print("Invalid choice. Please try agian.")
