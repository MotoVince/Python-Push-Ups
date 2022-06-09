#So I have no clue how calling on modules work with python, but I figured I would just start playing around and see what happens. 
#This program is meant to hypothetical overdraft fees and based off of account balance and how many times overdrawn. 
#Declarations. 

balance = 0
overdrawn = 0
fee = 0
balance_prompt = "Please Enter Account Balance"
overdraft_prompt = "How Many Times has the Account been Overdrawn?"
fee_prompt = "Overdraft Fee for this Account is: "

#Main

import house_keeping

house_keeping
if balance >= 0:
    import detail
    detail
else:
    import end_of_job
    end_of_job
