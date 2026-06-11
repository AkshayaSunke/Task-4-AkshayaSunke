# General Knowledge Quiz

print("Welcome to the General Knowledge Quiz!")
print("--------------------------------------")
score = 0
# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Paris.\n")

# Question 2
answer = input("2. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Mars.\n")

# Question 3
answer = input("3. What is the largest ocean on Earth? ").strip().lower()

if answer == "pacific ocean":
    print("Correct!\n")
    score += 1
else:
    print("Wrong! The correct answer is Pacific Ocean.\n")

# Final Score
print("--------------------------------------")
print("Quiz Completed!")
print(f"Your final score is {score}/3")

if score == 3:
    print("Excellent! You got all answers correct.")
elif score == 2:
    print("Good job!")
elif score == 1:
    print("Keep learning and try again!")
else:
    print("Better luck next time!")