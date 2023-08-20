import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="mysqlserver",
    user="root",
    password="MyNewPass",
    port =3306,
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "INSERT INTO mbta_buses (id, latitude, longitude, occupancy_status, current_status, current_stop_sequence, bearing, direction_id, route_id, stop_id, trip_id, updated_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (
            mbtaDict['id'],
            mbtaDict['latitude'],
            mbtaDict['longitude'],
            mbtaDict['occupancy_status'],
            mbtaDict['current_status'],
            mbtaDict['current_stop_sequence'],
            mbtaDict['bearing'],
            mbtaDict['direction_id'],
            mbtaDict['route_id'],
            mbtaDict['stop_id'],
            mbtaDict['trip_id'],
            mbtaDict['updated_at']
        )
        mycursor.execute(sql, val)

    mydb.commit()