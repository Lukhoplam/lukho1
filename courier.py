# when the user insert number , all will have a decimal because of the 'float' function
user_item=(float(input("enter the price of the item you'd like to purchase :\n "))) 
t_distance=(float(input("enter the total distance of the delivery in kms :\n")))
print()
'''whats happening from here is that i'm aaking the user which method he/she will choose and
whatever they type will be lower case because of the '.lower()' function 
and at the end it will calculate the total distance * transport '''

transport_choice=input("Are you going to using air or frieght ?\n").lower()
if transport_choice=="air":
    transport_choice=(float(0.35))

elif transport_choice=="freight":
    transport_choice=(float(0.25))
   
    

print()


# reasigning the variable name'transport_' until the end of the code.
transport_safety=input("full insurance or limited insurance ?").lower()
if transport_safety=="full insurance":
    transport_safety=(float(50.00))

elif transport_safety=="limited insurance" :
    transport_safety=(float(25.00))

print()

transport_extras=input("gift or no gift ?").lower()
if transport_extras=="gift":
    transport_extras=(float(15.00))
    
elif transport_extras=="no gift":
    transport_extras=float(0.00)

print()

transport_security=input("Do you want the delivery to be prioritized or just standard ? ").lower()
if transport_security=="prioritized":
    transport_security=(float(100.00))
    

elif transport_security=="standard":
    transport_security=(float(20.00))

print()

print(float(t_distance*transport_choice)+transport_safety+transport_extras+transport_security)





    




    







