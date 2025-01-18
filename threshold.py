# threshold.py

def find_threshold(threshold):
    # Initialize variables
    a = 1
    s_n = a  # Inicialize cumulative sum
    n = 0    # Start from n = 0

    #Keep looping while the sum is below or equal to the threshold
    while s_n <= threshold:
        n = n + 1
        a = 2 * a + 1  
        s_n = s_n + a       # Add to cumulative sum

    return n, s_n  # Return the smallest n and cumulative sum

threshold = int(input("Enter threshold: ")) # Get user input
n, s_n = find_threshold(threshold) #call the function
print("n =", n)
print("s_n =", s_n)