

# importing module calc.py
import calc


print(calc.add(10, 2))

calc.spam('gumby')



print('-------------------------------')


# print(calc.a)  # 1

# calc.a = 10   # Change attribute in module
# print(calc.a)   #10



# print(calc.a)   # Code wasn't rerun: attribute unchanged

 
print('-------------------------------')




from small import a,b  #copy out a, b into local vars a,b

print(a) #1
print(b)  #[1,2]

a = 20  #changes local a only not the module a
b[0] =15 #changes shared mutbale as list considered a ref obj

print(a)   #20     1
print(b)   #[15,2]

import small   

print(small.a)   #1
print(small.b)   #[15,2]
