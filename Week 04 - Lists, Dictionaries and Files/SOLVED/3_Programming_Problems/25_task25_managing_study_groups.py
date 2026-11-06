study_groups = {
    "John": {"Math", "Physics"},
    "Emily": {"Physics", "Biology"},
    "Alex": {"Math"},
}


def join_group(groups, student, group):
    """Add a student to a study group."""
    if student not in groups:
        groups[student] = set()            # a new student
    if group in groups[student]:
        print(f"{student} is already in {group}.")
    else:
        groups[student].add(group)
        print(f"{student} joined {group}.")


def leave_group(groups, student, group):
    """Remove a student from a study group."""
    if student in groups and group in groups[student]:
        groups[student].remove(group)
        print(f"{student} left {group}.")
    else:
        print(f"{student} is not in {group}.")


def show_groups(groups, student):
    """Print all the groups a student belongs to."""
    if student in groups and len(groups[student]) > 0:
        group_list = ", ".join(sorted(groups[student]))
        print(f"{student}'s groups: {group_list}")
    else:
        print(f"{student} is not in any group.")


def members_of(groups, group):
    """Return a sorted list of the students in one group."""
    return sorted([student for student in groups if group in groups[student]])


show_groups(study_groups, "John")
join_group(study_groups, "John", "Chemistry")
join_group(study_groups, "John", "Math")
leave_group(study_groups, "John", "Physics")
show_groups(study_groups, "John")
print()
join_group(study_groups, "Sara", "Biology")
leave_group(study_groups, "Alex", "Math")
leave_group(study_groups, "Alex", "Art")
show_groups(study_groups, "Alex")
show_groups(study_groups, "Sara")
print()
print("Biology members:", members_of(study_groups, "Biology"))
