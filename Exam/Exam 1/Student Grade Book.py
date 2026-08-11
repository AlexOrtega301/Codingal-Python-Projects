name_score = {
    "alex": 85,
    "brian": 92,
    "charlie": 78,
    "diana": 88,
    "ethan": 95
}
for score in name_score.values():
    total_score = sum(name_score.values())
    average_score = total_score / len(name_score)
    top_scorer = max(name_score, key=name_score.get)
    bottom_scorer = min(name_score, key=name_score.get)
    input_name = input("Enter a student's name to look up their score: ").lower()
    student_score = name_score.get(input_name)
    if student_score is not None:
        print(f"{input_name.title()}'s score is: {student_score}")
    else:
        print(f"{input_name.title()} is not in the grade book.")
