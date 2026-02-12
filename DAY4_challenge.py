data=[10,"Python","",25,"Loop",40]

number_list=[]
string_list=[]

num_count=0
str_count=0

for item in data:
    if type(item)==int:
        number_list=number_list+[item]
        num_count=num_count+1
    elif type(item)==str and item !="":

            string_list=string_list+[item]
            str_count=str_count+1

name="Sadana"

if len(name) % 2==0:
    
    new_numlist=[]
    new_strlist=[]
    
    for i in range(1, num_count):
        new_numlist=new_numlist + [number_list[i]]
        
    for i in range(1, str_count):
        new_strlist=new_strlist + [string_list[i]]
        
    number_list= new_numlist
    string_list= new_strlist

else:
  
    new_numlist=[]
    new_strlist=[]
    
    for i in range(0, num_count - 1):
        new_numlist=new_numlist + [number_list[i]]
        
    for i in range(0, str_count - 1):
        new_strlist=new_strlist + [string_list[i]]
        
    number_list=new_numlist
    string_list=new_strlist

print("Numbers List:", number_list)
print("Strings List:", string_list)

print("Total Numbers:", num_count)
print("Total Strings:", str_count)
