def main():

    subjects = int(input("🎯 Enter number of subjects: "))
    total = obtained = 0

    for i in range(subjects):
        t = float(input(f"\nTotal marks for subject #{i+1}: "))
        o = float(input("Obtained marks: "))
        total += t
        obtained += o

    percent = (obtained / total) * 100 if total > 0 else 0

    # Determine grade and color
    if percent >= 90:
        grade, color = "A+", GREEN
    elif percent >= 80:
        grade, color = "A", GREEN
    elif percent >= 70:
        grade, color = "B", YELLOW
    elif percent >= 60:
        grade, color = "C", YELLOW
    elif percent >= 50:
        grade, color = "D", YELLOW
    else:
        grade, color = "F (Fail)", RED

    print(f"\n📊 Total: {total}, Obtained: {obtained}, Percentage: {percent:.2f}%, Grade: {color}{grade}{RESET}")

main()
