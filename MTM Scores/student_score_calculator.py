def calculate_score():
    print("\n--- Enter Counts for a Student ---")
    student_name = input("Enter student's name (or type 'done' to finish): ")
    if student_name.lower() == 'done':
        return None

    try:
        purple_count = int(input(f"Enter number of PURPLE squares for {student_name}: "))
        orange_count = int(input(f"Enter number of ORANGE squares for {student_name}: "))
        green_count = int(input(f"Enter number of GREEN squares for {student_name}: "))
        blue_count = int(input(f"Enter number of BLUE squares for {student_name}: "))
        pink_count = int(input(f"Enter number of PINK squares for {student_name}: "))
        gold_count = int(input(f"Enter number of GOLD squares for {student_name}: "))
    except ValueError:
        print("Invalid input. Please enter whole numbers only.")
        return calculate_score() # Retry for the same student

    total_score = (purple_count * 3) + \
                  (orange_count * 4) + \
                  (green_count * 5) + \
                  (blue_count * 1) + \
                  (pink_count * 2) + \
                  (gold_count * 10)

    print(f"\nTotal score for {student_name}: {total_score}")
    return {"name": student_name, "score": total_score}

all_student_scores = []
while True:
    result = calculate_score()
    if result is None:
        break
    all_student_scores.append(result)

if all_student_scores:
    print("\n--- All Student Totals ---")
    for student in all_student_scores:
        print(f"{student['name']}: {student['score']}")
else:
    print("No student scores were entered.")