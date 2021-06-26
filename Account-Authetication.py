username = ["ExampleUser321"]
password = ["ExamplePass321"]

print("""
┏━━━┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓
┃┏━┓┃╋╋╋╋╋╋╋╋╋╋╋╋╋┏┛┗┓
┃┃╋┃┣━━┳━━┳━━┳┓┏┳━╋┓┏┛
┃┗━┛┃┏━┫┏━┫┏┓┃┃┃┃┏┓┫┃
┃┏━┓┃┗━┫┗━┫┗┛┃┗┛┃┃┃┃┗┓
┗┛╋┗┻━━┻━━┻━━┻━━┻┛┗┻━┛
╋╋╋╋╋╋┏┓┏┓╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋┏┓
╋╋╋╋╋┏┛┗┫┃╋╋╋╋╋╋┏┛┗┓╋╋╋╋╋┏┛┗┓
┏━━┳┓┣┓┏┫┗━┳━━┳━╋┓┏╋┳━━┳━┻┓┏╋┳━━┳━┓
┃┏┓┃┃┃┃┃┃┏┓┃┃━┫┏┓┫┃┣┫┏━┫┏┓┃┃┣┫┏┓┃┏┓┓
┃┏┓┃┗┛┃┗┫┃┃┃┃━┫┃┃┃┗┫┃┗━┫┏┓┃┗┫┃┗┛┃┃┃┃
┗┛┗┻━━┻━┻┛┗┻━━┻┛┗┻━┻┻━━┻┛┗┻━┻┻━━┻┛┗┛""")
user = input('(Y/y) to Log in, (N/n) to Sign up: ')

if user == "Y" or user == "y":
    #Login
    logUsrName = input("Username: ")
    logUsrPass = input("Password: ")

    for i in range(len(username)):
        if logUsrName == username[i] and logUsrPass == password[i]:
            print("Welcome: ",logUsrName)
            break
    else:
        print("Wrong Password")
        userLogin = input("(Y/y) to Try again| (N/n) to Sign up: ")
        if userLogin == "Y" or userLogin == "y":

            logUsrName = input("Username: ")
            logUsrPass = input("Password: ")

            for i in range(len(username)):
                if logUsrName == username[i] and logUsrPass == password[i]:
                    print("Welcome: ",logUsrName)
                    break
            else:
                print("Wrong Password")
        elif userLogin == "N" or userLogin == "n":

            #Register
            regUsrName = input("Username: ")
            regUsrPass = input("Password: ")

            #Append
            username.append(regUsrName)
            password.append(regUsrPass)

            userRegister = input("(Y/y) to Log in, (N/n) to Exit: ")
            if userRegister == "Y" or userRegister == "y":
                logUsrName = input("Username: ")
                logUsrPass = input("Password: ")

                for i in range(len(username)):
                    if logUsrName == username[i] and logUsrPass == password[i]:
                        print("Welcome: ",logUsrName)
                        break
                else:
                    print("Wrong Password")
            else:
                print("Please Comeback :<") 

elif user == "N" or user == "n":
    #Register
    regUsrName = input("Username: ")
    regUsrPass = input("Password: ")

    #Append
    username.append(regUsrName)
    password.append(regUsrPass)

    userRegister = input("(Y/y) to Log in, (N/n) to Exit: ")
    if userRegister == "Y" or userRegister == "y":
        logUsrName = input("Username: ")
        logUsrPass = input("Password: ")

        for i in range(len(username)):
            if logUsrName == username[i] and logUsrPass == password[i]:
                print("Welcome: ",logUsrName)
                break
        else:
            print("Wrong Password")
    else:
        print("Please Comeback :<")

