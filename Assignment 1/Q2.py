rate=20/100
std_ddc=10000
dpd=int(input("Enter the number of dependents : "))
Gross_income=int(input("Enter the gross income : "))
tax_inc=Gross_income-std_ddc-(dpd*3000)

Tax=tax_inc*rate

print("\nThe tax rate is 20%")

print("\nThe taxable income is : %d \nThe tax is : %d " % (tax_inc,Tax))
