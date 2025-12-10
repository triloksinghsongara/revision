student=dict()
logged=False
logged_user=" "
from datetime import datetime
ans = {
    "python": [2, 1, 2, 2, 2, 2, 1, 2, 1, 2],

    "DSA": [1, 2, 2, 2, 2, 1, 1, 2, 2, 2],

    "DBMS": [1, 1, 1, 2, 1, 2, 1, 1, 2, 2]
}
userlist=[]
passwordlist=[]

#-------------connectivity----------------------
import mysql.connector as ms
DB=ms.connect(
    host="127.0.0.1",
    user="root",
    password="", #your password
    database="", # your database name
)
mycursor=DB.cursor()















option = {
    "python": {
        1: "Python was developed by:  1: Bjarne Stroustrup  2: Guido van Rossum",
        2: "List is:  1: mutable  2: immutable",
        3: "Tuple is:  1: mutable  2: immutable",
        4: "Dictionary contains:  1: collection of individual data  2: pair of keys and values",
        5: "Which keyword is used to define a function?  1: func  2: def",
        6: "Which of the following is used to take input?  1: scanf()  2: input()",
        7: "Which operator is used for exponentiation?  1: **  2: ^",
        8: "Which data type is immutable?  1: List  2: Tuple",
        9: "Which keyword is used for loops?  1: for  2: repeat",
        10: "Which is used to include modules in Python?  1: include  2: import"
    },

    "DSA": {
        1: "Which data structure uses FIFO order?  1: Queue  2: Stack",
        2: "Which data structure uses LIFO order?  1: Queue  2: Stack",
        3: "Which searching algorithm works on sorted arrays?  1: Linear Search  2: Binary Search",
        4: "Which sorting algorithm is fastest on average?  1: Bubble Sort  2: Quick Sort",
        5: "Which data structure is used in recursion?  1: Queue  2: Stack",
        6: "Which traversal visits root first in a tree?  1: Preorder  2: Inorder",
        7: "Which data structure is used for BFS?  1: Queue  2: Stack",
        8: "Which data structure is used for DFS?  1: Queue  2: Stack",
        9: "Time complexity of binary search is:  1: O(n)  2: O(log n)",
        10: "Linked list elements are stored in:  1: Continuous memory  2: Non-continuous memory"
    },

    "DBMS": {
        1: "DBMS stands for:  1: Database Management System  2: Data Base Managing Source",
        2: "Which of the following is a primary key?  1: Unique identifier  2: Duplicate value",
        3: "Which command is used to retrieve data?  1: SELECT  2: UPDATE",
        4: "Which of the following is not a SQL command?  1: CREATE  2: MAKE",
        5: "Which key is used to link two tables?  1: Foreign key  2: Local key",
        6: "Which normal form removes partial dependency?  1: 1NF  2: 2NF",
        7: "Which SQL clause is used to filter records?  1: WHERE  2: ORDER BY",
        8: "Which of these ensures uniqueness?  1: UNIQUE  2: DEFAULT",
        9: "Which SQL statement is used to delete data?  1: DROP  2: DELETE",
        10: "Which of the following stores data permanently?  1: RAM  2: Hard Disk"
    }
}
def loaddata():
   global userlist,passwordlist
   mycursor.execute("SELECT * FROM registration")

   rows = mycursor.fetchall()
   
   for row in rows:
     userlist.append(row[2])
     passwordlist.append(row[4])
   
     
    


def register():
    global logged_user
    name=input("enter your name")
    username=input("enter user name")
    email=input("enter your email")
    password=input("enter password")
    while(True):
        repassword=input("enter re password")
        if(password==repassword):
            break
        else:
            print("plese enter same password")
    
    
    query = "INSERT INTO registration (name, username, email , password) VALUES (%s, %s, %s, %s)"
    values=[name,username,email,password]
    mycursor.execute(query,values)
    DB.commit()
    
    print("ragistration succesfull")
    logged_user=username
    return main()
 

def login():
    global logged,logged_user,userlist,passwordlist
    try:
        loaddata()
        username=input("enter username")
        upassword=input("enter password")
        if username in userlist :
            index=userlist.index(username)
            if upassword==passwordlist[index]:
                print("login succesfully")
                logged_user=username
                logged=True
                return main()
                
            else:
                print("wrong password")
                return login()
        else:
            print("username doesnt exist")
            return login()


    except:
        print("please register first")
        register()


    
def show_profile():
    global logged,logged_user
    if(not logged):
        print("plese login first")
        main()
    else:
        user=student[logged_user]
        print(f'''
username: {logged_user}
name:  {user["name"]}
email: {user["email"]}

''')
    
def update_profile():
    global logged,logged_user
    if(not logged):
        print("login first")
        return main()
    else:
        print("update dahsboard")
        username=input("enter new user name")
        name=input("enter new name")
        query = "UPDATE registration SET name=%s, username=%s WHERE username=%s"

        values=[name,username,logged_user]
        mycursor.execute(query,values)
        DB.commit()
        print("updated succesfully")
        return main()


def logout():
    global logged
    if(not logged):
        print("you are already logged out")
        main()
    else:
        logged=False
        main()
def quiz():
    if(logged):
        print(f'''
welcome in quiz {logged_user}''')
        score=0
        print('''
Choose option for category of qustion
              1.PYTHON
              2.DSA
              3.DBMS
''')
        input_category=int(input("enter your option"))

        if(input_category==1):
            for i in range(1,11) :
                print(f'''
your question no. {i}
{option["python"][i]}
''')
                user_ans=int(input("enter option"))
                if(user_ans==ans["python"][i-1]):
                    score+=5
                    print("right answer")
                else:
                    print("wrong answer")
            print(f'''
your score is:  {score}/50
''')
            score=str(score)
            score=score+"/50"

            now = datetime.now()
            formatted = now.strftime("%d-%m-%Y %H:%M:%S")
            query = "INSERT INTO quizdata (category,score,username,Date) VALUES (%s, %s, %s, %s)"
            values=["Python",score,logged_user,formatted]
            mycursor.execute(query,values)
            DB.commit()
            
            return main()
        elif(input_category==2):
            for i in range(1,11) :
                print(f'''
your question no. {i}
{option["DSA"][i]}
''')
                user_ans=int(input("enter option"))
                if(user_ans==ans["DSA"][i-1]):
                    score+=5
                    print("right answer")
                else:
                    print("wrong answer")
            print(f'''
your score is:  {score}/50
''')
            score=str(score)
            score=score+"/50"

            now = datetime.now()
            formatted = now.strftime("%d-%m-%Y %H:%M:%S")
            query = "INSERT INTO quizdata (category,score,username,Date) VALUES (%s, %s, %s, %s)"
            values=["DSA",score,logged_user,formatted]
            mycursor.execute(query,values)
            DB.commit()
            

           
            return main()
        


        elif(input_category==3):
            for i in range(1,11) :
                print(f'''
your question no. {i}
{option["DBMS"][i]}
''')
                user_ans=int(input("enter option"))
                if(user_ans==ans["DBMS"][i-1]):
                    score+=5
                    print("right answer")
                else:
                    print("wrong answer")
            print(f'''
your score is:  {score}/50
''')
            score=str(score)
            score=score+"/50"

            now = datetime.now()
            formatted = now.strftime("%d-%m-%Y %H:%M:%S")
            query = "INSERT INTO quizdata (category,score,username,Date) VALUES (%s, %s, %s, %s)"
            values=["DBMS",score,logged_user,formatted]
            mycursor.execute(query,values)
            DB.commit()
            return main()
        else:
            print("wrong choice")
            quiz()
            
             

    else:
      print("login first")
    return main()

          

def terminate():
    exit()

def main():
    print("Welcome in LNCT")
    response = input('''
        Choose option:
        1. Registration
        2. Login
        3. Profile
        4. Update profile
        5. Logout
        6. Main Menu
        7.Attempt quiz
        8.Exit                

            select option 1/2/3/4/5/6/7/8: ''')

    if response == '1':
        register()
    elif response == '2':
        login()
    elif response == '3':
        show_profile()
    elif response == '4':
        update_profile()
    elif response == '5':
        logout()
    elif response == '6':
        main()
    elif response == '7':
        quiz()
    elif response == '8':
        terminate()

    else:
        print("Invalid Choice, Please select correct option")
        main()
main()
