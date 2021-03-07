#In[1]:

my_list = [27, 5, 9, 6, 8]

def RemoveValue(myVal):
    my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

#In[2]

print(RemoveValue(27))

#In[3]

def RemoveValue(myVal):
    if myVal not in my_list:
        raise ValueError("Value must be in the given list")
    else:
        my_list.remove(myVal)
    return my_list

print(RemoveValue(27))

#In[4]

my_word_list = ['east', 'after', 'up', 'over', 'inside']

def OrganizeList(myList):
    myList.sort()
    return myList

print(OrganizeList(my_word_list))

#In[5]

my_new_list = [6, 3, 8, "12", 42]
print(OrganizeList(my_new_list))

#In[6]

def OrganizeList(myList):
    for item in myList:
        #if type(item) != str:
            #raise TypeError("Word list must be a list of strings")
        assert type(item) == str, "Word list must be a list of strings"
    myList.sort()
    return myList

print(OrganizeList(my_new_list))

#In[7]

import random

participants = ['Jack','Jill','Larry','Tom']

def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False
    
print(Guess(participants))

#In[8]

# Revised Guess() function
def Guess(participants):    
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
    
    try:
        test = my_participant_dict['Larry']
    except KeyError:
        return None
    
    if my_participant_dict['Larry'] == 9:
        return True
    else:
        return False

#In[9]

participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))