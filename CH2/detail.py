#Detail Module

#Declarations:
overdrawn = 0
fee = 0
balance = 0
balance_prompt = "Please Enter Account Balance"
overdraft_prompt = "How Many Times has the Account been Overdrawn?"
fee_prompt = "Overdraft Fee for this Account is: "

#Program

print(overdraft_prompt)
overdrawn = int(input())
import house_keeping
fee = (balance * 0.01) + 5 * overdrawn

print(fee_prompt, fee)
print(balance_prompt)
balance = int(input())
