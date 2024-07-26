f = open('students_records.txt','w')
f.write("""
Student ID | Student Name | Grade
 101       | Alice        | A
 102       | Bob          | B
 103       | Carol        | C
""")
f.close()
s = open('students_records.txt','r')
s.readlines()

print()
