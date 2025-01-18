
# sequences.py

def calculate_s_n(n): #Define a function named calculate_s_n with a parameter n
    #initialize variables
    a = 1 #initialize the first sequence value a_0 = 1
    s_n = a #start with a_0，Initialize the cumulative sum s_0 = a_0

    for _ in range (1, n+1): #interate a sequence  of numbers from 1(inclusive) to n+1(exclusive)
        a = 2 * a + 1 
        s_n = s_n + a 

    return s_n

n = int(input("Enter value of n: ")) #Get user input
s_n = calculate_s_n(n)  #call the function
print("s_n =" , s_n) 

