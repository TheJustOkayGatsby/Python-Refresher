#Write a program in Python to prompt the user to input their name, employee number, week
#ending date, hours worked, rate per hour, standard and overtime tax percentage rate. Use the
#data input to calculate gross pay, tax deductions and net pay. Output the results as a
#formatted payslip. Assume that a standard working week is 37.5 hours.

#E.g. Ask the user to enter the following data:
#Employee Name:(sample input – Mark Bate)
#Employee Number: (sample input – 123456789A)
#Week ending:(sample input - 26/01/2018)
#Number of hours worked:(sample input – 42.5)
#Hourly Rate:(sample input – 10.50)
#Overtime Rate:(time-and-a-half as 1.5)
#Standard Tax Rate:(sample input – 20)
#Overtime Tax Rate:(sample input – 50)

#Once the above data has been entered the program should display the employee’s payslip
#as per the following example:

from datetime import datetime
#Vars
EName = "Null"
ENumber = "Null"
# WkEnd = datetime()
HrWork = float()
HrPay = float()
TaxNorm = float()
TaxOT = float()

def callvars():
    print("Program will calculate gross pay, tax deductions, and net pay for the week.\nTo begin, please press enter")
    input()

    while 1 == 1:#employee name
        try:
            EName = input("Please enter NAME of employee, followed by enter: ")
            break
        except:
            print("Invalid value for NAME, please try again.")
    while 1 == 1:#employee number
        try:
            ENumber = input("Please enter employee's EMPLOYEE NUMBER, followed by enter: ")
            break
        except:
            print("Invalid value for EMPLOYEE NUMBER, please try again.")
    while 1 == 1:#date
        try:#(sample input - 26/01/2018) 
            WkEnd = datetime.strptime(input("Please enter a valid PAYROLL WEEK ENDING in format DD/MM/YYYY: "),'%d/%m/%Y')
            break
        except:
            print("Invalid date value, please try again.")
    while 1 == 1:#hrworked
        try:
            HrWork = float(input("Please input NUMBER OF HOURS WORKED, followed by enter: "))
            break
        except:
            print("Invalid numerical value, please try again.")
    while 1 == 1:#HrPay
        try:
            HrPay = float(input("Please input HOURLY WAGE, followed by enter:"))
            break
        except:
            print("Invalid value, please try again.")
    while 1 == 1:#OtPay
        try:
            OtPay = float(input("Please input OVERTIME RATE, as a multiplier, followed by enter(e.g: 1.5 for time-and-a-half):"))
            break
        except:
            print("Invalid value for OVERTIME RATE, please try again.")
    while 1 == 1:#TaxNorm
        try:
            TaxNorm = float(input("Please input REGULAR TAX RATE as a percent:"))
            TaxNorm = TaxNorm/100

            break
        except:
            print("Invalid value, please try again.")
    while 1 == 1:#ottax
        try:
            TaxOT = float(input("Please input OVERTIME TAX RATE as a percent"))
            TaxOT = TaxOT/100
            break
        except:
            print("Invalid value, please try again.")
    if HrWork >37.5:
        OtHrs = HrWork - 37.5
        NormalHrs = 37.5
    elif HrWork <= 37.5:
        OtHrs = 0
        NormalHrs = HrWork
    OtWage = OtPay*HrPay
    return WkEnd, EName, ENumber, NormalHrs , OtHrs , HrPay, OtWage, TaxNorm, TaxOT



def calcgross(hrwork, hrpay, hrot, otpay):
    reggross = hrwork * hrpay
    otgross = hrot * otpay
    tot = reggross+otgross
    return tot

def calctot(hr, pay):
    return hr * pay

def net(pay, tax):
    taxtotal = tax* pay 
    nettotal = pay - taxtotal
    return nettotal, taxtotal

def taxreduction(tax, totalearned):
    return tax*totalearned


def printslip(wk, name, empnr, normalhours , othours , payrate, otrate, taxnorm, taxot):
    regtotal = float(calctot(normalhours, payrate))
    regtax = float(taxreduction(taxnorm , regtotal))
    ottotal = float(calctot(othours, otrate))
    gross = calcgross(normalhours , payrate , othours , otrate)
    ottax = taxreduction(taxot , ottotal)
    totaltax = ottax + regtax
    net = gross - totaltax
    datetext = wk.strftime('%d/%m/%Y')


    regtotal = format(regtotal , '.2f')
    ottotal = format(ottotal , '.2f')
    regtax = format(regtax , '.2f')
    gross = format(gross , '.2f')
    ottax = format(ottax , '.2f')
    totaltax = format(totaltax , '.2f')
    net = format(net , '.2f')
    payrate = format(payrate , '.2f')    
    otrate = format(otrate , '.2f')
    
    print("\nWEEK ENDING:" , datetext)
    print("Employee: " , name)
    print("Employee Number: " , empnr)
    print("\t\t\tEarnings\t\tDeductions")
    print("\t\t\tHours   Rate     Total")
    print("Hours (normal)\t\t" , normalhours , "  " , payrate , "  " , regtotal ,
         "  Tax @ " , taxnorm*100, "%  " , regtax)

    print("Hours (overtime) \t", othours , "   " , otrate , "   " , ottotal ,
         "  Tax @  " , taxot*100, "% " , ottax)
    print("\n\t\t\tTotal pay:\t\t\t\t " , gross)
    print("\t\t\tTotal deductions:\t\t\t " , totaltax)
    print("\t\t\tNet pay:\t\t\t\t " , net)

varis = callvars()
wk = varis[0]
name= varis[1]
empnr= varis[2]
normalhours= varis[3]
othours= varis[4]
payrate= varis[5]
otrate= varis[6]
taxnorm= varis[7]
taxot= varis[8]
printslip(wk, name, empnr, normalhours , othours , payrate, otrate, taxnorm, taxot)

