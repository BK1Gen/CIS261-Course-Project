# Corey Gassaway
# CIS 261
# Course Project

def GetEmpName():
    empname = input("Enter employee name (END to terminate): ")
    return empname

def GetDatesWorked():
    #write the code to input fromdate and todate and return the values from the function.
    #Prompt the user for the dates in the following format: mm/dd/yyyy.
    #no validations are needed for this input, we wukk assume all dates are entered correctly.
    fromdate = input("Enter Start Date (mm/dd/yyyy: ")
    todate = input("Enter End Date (mm/dd/yyyy: ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours

def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate

def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate 
    incometax = grosspay * taxrate 
    netpay = grosspay - incometax
    return grosspay, incometax, netpay
#def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
#    print(empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    #create a for loop to read through EmpDetailList and assign values in list to variables.
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        #assign values to todate, empname, hours, hourlyrate, and taxrate
        todate = EmpList[1]
        empname = EmpList[2]
        hours = float(EmpList[3])
        hourlyrate  = float(EmpList[4])
        taxrate = float(EmpList[5])

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}" )
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay
        #assign totals to dictionary
        EmpTotals["TotEmp"] = TotEmployees
        #assign TotHours, TotGrossPay, TotTax, and TotNetPay to corresponding dictionary item
        EmpTotals["TotHrs"] = TotHours
        EmpTotals["TotGrossPay"] = TotGrossPay
        EmpTotals["TotTax"] = TotTax
        EmpTotals["TotNetPay"] = TotNetPay


#def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):
#    print()
#    print(f"Total Number Of Employees: {TotEmployees}")
#    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
#    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
#    print(f'Total Income Tax:  {EmpTotals["TotTax"]:,.2f}')
#    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')

def PrintTotals(EmpTotals):
    print()
    #use dictionary to print totals
    print(f'Total number of Employees: {EmpTotals["TotEmp"]}')
    #Print TotalHrs, TotGrossPay, TotTax, and TotNetPay from dictionary
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]}')
    print(f'Total Income Tax:  {EmpTotals["TotTax"]}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]}')


if __name__ == "__main__":
    #TotEmployees = 0
    #TotHours = 0.00
    #TotGrossPay = 0.00
    #TotTax = 0.00
    #TotNetPay = 0.00
    
    #create empty list and dictionary
    EmpDetailList = []
    EmpTotals = {}
    
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        fromdate, todate = GetDatesWorked()
        hours = GetHoursWorked()        
        hourlyrate = GetHourlyRate()        
        taxrate = GetTaxRate()        
        #grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        #printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        
        #add fromdate, todate, empname, hours, hourlyrate, and taxrate to list EmpDetail
        EmpDetail = fromdate + "|" + todate  + "|" + empname  + "|" + str(hours)  + "|" + str(hourlyrate)  + "|" + str(taxrate) + "\n"
        #add list EmpDetail to EmpDetailList
        EmpDetailList.append(EmpDetail)  
                
        #TotEmployees += 1
        #TotHours += hours
        #TotGrossPay += grosspay
        #TotTax += incometax
        #TotNetPay += netpay
    printinfo(EmpDetailList)
    PrintTotals (EmpTotals)