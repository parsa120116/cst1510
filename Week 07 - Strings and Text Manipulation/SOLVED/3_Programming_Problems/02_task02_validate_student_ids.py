def is_valid_id(student_id):
    """Return True if student_id is "M00" followed by 6 digits (9 characters in total)."""
    if not student_id.startswith("M00"):
        return False
    if len(student_id) != 9:
        return False
    return student_id[3:].isdigit()


student_ids = ["M00123456", "M0012345", "X00123456", "M00ABCDEF", "M00987654"]

for student_id in student_ids:
    if is_valid_id(student_id):
        print(f"{student_id}: valid")
    else:
        print(f"{student_id}: INVALID")
