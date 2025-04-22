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


def insertTrip(trip):
    sql = """INSERT INTO trip VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
    values = (
    trip.getTID(), trip.getPUtime(), trip.getPUdate(), trip.getPUaddress(), trip.getDOaddress(), trip.getStatus(),
    trip.getCID(), trip.getDID())
    result1 = False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result1 = True
    except:
        print("Error: ", sys.exc_info())

    finally:
        del values
        del sql
        return result1


def searchTrip(tid):
    sql = """ SELECT * FROM trip WHERE tid = %s"""
    values = (tid,)
    trip = None

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        trip = cursor.fetchone()
        cursor.close()
        conn.close()

    except:
        print("Error : ", sys.exc_info())

    finally:
        del values
        del sql
        return trip


def editTrip(trip):

    sql = """ UPDATE trip SET PUtime= %s, PUdate = %s ,PUaddress= %s, DOaddress= %s where tid=%s"""
    values = (trip.getPUtime(), trip.getPUdate(), trip.getPUaddress(), trip.getDOaddress(),
              trip.getTID())
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
        print("Error! : "), sys.exc_info()
    finally:
        del values
        del sql
        return result


def deleteTrip(tid):
    sql = """DELETE FROM trip WHERE tid=%s"""
    values = (tid,)
    result = False

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    except:
        print("Error ", sys.exc_info())

    finally:
        del values
        del sql

        return result


def getAllTrip(cid):
    sql = """SELECT * FROM trip WHERE cid=%s """
    values = (cid,)
    trip = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        trip = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error !", sys.exc_info())
    finally:
        del sql
        del values
        return trip


def assingTrip():
    sql = """SELECT * FROM trip WHERE status='pending' """
    trip = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        trip = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error !", sys.exc_info())
    finally:
        del sql

        return trip


def getTid(cid):
    sql = """SELECT tid  FROM trip WHERE cid=%s and status='pending' """
    values = (cid,)
    trip = None

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        trip = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error !", sys.exc_info())
    finally:
        del values
        del sql
        return trip


def getTrip():
    sql = """SELECT *  FROM trip """

    trip = None

    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        trip = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error !", sys.exc_info())
    finally:

        del sql
        return trip


def assignDriver(okay):
    sql = """ UPDATE trip SET did=%s, status='booked' WHERE tid=%s """
    values = (okay.getDID(), okay.getTID())
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
        print("Error! : "), sys.exc_info()
    finally:
        del values
        del sql
        return result


def completeTrip(okay):
    sql = """ UPDATE trip SET did=%s, status='completed' WHERE tid=%s """
    values = (okay.getDID(), okay.getTID())
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
        print("Error! : "), sys.exc_info()
    finally:
        del values
        del sql
        return result


def confirmTrip(did):
    sql = """SELECT * FROM trip WHERE status='booked' AND did=%s """
    values = (did,)
    trip = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        trip = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error !", sys.exc_info())
    finally:
        del values
        del sql
        return trip
