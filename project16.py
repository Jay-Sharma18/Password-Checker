user_input=input("Please enter the string")
user_input_list=user_input.split(',')
alpha_lower=False
alpha_upper=False
number1 =False
symbol1=False
final_list=[]
for i in user_input_list:
    if 6<=len(i)<=12:
        for j in i:
            if j.islower():
                alpha_lower =True
            elif j in ['0','1','3','4','5','6','7','8','9'] :
                number1 =True
            elif j in ['#','@','$']:
                symbol1 =True
            elif j.isupper():
                alpha_upper= True
            else:
                pass
            
        if alpha_lower and alpha_upper:
            if number1 and symbol1:
                final_list.append(i)

        else:
            print("{} is not a valid password".format(i))
        alpha_upper=False
        alpha_lower=False
        number1=False
        symbol1=False
    else:
        print("{} is {} characters long".format(i,len(i)))
print("Valid Passwords:",final_list)
    

    
                
                
            
                
            
                
                
                    