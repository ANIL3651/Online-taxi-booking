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
        print("Error! : ", sys.exc_info())

    finally:
        return conn


def insertCustomer(customerInfo):

    sql = """INSERT INTO customer VALUES (%s, %s, %s, %s ,%s, %s, %s)"""
    values = (customerInfo.getCID(), customerInfo.getName(), customerInfo.getAddress(),
              customerInfo.getEmail(), customerInfo.getContactNo(), customerInfo.getPayment(),
              customerInfo.getPassword())
    result=False
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        result=True


    except:
        print("Error : ", sys.exc_info())

    finally:
        del values
        del sql
        return result



def getAllCustomer():

    sql = """SELECT * FROM customer"""
    customer = None
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql)
        customer = cursor.fetchall()
        cursor.close()
        conn.close()

    except:
        print("Error !", sys.exc_info())
    finally:
        del sql
        return customer


def logincustomer(customer):
    sql = """SELECT * FROM customer WHERE email = %s and password= %s"""
    values = (customer.getEmail(), customer.getPassword())
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



