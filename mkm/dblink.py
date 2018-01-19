import MySQLdb
import time
import traceback

class dblink():


    def __init__(self,ip,username,passwd,database):
        self.ip = ip
        self.username = username
        self.passwd = passwd
        self.database = database
        pass

    def getConnect(self):
        db = MySQLdb.connect(self.ip, self.username, self.passwd, self.database,charset="utf8")
        return db

    def findOne(self, conn, sql):
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            data =   cursor.fetchone()
            return data
        except Exception, e:
            print("mysql exception:" + e.message)
            print traceback.print_exc()

    def executQuery(self, conn, sql):
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            data = cursor.fetchall()
            return data
        except Exception, e:
            print("mysql exception:" + e.message)
            print traceback.print_exc()

    def update(self,conn,sql):
        try:
            cursor = conn.cursor()
            cursor.execute(sql)
            conn.commit()
        except Exception,e:
            print("mysql exception:"+str(e))
            print traceback.print_exc()


    def saveBydatas(self,tablename,datas):
        try:
            db = MySQLdb.connect(self.ip, self.username, self.passwd, self.database)
            cursor = db.cursor()

            index = 1
            for row in datas:
                cols=""
                for col in row :
                    cols=cols+col+","
                cols=cols+str(1)
                sql="insert into "+tablename+" values("+str(cols)+")"
                print cols
                cursor.execute(sql)
                if(index % 100 == 0 ):
                    db.commit()
            db.commit()
            db.close()
        except Exception,e:
            db.close()
            print("mysql exception:"+e)
    def query(self,sql):
        try:
            db = MySQLdb.connect(self.ip, self.username, self.passwd, self.database,charset="utf8")
            cursor = db.cursor()
            cursor.execute(sql)
            data=cursor.fetchall()
            return data
        except Exception,e:
            db.close()
            print("mysql exception:" + e.message)

    def close(self, conn):
        conn.close();