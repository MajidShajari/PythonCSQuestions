def main():
    allowed_majors = {"computer", "mathematics", "physics"}
    registered_students = []

    while True:
        try:
            line = input().strip()
        except EOFError:
            break
        if line.lower() == "exit":
            break
        parts = line.split(";")
        if len(parts) != 3:
            continue
        name = parts[0].strip()
        national_id = parts[1].strip()
        major = parts[2].strip().lower()
        if not name or not national_id or not major:
            continue
        if not national_id.isdigit() or len(national_id) != 10:
            continue
        # Check national ID validity
        digits = [int(d) for d in national_id]
        checksum = sum(digits[i] * (10 - i) for i in range(9))
        rem = checksum % 11
        if (rem < 2 and digits[9] != rem) or (rem >= 2 and digits[9] != (11 - rem)):
            print("national id Not Valid!")
            continue
        if major in allowed_majors:
            if any(student[1] == national_id for student in registered_students):
                continue
            registered_students.append((name, national_id, major))

    for student in registered_students:
        print(f"{student[0]};{student[1]};{student[2]}")


if __name__ == "__main__":
    main()
