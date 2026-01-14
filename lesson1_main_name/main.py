from module import emailProcess, printMsg
emails = ['vietbac.coding@gmail.com', 'qty@yahoo.com', 'bacdev@iuh.edu.vn']

for email in emails:
    username, domain_name = emailProcess(email)
    printMsg(username, domain_name)