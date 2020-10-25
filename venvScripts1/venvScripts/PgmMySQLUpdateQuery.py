import mysql.connector

mydb = mysql.connector.connect(
    host="135.250.138.238",
    user="aordbremote",
    passwd="invinci8le_REM",
    database="astro_mba"
)

sql = "update CORRECTIVO_OMEGA_ASTRO set ID_EVENTO=107 where ID_EVENTO=105"

mycursor = mydb.cursor()
mycursor.execute(sql)
mydb.commit()
print('No of rows affected :',mycursor.rowcount)