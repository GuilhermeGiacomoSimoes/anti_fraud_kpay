import mysql.connector
from mysql.connector import errorcode

def getConnection():
    try:
        cnx = mysql.connector.connect(user='root',password='root',host='127.0.0.1', database='ka_pay')
        return cnx
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something id wrong with your user name or password")
            return None 
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exists")
            return None 
        else:
            print(err)
            return None 
    else:
        cnx.close()
        return None 


def getClients():
    connection = getConnection()

    if connection != None:
        cursor = connection.cursor()
        query = ("SELECT name,birthDate,cpfCnpj,addressStreet,addressNumber,addressNeighborhood,addressCity,addressState,fraudster FROM client")
        cursor.execute(query)
    
        clients = []

        for (name,birthDate,cpfCnpj,addressStreet,addressNumber,addressNeighborhood,addressCity,addressState,fraudster) in cursor:
            client = [ 
                         name,
                         birthDate,
                         cpfCnpj,
                         addressStreet,
                         addressNumber,
                         addressNeighborhood,
                         addressCity,
                         addressState,
                         fraudster
                        ] 
            clients.append(client)

        connection.close()
        return clients


#fraudster 
