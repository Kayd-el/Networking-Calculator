import subprocess
exit_selected = 0

while exit_selected != 4:
    print("Which calculator would you like to use?\n")
    print("#1 prefix -> network/wildcard mask\n")
    print("#2 network/wildcard mask -> prefix\n")
    print("#3 Subnet calculator\n")
    print("#4 exit\n")
    option = input("Select a number: ")

    if option == "1":
        subprocess.run(["Python", "Prefix-Subnet.py"])

    if option == "2":
        subprocess.run(["Python", "Subnet-Prefix.py"])

    if option == "3":
        subprocess.run(["Python", "Subnet-Calculator.py"])

    if option == "4":
        exit_selected
        print("Terminating application")
        break
