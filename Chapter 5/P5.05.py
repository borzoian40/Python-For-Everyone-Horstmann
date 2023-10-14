"""
• P5.05 Write a function
def repeat(string, n, delim)
that returns the string string repeated n times, separated by the string delim. For
example, repeat("ho", 3, ", ") returns "ho, ho, ho".
"""
def repeat(string, n, delim):
    if n <= 0:
        return ""  # If n is non-positive, return an empty string
    repeated_string = (string + delim) * (n - 1) + string
    return repeated_string

# Example usage:
input_string = "ho"
repetitions = 3
delimiter = ", "
result = repeat(input_string, repetitions, delimiter)
print(result)

