# quiz system

# question bank as list of tuples
# (question, A, B, C, D, correct)

questions = [
    ("Which data type is immutable in Python?", "List", "Dictionary", "Tuple", "Set", "C"),
    ("What is output of print(2**3)?", "6", "8", "9", "12", "B"),
    ("Which keyword defines a function?", "fun", "define", "def", "function", "C"),
    ("What does size() do?", "Adds items", "Returns length", "Deletes items", "Sorts list", "B"),
    ("How to write single line comment?", "//", "/*", "#", "<!--", "C"),
    ("How to create a dictionary?", "d=[]", "d=()", "d={}", "d=<>", "C"),
    ("Which loop runs when iterations are unknown?", "for", "while", "do while", "repeat", "B"),
    ("What will bool('') return?", "True", "None", "Error", "False", "D"),
    ("Which method adds element to list?", "add()", "append()", "insert()", "push()", "B"),
    ("What is type(10.5)?", "int", "content", "float", "double", "C"),
]

print("===== PYTHON QUIZ SYSTEM =====")
name = input("Enter Name: ").strip()

while True:
    try:
        rollno = int(input("Enter Roll No: "))
        break
    except ValueError:
        print("Enter a valid roll number")

print(f"Hello {name}! Lets start the quiz")

score = 0
wrong_answers = []

for idx in range(len(questions)):
    q = questions[idx]

    print(f"\nQ{idx + 1}: {q[0]}")
    print(f"  A. {q[1]}")
    print(f"  B. {q[2]}")
    print(f"  C. {q[3]}")
    print(f"  D. {q[4]}")

    while True:
        ans = input("Your Answer: ").strip().upper()
        if ans in ["A", "B", "C", "D"]:
            break
        print("Please enter A, B, C or D only")

    if ans == q[5]:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Right answer was {q[5]}\n")
        wrong_answers.append((q[0], ans, q[5]))

total = len(questions)
percent = (score / total) * 100

if percent >= 90:
    grade = "O"
elif percent >= 80:
    grade = "A+"
elif percent >= 70:
    grade = "A"
elif percent >= 60:
    grade = "B+"
elif percent >= 50:
    grade = "B"
else:
    grade = "F"

if percent >= 50:
    result = "PASS"
else:
    result = "FAIL"

print("====== RESULT REPORT ======")
print(f"Name    : {name}")
print(f"Roll No : {rollno}")
print(f"Score   : {score} / {total}")
print(f"Percent : {percent:.2f}%")
print(f"Grade   : {grade}")
print(f"Result  : {result}")

if len(wrong_answers) == 0:
    print("Perfect score! Well done")
else:
    print("--- Questions You Got Wrong ---")
    for idx, w in enumerate(wrong_answers, start=1):
        print(f"   {idx}. {w[0]}")
        print(f"   Your Answer : {w[1]}")
        print(f"   Correct Ans : {w[2]}")