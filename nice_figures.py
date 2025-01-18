# nice_figures.py

def nice_figures(n):
    for i in range(1, n + 1):
        print(i * "*")  # Print i stars on the i-th line

n = int(input("Enter n: "))  # Get user input
nice_figures(n)          # call the function