#In[1]
guests = open("guests.txt", "w")
initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]

for i in initial_guests:
    guests.write(i + "\n")
    
guests.close()

#In[2]
with open("guests.txt") as guests:
    for line in guests:
        print(line)

#In[3]
new_guests = ["Sam", "Danielle", "Jacob"]

with open("guests.txt", "a") as guests:
    for i in new_guests:
        guests.write(i + "\n")

guests.close()

#In[4]
with open("guests.txt") as guests:
    for line in guests:
        print(line)

#In[5]
checked_out=["Andrea", "Manuel", "Khalid"]
temp_list=[]

with open("guests.txt", "r") as guests:
    for g in guests:
        temp_list.append(g.strip())

with open("guests.txt", "w") as guests:
    for name in temp_list:
        if name not in checked_out:
            guests.write(name + "\n")

#In[6]
with open("guests.txt") as guests:
    for line in guests:
        print(line)

#In[7]
guests_to_check = ['Bob', 'Andrea']
checked_in = []

with open("guests.txt","r") as guests:
    for person in guests:
        checked_in.append(person.strip())
    for person in guests_to_check:
        if person in checked_in:
            print("{} is checked in".format(person))
        else:
            print("{} is not checked in".format(person))