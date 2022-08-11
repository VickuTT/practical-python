# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0

while principal > 0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)

while i <13:
    principal = principal * (1+rate/12) - (payment+1000)
    total_paid = total_paid + payment+1000
    i+=1
while principal>0:
    principal = principal * (1 + rate / 12) - payment 
    total_paid = total_paid + payment
print('Total paid', total_paid)


#1.8
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
i=1

while i <extra_payment_start_month:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    i+=1
while extra_payment_start_month<=i <extra_payment_end_month+1:
    principal = principal * (1 + rate / 12) - payment-extra_payment
    total_paid = total_paid + payment+extra_payment
    i+=1
while principal>0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment

print('Total paid', total_paid)

#1.10
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000
i=0

while i <extra_payment_start_month:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    i+=1
    print(i,total_paid,principal)
while extra_payment_start_month<=i <extra_payment_end_month+1:
    principal = principal * (1 + rate / 12) - payment-extra_payment
    total_paid = total_paid + payment+extra_payment
    i+=1
    print(i,total_paid, principal)
while principal>0:
    principal = principal * (1+rate/12) - payment
    total_paid = total_paid + payment
    i+=1
    print(i,total_paid, principal)
   
