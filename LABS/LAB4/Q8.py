class Account:
    def __init__(self, acc_no, balance, code):
        self.__acc_no = acc_no
        self.__balance = balance
        self.__code = code

    def show_details(self):
        print(f"Account Number: {self.__acc_no}")
        print(f"Balance: {self.__balance}")
        print(f"Security Code: {self.__code}")

new_account = Account("109922", 10000, "LM10")
new_account.show_details()
