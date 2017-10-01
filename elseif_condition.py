'''
Created on Oct 15, 2016

@author: www
'''
amount=2000
#amount=100

if amount<1000:
    discount=amount*0.05
    print ("Discount",discount)
else:
    discount=amount*0.10
    print ("Discount",discount)
    
print ("Net payable:",amount-discount)


""" use of elif instead of else """
amount=2000
#amount=100
if amount<1000:
    discount=amount*0.05
    print ("Discount",discount)
elif amount<5000:
    discount=amount*0.10
    print ("Discount",discount)
else:
    discount=amount*0.15
    print ("Discount",discount)
    
print ("Net payable:",amount-discount)