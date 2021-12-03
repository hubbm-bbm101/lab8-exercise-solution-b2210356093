import sys
try:
    with open(sys.argv[1], encoding="utf-8") as inputFile:
        student_dict = {}
        for entry in inputFile:
            studentname = entry.split(":")[0]
            student_dict[studentname] = (entry.strip().split(":")[1]).split(",")

        for name in sys.argv[2].strip().split(","):
            if not name:
                print("You cant't leave empty after comma. You should write a name.")
            else:
                try:
                    university = student_dict[name][0]
                    department = student_dict[name][1]
                    print(f" - NAME: {name} - UNIVERSITY: {university} - DEPARTMENT: {department}")
                except KeyError:
                    print(f" - No record of {name} was found.")
except FileNotFoundError:
    print(f"ERROR: FileNotFound! There is no file named {sys.argv[1]} ")
except IndexError:
    print(f"You should run this python script from command line terminal.")

