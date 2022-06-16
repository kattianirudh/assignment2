import pyodbc
server = 'adb6.database.windows.net'
database = 'assignment2'
username = 'axk3905'
password = 'Password@123'
driver = '{ODBC Driver 18 for SQL Server}'
def connect_db():
        cnxn = pyodbc.connect('DRIVER='+driver+';SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
        cursor = cnxn.cursor()
        return cursor