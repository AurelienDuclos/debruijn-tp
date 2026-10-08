def print_even(test_list) : 
    result = []  
    for i in test_list: 
        if i % 2 == 0: 
            # we need to store all results 
            result.append(i) 
    return result 
  
# initializing list 
test_list = [1, 4, 5, 6, 7] 
  
# printing initial list 
print ("The original list is : " +  str(test_list)) 
#The original list is : [1, 4, 5, 6, 7] 
  
# printing even numbers 
print ("The even numbers in list are : ", end = " ") 
for j in print_even(test_list): 
    print (j, end = " ")