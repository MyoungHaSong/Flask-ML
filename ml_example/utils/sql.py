import pymysql

mydb = pymysql.connect(
        host = 'localhost',
        user = 'root',
        password = '0000',
        database = 'my_rest_db'
    )

def insert(id,label,path,mydb= mydb):
    cursor = mydb.cursor()
    sql = """insert into svhn (id,label,path) values (%s,%s,%s)"""
    cursor.execute(sql,(id,int(label),path))
    print('Insert New data')
    mydb.commit()
    mydb.close()


def search_last(mydb = mydb):
    cursor = mydb.cursor()
    sql = """SELECT id, label,path FROM svhn ORDER BY id DESC LIMIT 1"""
    cursor.execute(sql)
    result = cursor.fetchall()
    for data in result:
        id,label,path = data[0],data[1],data[2]
    return id,label,path


