import sqlite3

from threading import Event

print("\n""\n")
i=0
while i<200:
    print("الرجاء اختيار العملية التي تريد اجراىها")
    print("\n")
    print("      لاضافة طالب اضغط على حرف       a ")
    print("    لحذف طالب اضغط على حرف      d ")
    print("    لتعديل معلومات طالب اضغط على حرف u ")
    print("    لعرض معلومات طالب اضغط على الحرف s ")
    letters=["a","d","u","s"]
    print("\n")
    letters=input("Enter a letter:")

    conn = sqlite3.connect('school.db') 
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS students 
                (studentId INTEGER PRIMARY KEY,
                firstName TEXT not null,
                lastName TEXT not null, 
                age INTEGER not null, 
                grade TEXT not null,
                date TEXT not null);''')
    cur.execute("DROP table if exists lessons")
    cur.execute('''CREATE TABLE IF NOT EXISTS lessons 
                (lessonId INTEGER PRIMARY KEY,
                lesson TEXT not null);''')
    cur.execute('''CREATE TABLE IF NOT EXISTS registless(
                operaId  INTEGER PRIMARY KEY AUTOINCREMENT, 
                lessonId integer not null,
                studentId integer not null,
                foreign key (studentId) references students (studentId));''')


    if "a" in letters:
         
        studentId = input("Enter studentId : ")
        firstName      = input("Enter firstName : ")
        lastName    = input("Enter lastName : ")
        age    = int(input("Enter age: "))
        grade   = input("Enter the grade : ")
        date = input("Enter the date : ")
        cur.execute("INSERT INTO students (`studentId` , `firstName` , `lastName` , `age` , `grade` , `date`) VALUES (?, ?, ?, ?, ?, ?)",(studentId, firstName , lastName , age , grade , date))

        #ظهور ان السطر قد اضيف
        print(cur.rowcount, "ligne insérée.")

        cur.execute("INSERT INTO lessons (lessonId, lesson) VALUES (1, 'php')")
        cur.execute("INSERT INTO lessons (lessonId, lesson) VALUES (2, 'javascript')")
        cur.execute("INSERT INTO lessons (lessonId, lesson) VALUES (3, 'python')")
        cur.execute("INSERT INTO lessons (lessonId, lesson) VALUES (4, 'ruby')")

        #عدد الدروس المسجل فيها الطالب
        print("الرجاء اختيار الدروس التي تريدها")
        print("المكون php        اضغط على        1")
        print("المكون javascript اضغط على        2")
        print("المكون python     اضغط على        3")
        print("المكون ruby       اضغط على        4")

        number=[1,2,3,4]
        number=int(input("كم من مكون تريد التسجيل فيه :"))
        
        i=1
        while i<=number :
            lessonId=input("ادخل رقم المكون :")
            cur.execute("insert into registless ('lessonId', 'studentId') VALUES (?, ?)",(lessonId, studentId))
            i+=1

        conn.commit()
        print("")
        print("  تمت العملية بنجاح   ")
        Event().wait(4)

    elif "d" in letters:
        
        studentId=int(input("Enter studentId : "))
        row=cur.execute("SELECT * from students WHERE studentId = ?",(studentId,)).fetchall()
        print(row)

        row = cur.execute("SELECT * from registless WHERE studentId = ?", (studentId,)).fetchall()
        print(row)
        Event().wait(5)

        reponse=  input(" تريد اتمام عملية الحذف ؟ [o/n] :")
        reponse= reponse.strip().lower()
        if reponse.startswith('o'):
            x = cur.execute("delete  FROM students WHERE studentId = ?", (studentId,))
            x = cur.execute("delete  FROM registless WHERE studentId = ?", (studentId,))
            conn.commit()
        elif reponse.startswith('n') or reponse =='':
            print("الى اللقاء")
        else:
            print("اجب ب 'o' ou 'n'")


        Event().wait(5)
        print("")
        print("  تمت العملية بنجاح   ")
        Event().wait(4)

         
    elif "u" in letters:
        
        studentId=input("Enter studentId : ")
        row = cur.execute("SELECT * from students WHERE studentId = ?", (studentId,)).fetchall()
        print(row)
        print("\n")
        newfirstName=  input("Enter newfirstName : ")

        cur.execute("UPDATE students set firstName= ? WHERE studentId=? ", (newfirstName, studentId))
        conn.commit()
        
        print("")
        print("  تمت العملية بنجاح   ")
        Event().wait(4)
        
    elif "s" in letters:
        
        studentId=int(input("Enter studentId : "))
        row=cur.execute("SELECT * from students WHERE studentId = ?",(studentId,)).fetchall()
        print(row)
            
        print("")
        print("  تمت العملية بنجاح   ")
        Event().wait(5)
        
    else:
        print("\n")
        print ("         ERROR : خطا")
        Event().wait(4)
    
    conn.commit()
    conn.close()
i+=1   
