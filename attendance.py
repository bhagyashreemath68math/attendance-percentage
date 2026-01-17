import sys
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    classes_held = sys.argv[1]
    classes_attended = sys.argv[2]

else:
    script_name = sys.argv[0]
    classes_held = input("Enter number of classes held: ")
    classes_attended = input("Enter number of classes attended: ")
    percentage = (int(classes_attended) / int(classes_held)) * 100

    if percentage >= 75:
        print("Eligible")
        status = "Eligible"
    else:
        print("Not Eligible")
        status = "Not Eligible"
    
    print("Script Name:", script_name)
    print("Classes Held:", classes_held)
    print("Classes Attended:", classes_attended)
    print("Attendance Percentage:", percentage)
    print("Print Status:", status)