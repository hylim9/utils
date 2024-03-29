from django.conf import settings

import pymysql
import traceback

class sql_pymysql:
    def __init__(self):
        try:
            db = settings.DATABASES.get('default')
            
            self.con = pymysql.connect(
                host=db.get('HOST'),
                port=int(db.get('PORT')),
                user=db.get('USER'),
                password=db.get('PASSWORD'),
                db=db.get('NAME'),
                charset=db.get('OPTIONS').get('charset')
            )
            self.cursor = self.con.cursor()

        except Exception as e:
            print(traceback.format_exc())

    # def __del__(self):
    #     self.close()

    def connect(self):
        return self.con

    def close(self):
        if self.con is not None:
            self.con.close()
            self.con = None

    def sql_to_mysql(self, sql):
        try:
            self.cursor.execute(sql)
            self.con.commit()
        except Exception as e:
            print(traceback.format_exc())
        finally:
            self.close()

    def sql_to_mysql_param(self, sql, param):
        try:
            self.cursor.execute(sql, param)
        except Exception as e:
            print(traceback.format_exc())
        finally:
            self.close()

    def select_from_mysql(self, sql):
        try:
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(traceback.format_exc())
        finally:
            self.close()

    def executemany_to_mysql(self, sql, list):
        try:
            self.cursor.executemany(sql, list)
            self.con.commit()
        except Exception as e:
            print(traceback.format_exc())
        finally:
            self.close()
