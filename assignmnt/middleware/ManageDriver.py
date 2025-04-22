import mysql.connector
import sys
def connect():
    conn = None

    try:
        conn = mysql.connector.connect(
            host='localhost',
            port='3306',
            user='root',
            password='',
            database='taxibooking'
        )
    except:
        print("Error !", sys.exc_info())
    finally:
        return conn

def saveDriver(driverInfo):
    sql = """INSERT INTO driver VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (driverInfo.getDID(),
              driverInfo.getName(),
              driverInfo.getEmail(),
              driverInfo.getAddress(),
              driverInfo.getLicenseNo(),
              driverInfo.getPassword())
    result = False

    try:

        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result = True
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        return result



def displayAllDriver():

    sql = """ SELECT * FROM driver """
    driver = None

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        driver = cursor.fetchall()

        cursor.close()
        conn.close()

    except:
        print("Error: ", sys.exc_info())
    finally:
        del sql
        return driver





def logindriver(driver):
    sql = """SELECT * FROM driver WHERE email = %s and password= %s"""
    values = (driver.getEmail(), driver.getPassword())
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        return  result

def loginAdmin(admin):
    sql = """SELECT * FROM admin WHERE username = %s and password= %s"""
    values = (admin.getUsername(), admin.getPassword())
    result = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        result = cursor.fetchone()
        cursor.close()
        conn.close()


    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        return result


def getAllDriverid():
    sql = """SELECT did FROM driver """
    driver = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        driver = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error !", sys.exc_info())
    finally:
        del sql
        return driver

