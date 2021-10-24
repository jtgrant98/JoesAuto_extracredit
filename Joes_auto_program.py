import Joes_auto_class as xx


print('CUSTOMER DETAILS')
name = input('Enter name : ')
address = input('Enter address : ')
phone = input('Enter phone : ')
customer = xx.Customer(name, address, phone)
print()
print('CAR DETAILS')
make = input('Enter manufacturer : ')
model = input('Enter car model : ')
year = int(input('Enter year of manufacture : '))
car = xx.Car(make, model, year)
print()
print('CHARGE DETAILS')
pcharge = float(input('Enter charge amount for parts : '))
lcharge = float(input('Enter charge amount for labor : '))
charges = xx.ServiceQuote(pcharge, lcharge)
print()
print('\nCUSTOMER INFORMATION')
print(f'Name : {customer.get_name()}\n'
      f'CONTACT INFO : {customer.get_address()}  ({customer.get_phone()})')
print('\nCAR INFORMATION')
print(f'Manufacturer = {car.get_make()}\n'
      f'Model : {car.get_model()}\nYear : {car.get_year()}')
print('\nCHARGE INFORMATION')
print(f'Parts cost : {charges.get_parts_charges()}\n'
      f'Labour cost : {charges.get_labour_charges()}\n'
      f'Sales Tax : {charges.get_sales_tax()}\n'
      f'Total Charges : {charges.get_total_charges()}')
