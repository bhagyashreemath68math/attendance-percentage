import sys
if len(sys.argv) == 3:
    script_name = sys.argv[0]
    classes_held = sys.argv[1]
    classes_attended = sys.argv[2]

else:
    script_name = sys.argv[0]
    classes_held = 100
    classes_attended = 80
    percentage = (int(classes_attended) / int(classes_held)) * 100
    
    if percentage >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible"
    
    print("Script Name:", script_name)
    print("Classes Held:", classes_held)
    print("Classes Attended:", classes_attended)
    print("Attendance Percentage:", percentage)
    print("Status:", status)