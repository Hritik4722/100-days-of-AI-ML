import os
print("Welcome to TODO list\n")


def num_task_get():
    with open("num_task.txt", "r") as f:
        line = f.read()
        if not line:
            with open("num_task.txt", "w") as f:
                f.write("1")
            return 1
        else:
            return line

    
def num_task_add():
    getnumber = num_task_get()
    number = str(int(getnumber)+1)
    with open("num_task.txt", "w") as f:
        f.write(number)
            
        
def num_task_subtract():
    getnumber = num_task_get()
    number = str(int(getnumber)-1)
    with open("num_task.txt", "w") as f:
        f.write(number)
    
def add_task():
    task = input("Enter the task\n")
    try:
        with open("task.txt", "a") as f:
            f.write("--> "+task+"---Pending\n")
        num_task_add()
    except Exception as e:
        print(f"error occurred {e}")
    print("Task Added successfully ✓✓\n")


def view_task():
    try:
        with open("task.txt", "r") as f:
            while True:
                line = f.readline()
                if line == "":
                    break
                print(line.strip())
    except Exception as e:
        print(f"error occurred {e}")


def Completed(line):
    numOfLine = int(num_task_get()) 
    linetocomplete = None
    num = 1
    tempfile = open("tempfile.txt","a")
    with open("task.txt", "r") as f:     
        while num  != numOfLine:
            if num == line:
                linetocomplete = f.readline()
            else:
                tempfile.write(f.readline())
            num = num + 1

    editline = linetocomplete[0:-8]
    newline = editline + "Completed"
    tempfile.write(newline+"\n")
    tempfile.close()
    os.remove("task.txt")
    os.rename("tempfile.txt","task.txt")

   

filecreation = open("num_task.txt" ,"a")
filecreation.close()
while True:
    print('''1) add task\n2) View Task\n3) mark complete\n4) Exit  ''')
    userInput = int(input("Enter number from options\n"))
    match userInput:
        case 1:
            add_task()

        case 2:
            view_task()

        case 3:
            view_task()
            inp = int(input("enter the task number to be mark as completed\n"))
            Completed(inp)
        case 4:
            break

        case _:
            print("input wrong\n")
    

            