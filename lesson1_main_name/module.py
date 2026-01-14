def emailProcess(email):
    username = email[0:email.index("@")]
    domain_name = email[email.index("@") + 1:]
    return [username, domain_name]

def printMsg(username, domain_name):
    print(f"Username is {username}\tDomain is {domain_name}")

def main():
    # vietbac@gmail.com
    email = input("Please enter your email: ")
    printMsg(email)
if __name__ == "__main__":
    main()
