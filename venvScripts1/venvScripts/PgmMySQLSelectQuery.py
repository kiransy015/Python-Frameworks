import mysql.connector

mydb = mysql.connector.connect(
    host="135.250.138.238",
    user="aordbremote",
    passwd="invinci8le_REM",
    database="tra"
)

mycursor = mydb.cursor()
mycursor.execute("select * from ASIGNACION_ALARMAS")
myresult = mycursor.fetchall()

for x in myresult:
    print(x)