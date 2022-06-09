#Declarations
balance = 0
overdrawn = 0
fee = 0
balance_prompt = "Please Enter Account Balance"
overdraft_prompt = "How Many Times has the Account been Overdrawn?"
fee_prompt = "Overdraft Fee for this Account is: "


import house_keeping

house_keeping
while balance >= 0:
    import detail
    detail
else:
    import end_of_job
    end_of_job
