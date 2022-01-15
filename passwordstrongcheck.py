print("T&c for creating a new password ")
print("1) The password must be minimum 8 and maximum 16")
print("2) The password must have  include  least One Captial and One Small Letters ")
print(R"3) The password must  include number and special character like $,*,&,+,@,!,etc  ")
password = input(" Enter the new password fullfilling the above Condition: ")
cpass = list(password)
print(type(cpass))
big_letters= "ABCDEFGHIJKLMNPQRSTWVXYZ"
small_letters="abcdefghijklmnopqrstwvxyz"
numbers= [1,2,3,4,5,6,7,8,9,0]
special_char="!@#$%^&*()-=_+/?><"
print(special_char)
big_flag = 0
Small_flag = 0
special_flag = 0

for i in password:
    if i   in big_letters:
        print(i)
        if big_flag == 1:
            break 
        else:
            big_flag = big_flag + 1 
         

for i in password:     
    
    if i  in small_letters:
        print(i)
        if Small_flag == 1:
            break 
        else:
            Small_flag = Small_flag +1
        

for i in password:   
    if i   in special_char:
        print(i)
        if special_flag == 1:
            break 
        else:
            special_flag = special_flag + 1 
            break
        
        

if len(password) < 8 and len(password) > 16 :
    print("password doesnot match the criteria :  The password must be minimum 8 and maximum 16 ")
elif big_flag != 1  : 
    print("password doesnot match the criteria : The password must have  at least One Captial letters")
elif Small_flag != 1:
    print("password doesnot match the criteria : The password must have  at least One Small letters")
elif password in numbers:
    print("password doesnot match the criteria : The password must include Numbers ")
elif special_flag != 1 :
    print("password doesnot match the criteria : Password must include special character ")
else:
    print("Password has been Set Successfully ")