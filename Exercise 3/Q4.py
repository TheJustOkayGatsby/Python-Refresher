#Write a program to input a salary from the user and determine how much tax
#someone should pay according to the following rules:
#People pay no tax if they earn up to €10,000. They pay tax at the rate of 20% on the
#amount they earn over €10,000 but up to €50,000. They pay tax at 40% on any money
#they earn over €50,000. 
income = int(input("please enter salary"))
tax = float()
if income < 10000:
  print("You pay no tax")
elif income >= 10000 and income <= 50000:
  income = income-10000
  tax = .2
  taxcost1 = tax * income
  print("your bracket is at highest 20 percent tax, which is €", taxcost1)
elif income > 50000:
  tax = .4
  income = income - 50000
  taxunder50 = 8000
  taxcost2 = tax * income + taxunder50
  print("your bracket is at highest 40 percent tax, which is €", taxcost2)
