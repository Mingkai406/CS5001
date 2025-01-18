# even_nicer_figures.py

def even_nicer_figures(n):
    # Print the upper part
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        stars = "*" * i
        print(spaces + stars)

    # Print the lower part
    for i in range(n - 1, 0, -1):
        spaces = " " * (n - i)
        stars = "*" * i
        print(spaces + stars)

n = int(input("Enter n: ")) # Get user input
even_nicer_figures(n) # Call the function

