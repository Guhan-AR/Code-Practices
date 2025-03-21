import random

from Loan import Loan
from account import Account


class Bank:

    class Create:

        def open_account(self,branch,customer,accounts):
            if branch.Name and branch.id and branch.Branch_name and customer.Name:
                current_account = Account(random.randrange(10000, 99999), 0, input("Enter a type of account you need:"))
                account = [branch.Name,branch.id,branch.Branch_name,customer.Name,customer.Id,customer.Phone_number,customer.Address,customer.Pan_card_number,current_account.Id,current_account.Balance,current_account.Type,0,0,0,"account_active"]
                accounts.append(account)

        def open_loan(self,account_id,accounts):
            for i in range(len(accounts)):
                if accounts[i][8] == account_id:
                    # print("*"*20,"Working")
                    current_loan = Loan(random.randrange(10000, 99999), int(input("Enter the loan amount:")), input("Enter loan type:"))
                    accounts[i][11] , accounts[i][12] , accounts[i][13] = current_loan.Id , current_loan.Amount , current_loan.Type
                    accounts[i][9] += current_loan.Amount
                    break

        # def number_generator():
        #     print("3.dummy generator")

    class Read:

        def account_based_read(self,accounts):
            if accounts:
                for i in accounts:
                    print("*"*20)
                    print("Bank Name:",i[0])
                    print("Branch Id:",i[1])
                    print("Branch Name:",i[2])
                    print("Customer Name:",i[3])
                    print("Customer Id:",i[4])
                    print("Customer Phone number:",i[5])
                    print("Customer Address:",i[6])
                    print("Customer Pan card Number:",i[7])
                    print("Account Id:",i[8])
                    print("Balance:",i[9])
                    print("Account Type:",i[10])
                    print("Loan Id:",i[11])
                    print("Loan Amount:",i[12])
                    print("Loan Type:",i[13])
                    print("Account Status::",i[14])
                    print("*" * 20)
            else:
                print("No accounts to view.")

        # def loan_based_read():
        #     print("5.loan based read")

    class Update:

        def credit(self,id,amount,accounts):
            if accounts:
                for i in range(len(accounts)):
                    if accounts[i][8] == id and accounts[i][14] != "closed":
                        accounts[i][9] += amount
                        break
                    else:
                        print("account already closed.")
            else:
                print("No accounts to view.")

        def debit(self,id,amount,accounts):
            if accounts:
                for i in range(len(accounts)):
                    if accounts[i][8] == id and accounts[i][9]>amount:
                        accounts[i][9] -= amount
                        Bank.Read.account_based_read(0, accounts)
                        break
                    else:
                        print("no valid balance heree")
                        break
            else:
                print("*"*20)
                print("No accounts to view.")
                print("*" * 20)

    class Delete:
        def close_account(self,id,accounts):
            if accounts:
                for i in range(len(accounts)):
                    if accounts[i][8]==id:
                        if accounts[i][12] == 0:
                            accounts[i][9] = 0
                            accounts[i][14] = "closed"
                        else:
                            print("can't close now because of active loan")
                        break
            else:
                print("*"*20)
                print("No accounts to view.")
                print("*" * 20)


            # print("9.close account")

        def close_loan(self,id,accounts):

            if accounts:

                for i in range(len(accounts)):
                    if accounts[i][8]==id:
                        if accounts[i][12]<accounts[i][9]:
                            accounts[i][9] -= accounts[i][12]
                            accounts[i][12] = 0
                        break
            else:
                print("*"*20)
                print("No accounts to view.")
                print("*" * 20)
