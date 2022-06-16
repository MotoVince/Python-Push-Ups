#Declarations
balance = 0
overdrawn = 0
fee = 0
balance_prompt = "Please Enter Account Balance "
overdraft_prompt = "How Many Times has the Account been Overdrawn? "
fee_prompt = "Overdraft Fee for this Account is: "

#Detail:
def overdraft_fee(overdrawn, balance):
  return (balance * 0.01) + 5 * overdrawn
  
#Housekeeping:
def housekeeping():
  print(balance_prompt)
  new_balance = int(input())
  return new_balance 

#End of job:
def end_of_job():
  print("Thank You for using this program, have a great day.")

#Main:

balance = housekeeping()
while balance > 0:
  fee = overdraft_fee(int(input(overdraft_prompt)), balance)
  print(fee_prompt, fee)
  balance = housekeeping()
else:
  end_of_job()
