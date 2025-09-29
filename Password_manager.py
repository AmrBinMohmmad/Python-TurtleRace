import cryptography.ferent as fernet
master_pwd = input("Enter your your master password ")

def view():
    with open('passwords.txt' , 'r') as f:
      for line in f.readlines():
          data = line.rstrip()
          user , passw = data.split("|")
          print("User= ",user, "| password:" ,passw)
          


def add():
    name = input("Account= ")
    pwd = input("Password= ")
    
    with open('passwords.txt' , 'a') as f:
        f.write(name +"|"+ pwd +"\n")

while True:
    mode = input(
       "Chose add or view or q to quit ").lower().strip()
    if mode == "q":
       break

    if mode == "add":
        add()
    elif mode == "view":
        view()
    else: 
     print("invaild input")    
     continue