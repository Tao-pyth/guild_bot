import cx_Oracle , sys
import LOG_orig

class SQL:
    def __init__(self):
        LOG = LOG_orig.LOG(__file__)
        self.LOG = LOG
        """
        USER = "DB_BOT"
        password = "DB_BOT"
        HOST = "localhost"
        #ポート
        PORT = 1521
        #SERVICE_NAME
        SVS = "Oracle"
        """
        connect=cx_Oracle.connect(user="DB_BOT", password="DB_BOT", dsn='localhost:1521/ORACLE')
        try:
            self.connect = connect
            cur = self.connect.cursor()
        except:
            self.LOG.msg(sys.exc_info(),2)
    def CREATE(self,TABLE_name,column):
        """
        self = *
        TABLE_name = STR
        column = LIST
        """
        SQL_txt = 'CREATE TABLE '
        SQL_txt += TABLE_name
        SQL_txt += " (\n"
        for x in colimn:
            column_name = str(x[0]) + ' '
            column_type = str(x[1])
            if x[2] == 1:
                column_null = ' NOT NULL'
            elif x[2] == 2:
                column_null = ' NOT NULL PRIMARY KEY'
            else:
                column_null = ' NULL'
            if x[3] is NONE:
                column_def_ = ','
            else:
                column_def_ = 'DEFAULT(' + str(x[3]) + '),\n'
            SQL_txt += column_name + column_type + column_null + column_def_
        SQL_txt += ')'
        self.LOG.SQL(SQL_txt)
        try:
            cur.execute(SQL_txt)
        except cx_Oracle.DatabaseError:
            LOG.msg(sys.exc_info())

    def DROP(self,TABLE_name):
        """
        self = *
        TABLE_name = STR
        column = LIST
        """
        SQL_txt = 'DROP TABLE '
        SQL_txt += TABLE_name
        try:
            cur.execute(sql)
        except cx_Oracle.DatabaseError:
            LOG.msg(sys.exc_info())
