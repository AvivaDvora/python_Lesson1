import os

print ('''\t\t\t   1. Create a new folder in the selected location . 
               2. Delete an existing folder if it is empty . 
               3. Create a new file in the folder . 
               4. Write content to a file or add content to an existing file . 
               5. Delete a file in the selected location . 
               6. List all files and directories in a given folder . 
               7. Display the full path of the current folder . 
Exit 0''')

choice = int(input())

while choice != 0:

    if choice == 1:
        print ("Enter location")
        url = input()
        os.mkdir(url)
    elif choice == 2:
        print ("Enter location")
        url = input()
        os.rmdir(url)
    elif choice == 3:
        print (" Enter a location and file name ")
        url = input()
        with open(url + ".txt", "w") as file:
            file.write("")
    elif choice == 4:
        print (" Enter a location and file name ")
        url = input()
        print (" Insert content ")
        txt = input()
        with open(url + ".txt", "a") as file:
            file.write(txt)
    elif choice == 5:
        print ("Enter location")
        url = input()
        os.remove(url)
    elif choice == 6:
        print ("Enter location")
        url = input()
        print (os.listdir(url))
    elif choice == 7:
        print (os.getcwdu())
    print ('''\t\t\t\t   1. Create a new folder in the selected location . 
                   2. Delete an existing folder if it is empty . 
                   3. Create a new file in the folder . 
                   4. Write content to a file or add content to an existing file . 
                   5. Delete a file in the selected location . 
                   6. List all files and directories in a given folder . 
                   7. Display the full path of the current folder . 
    Exit 0''')
    choice = int(input())