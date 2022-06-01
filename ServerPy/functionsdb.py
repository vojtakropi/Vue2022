import mysql.connector
from mysql.connector import Error


def connectdbget():
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='vue2022db',
                                             user='root',
                                             password='Vojtakropi20')
        if connection.is_connected():
            sql_prepare_query = "SELECT * from scoreboard"
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_prepare_query)
            records = cursor.fetchall()
            cursor.close()
            connection.close()
        return records

    except Error as e:
        print("Error while connecting to MySQL", e)


def connectdbdel(username):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='vue2022db',
                                             user='root',
                                             password='Vojtakropi20')
        if connection.is_connected():
            sqlquery = "DELETE FROM users WHERE userName='%s'" % username
            cursor = connection.cursor(buffered=True)
            cursor.execute(sqlquery)
            connection.commit()
            cursor.close()
            connection.close()

    except Error as e:
        print("Error while connecting to MySQL", e)


def connectdbdput(username, passwd):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='vue2022db',
                                             user='root',
                                             password='Vojtakropi20')
        if connection.is_connected():
            sql_prepare_query = "INSERT INTO users (userName, passwd) VALUES (%s,%s)"
            values = (username, passwd)
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_prepare_query, values)
            connection.commit()
            cursor.close()
            connection.close()

    except Error as e:
        print("Error while connecting to MySQL", e)



def connectdbdpatch(username, passwd):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='vue2022db',
                                             user='root',
                                             password='Vojtakropi20')
        if connection.is_connected():
            sql_prepare_query = "UPDATE users SET passwd = %s WHERE userName=%s"
            values = (passwd, username)
            cursor = connection.cursor(buffered=True)
            cursor.execute(sql_prepare_query, values)
            connection.commit()
            cursor.close()
            connection.close()

    except Error as e:
        print("Error while connecting to MySQL", e)

if __name__ == "__main__":
    #connectdbdel('vojta')
    #connectdbdput('uiaDUGHSUI', 'AIUSDUIAS')
    connectdbdpatch('uiaDUGHSUI', 'asiudajis')
   # a = connectdbget()