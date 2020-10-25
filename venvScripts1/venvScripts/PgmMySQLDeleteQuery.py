import mysql.connector

mydb = mysql.connector.connect(
    host="135.250.138.238",
    user="aordbremote",
    passwd="invinci8le_REM",
    database="astro_mba"
)

sql="delete from EVENTOS_OMEGA_ASTRO where ID_EVENTO='7000'"

mycursor = mydb.cursor()
mycursor.execute(sql)
mydb.commit()

x = print(mycursor.rowcount, " records deleted")
