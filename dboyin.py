import mysql.connector


class Core:
    def __init__(self):
        super().__init__()
        self.__connectbd()
        self.createTable()
        
        
    def __connectbd(self):
        try: 
            self.conn=mysql.connector.connect(
                host='localhost',
                database='oyindb',
                user='root',
                password='root'
            )
        except Exception as err:
            print(err)
        else:
            # print('ulandi')
            pass
        
    def createTable(self):
        try:
            with self.conn.cursor() as cursor:
                sql='''create table if not exists user(
                        id serial,
                        first_name varchar(64) not null,
                        last_name varchar(64) not null,
                        login varchar(32) not null unique,
                        password varchar(32) not null
                    )'''       
                cursor.execute(sql)
        except Exception as err:
            print(err)
        else:
            # print("table yaratildi")
            pass
            
    def createuser(self,fname,lname,login,parol):
        try:
            with self.conn.cursor() as cursor:
                query=f'''
                    insert into user(first_name,last_name,login,password) 
                    values('{fname}','{lname}','{login}','{parol}');'''
                cursor.execute(query)
        except Exception as err:
            print(err)
        else:
            self.conn.commit()
            return True
            
    def getuser(self,login):
        with self.conn.cursor() as cursor:
            query=f'''select * 
                from user
                where login="{login}" 
                '''
            cursor.execute(query)
            resut=cursor.fetchone()
            
        if resut!=None:
            return False
        else:
            return True
        
    def getUserloginandparol(self,login,parol):
        with self.conn.cursor() as cursor:
            query=f'''select * 
                from user
                where login="{login}" and password="{parol}"
                '''
            cursor.execute(query)
            resut=cursor.fetchone()
            
        if resut==None:
            return False
        else:
            return True
        

                
                
