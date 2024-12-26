

# Using + Operator
   
str1 = "Hello "    # Initialisation of two strings 
str2 = "Python"    
     
str3 = str1 + str2     # Using + Operator, we add two strings in strings concatenation    
  
print("The new combined string is:",str3)    # Printing the new string, which is combination of str1 and str2  



# Using Join() Method
     
str1 = "Hello"    # Initialisation of two strings 
str2 = "Python"    
    
print("".join([str1, str2]))    # join() method is used to combine the strings  
str3 = " ".join([str1, str2])    
    
print("The new combined string is:",str3)    


# Using % Operator
# Initialisation of three strings      
str1 = "Hello"    
str2 = "Get Way Of"    
str3 = "India"  
# % Operator is used here to combine the string    
print("% s % s %s" % (str1, str2, str3))  

# Using format() function

# Taking user inputs of three strings      
str1 = input("Enter the value of Str1: ")   
str2 = input("Enter the value of Str2: ")  
str3 = input("Enter the value of Str3: ")  
     
print("{} {} {}".format(str1, str2, str3))     # format function is used here to concatenate the strings
 
str4 = "{} {} {}".format(str1, str2, str3)     # Store the result in new variable, str4 
 
print(str4)     # Print the combined string