# Corey Gassaway
# CIS 261
# Course Project

def GetEmpName():
    empname = input("Enter employee name: ")
    return empname
#write the GetHoursWorked function
def GetHoursWorked():
    hours = float(input('Enter amount of hours worked:  '))
    return hours
#write the GetHourlyRate function
def GetHourlyRate():
    hourlyrate = float(input ("Enter hourly rate: "))
    return hourlyrate
#write the GetTaxRate function
def GetTaxRate():
    taxrate = float(input ("Enter tax rate: "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate 
    incometax = grosspay * taxrate 
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}", f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}", f"{incometax:,.2f}", f"{netpay:,.2f}")

def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    #write the code to print TotHours, TotGrossPay,TotTax, and the TotNetPay with 2 decimal places
    print(f'Total Hours Worked: {EmpTotals["TotHrs"]:,.2f}')
    print(f'Total Gross Pay: {EmpTotals["TotGrossPay"]:,.2f}')
    print(f'Total Income Tax:  {EmpTotals["TotTax"]:,.2f}')
    print(f'Total Net Pay: {EmpTotals["TotNetPay"]:,.2f}')

if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break
        #write the code to assign to hours the return value from GetHoursWorked
        hours = GetHoursWorked()
        #write the code to assign hourlyrate the return value from GetHourlyRate
        hourlyrate = GetHourlyRate()
        #write the code to assign to taxrate the return value from GetTaxRate
        taxrate = GetTaxRate()
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        #write the code to increment the other total variables with the appropriate values
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay


    PrintTotals (TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay)