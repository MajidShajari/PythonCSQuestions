def main():
    dict_of_students = {}
    while True:
        try:
            input_str = input("enter student name and grades (or 'exit' to quit):\n").strip()
        except EOFError:
            break
        if input_str.lower() == "exit":
            break
        parts = input_str.split()
        if len(parts) < 2:
            continue
        name = parts[0]
        grades = []
        for grade in parts[1:]:
            try:
                grades.append(float(grade))
            except ValueError:
                continue
        if not grades:
            continue
        dict_of_students[name] = grades

    if not dict_of_students:
        return

    standard = 17.0
    list_of_students_above_standard = []
    for name, grades in dict_of_students.items():
        average = sum(grades) / len(grades)
        if average > standard:
            list_of_students_above_standard.append(name)

    print(*list_of_students_above_standard, sep="\n")


if __name__ == "__main__":
    main()
