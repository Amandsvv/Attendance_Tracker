# Name : Aman Kumar
# Roll : 2501940051
# Date : 11 Nov, 2025
# Assignment Title : Python-based Command-Line Attendance Tracker

def sep():
    print("-"*50)

print("Welcome to attendance tracker")
sep()
print("Attendance Tracker allows users to record student names and timestamps, validate enteries, and generate formatted attendance summaries automatically.")
sep()
print("\n")

student_record = {}
total_Student = input("Enter total no. of students : ")
if(not total_Student.isdigit() or (int)(total_Student) <= 0):
    sep()
    print("Please enter a valid value")
    sep()
    exit(0)


assiglum = ["st", "nd", "rd", 'th']
total_Student = int(total_Student)
sep()

i=0

while ( i < total_Student):
    x = i
    if(i > 3): x = 3
    name = input(f"Enter name of {i+1}{assiglum[x]} student : ")

    if(name.strip() == ""):
        sep()
        print("Name cannot be kept empty. Please reenter the name")
        sep()
        continue

    time = input("Enter time (e.g : 09:15 AM) : ")

    while(time.strip() == ""):
        sep()
        print("Time is required, can't kept empty. Please reenter time")
        sep()
        time = input("Enter time (e.g : 09:15 AM) : ")
    sep()
    
    if(name not in student_record):
        student_record[name] = time
    else:
        sep()
        print(f"Student {name} already marked as present")
        sep()
        continue
    print()
    i+=1

print()
sep()
print("Student Name\tCheck-In-Time")
sep()
for key,value in student_record.items():
    print(f"{key}\t{value}")
sep()
print(f"Total Students Present: {total_Student}")
sep()

choice = input('Do you wish to save the record : Enter "Y" for Yes or "N" for No: ')

if(choice == "Y"):
    with open ("./attendance_log.txt","w") as file:
        file.write('-'*50+'\n')
        file.write("Student Name\tCheck-In-Time\n")
        file.write('-'*50+'\n')
        for key,value in student_record.items():
            file.write(f"{key}\t{value}\n")
        file.write('-'*50+'\n')
        file.write(f"Total Students Present: {total_Student}\n")
        file.write('-'*50+'\n')
    print("--Records Successfully Saved--")
else:
    print("ThankYou!")

    
    
