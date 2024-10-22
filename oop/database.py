import mysql.connector # type: ignore

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="12345678901234567890",
    database="mydatabase"
)
myCursor = mydb.cursor()



# INSERT Insert new data into a table

# sql = "INSERT INTO Employees (FirstName, Department) VALUES (%s, %s)"
# val = ("John", "Marines")
# myCursor.execute(sql, val)
# mydb.commit()  # Commit the changes

# myCursor.execute("select * from Employees")

# for i in myCursor:
#     print(i)

# UPDATE Modify existing data in a table
sql = "UPDATE Employees SET FirstName = %s WHERE EmployeeID = %s"
val = ("Janet", 2)
myCursor.execute(sql,val)
mydb.commit()

myCursor.execute("select * from Employees")

for i in myCursor:
     print(i)

print(mydb.get_server_info())