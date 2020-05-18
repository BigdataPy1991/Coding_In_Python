#Password Generator

'''This is a code to generate Passwords given the length of the password.
This code ensures the password has one capital letter,one special character,one number'''

import random
def pass_gen(length):
    pas_values = "abcdefghijklmnopqrstuvwxyz"
    cap_values="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    s={'~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/'}
    nums="1234567890"
    new_pas=""
    res="".join(random.sample(cap_values,1))+"".join(random.sample(pas_values,(length-3)))+"".join(random.sample(s,1))+"".join(random.sample(nums,1))
    return res        
pass_gen(8) 


#Sample passwords generated using the code
Rqczjr|6
Oztdyl>9
Opglbn!9
Eanbtg#1
Mbghzp?5
