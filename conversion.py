def dollars2cents(dollars):
    cents = dollars * 100
    return cents

def gallons2liters(gallons):
    liters = gallons * 3.78
    return liters

def hours2minutes(hours):
    minutes = hours * 60
    return minutes

# comment
def feet2inches(feet):
	inches = feet * 12
	return inches

#Chia added something here

inches = feet2inches(10)
print(inches)

cents = dollars2cents(5)
print('{} dollars are {} cents'.format(5, cents))
