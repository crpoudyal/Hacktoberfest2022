#Python program with basic functions, admission, minus and times to work out and print a value. Stored as floats for dollar currency display.
#park admission price
disney_admission_price=130
#discount for student
discount_amount=30
student_admission=disney_admission_price-discount_amount
#kids discount
kids_admission=disney_admission_price/10
#tax price @10%
tax_price_student="{:.2f}".format(student_admission*.10)
tax_price_kids="{:.2f}".format(kids_admission*.10)
tax_price_full="{:.2f}".format(disney_admission_price*.10)
#convert price to string
converted_student_admission=str(student_admission)
converted_disney_admission_price=str(disney_admission_price)
converted_kids_price=str("{:.2f}".format(kids_admission))
#working out tax
tax_price_student=str(tax_price_student)
tax_price_kids=str(tax_price_kids)
tax_price_full=str(tax_price_full)
disney_castle= """
_   |~  _
[_]--'--[_]
|'|""`""|'|
| | /^\ | |
|_|_|I|_|_|
"""
#print ticket prices on 'menu'
print ('############################################################')
print("Welcome to Disney")
print (disney_castle)

print ('############################################################')
print ('The prices for admission are:')
print("Student admission price is $" + converted_student_admission + " add on tax = $" + tax_price_student )
print("Adult admission price is $" + converted_disney_admission_price + " add on tax = $" + tax_price_full )
print("Kids under 12 price is $" + converted_kids_price + " add on tax = $" + tax_price_kids)

print ('############################################################')