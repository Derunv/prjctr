def get_subjects_not_passed_by_all_students(student_exams):
    subject_scores = {}
    subject_not_passed_by_all_students = set()
    # Populate the dictionary with subjects and corresponding scores
    for name, score, subject in student_exams:
        if subject in subject_scores:
            subject_scores[subject].append(score)
        else:
            subject_scores[subject] = [score]
    for subject in subject_scores:
        #print(max(subject_scores.get(subject)))
        if max(subject_scores.get(subject)) < 60:
            subject_not_passed_by_all_students.add(subject)
    return subject_not_passed_by_all_students


def test_get_subjects_not_passed_by_all_students():
    exams = [
        ("Alice", 55, "Math"),
        ("Bob", 40, "Math"),
        ("Charlie", 30, "Math"),
        ("Alice", 50, "Science"),
        ("Bob", 45, "Science"),
        ("Charlie", 40, "Science"),
        ("Alice", 95, "History"),
        ("Bob", 85, "History"),
        ("Charlie", 90, "History"),
        ("Charli", 90, "History")
    ]
    assert get_subjects_not_passed_by_all_students(exams) == {"Science", "Math"}

test_get_subjects_not_passed_by_all_students()