import mysql.connector

mydb = mysql.connector.connect(
    host="135.250.138.238",
    user="aordbremote",
    passwd="invinci8le_REM",
    database="astro_mba"
)

sql = "INSERT INTO `CORRECTIVO_OMEGA_ASTRO` (`FECHA_INS_TAB`, `ID_TAREA_GF`, `ID_EVENTO`, `FECHA_EVENTO`, `ESTADO_TAREA`, `MAQUINA`, `TAREA_ASOCIADA`, `ESTADO_INTERNO_TAREA`, `MOTIVO_TAREA`, `GRI_ASOCIADO`, `CESABLE`, `ID_CAUA`) VALUES ('2019-04-30 16:03:35', '8:1556620414579', 105, 1556620413, 'P', 'aorfit431', '', 'F', 'I', NULL, 'SI', 2908)"

mycursor = mydb.cursor()
mycursor.execute(sql)
mydb.commit()

print("No of queries inserted :",mycursor.rowcount)