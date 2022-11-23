"""
P3.12 Write a program that translates a letter grade into a number grade. Letter grades are 
A, B, C, D, and F, possibly followed by + or –. Their numeric values are 4, 3, 2, 1, and 
0. There is no F+ or F–. A + increases the numeric value by 0.3, a – decreases it by 0.3. 
However, an A+ has value 4.0. 
Enter a letter grade: B-
The numeric value is 2.7
"""
def main(grade):
    score = 0
    if grade == "A+":
        score = 4.3
    elif grade == "A":
        score = 4.0
    elif grade == "A-":
        score = 3.7
    elif grade == "B+":
        score = 3.3
    elif grade == "B":
        score = 3.0
    elif grade == "B-":
        score = 2.7
    elif grade == "C+":
        score = 2.3
    elif grade == "C":
        score = 2.0
    elif grade == "C-":
        score = 1.7
    elif grade == "D+":
        score = 1.3
    elif grade == "D":
        score = 1.0
    elif grade == "D-":
        score = 0.7
    else:
        print("Unfortunately, you have to redo the test.")
    return score


if __name__ == "__main__":
    result = (input("Please enter your grade: "))
    print(f"The numeric value is: {main(result)}")
    
    
#### Second Approach ####

grade = input("Please enter your grade: ")
grade = grade.upper()

if grade[0] == "A":
    score = 4.0
elif grade[0] == "B":
    score = 3.0
elif grade[0] == "C":
    score = 2.0
elif grade[0] == "D":
    score = 1.0
else:
    score = 0.0


if len(grade) > 1 and grade[0] != "F":
    if grade[1] == "+":
        score += 0.3
    elif grade[1] == "-":
        score -= 0.3
else:
    print("Unfortunately, you have to redo the test.")

#Final score
print(f"The numeric value of your grade is: {score}")
