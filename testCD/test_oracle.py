import cx_Oracle , sys
sys.path.append("D:\\_user_template_\\Documents\\PG\\BOT\\guild_bot\\sys_fanc")
import LOG_orig

"""
USER = "DB_BOT"
password = "DB_BOT"
HOST = "localhost"
#ポート
PORT = 1521
#SERVICE_NAME
SVS = "Oracle"
"""
#SERVICE_NAMEを指定
#print(tns)
LOG = LOG_orig.LOG(__file__)
connect=cx_Oracle.connect(user="DB_BOT", password="DB_BOT", dsn='localhost:1521/ORACLE')
#conn = cx_Oracle.connect("takuya", "taku0872", tns)
cur = connect.cursor()
cur.execute("""select name from v$database""")
rows = cur.fetchall()
for r in rows:
    print("SERVICE_NAME:%s" % (r[0]))
#SIDを確認
cur.execute("""select instance_name from v$instance""")
rows = cur.fetchall()

for r in rows:
    print("SID:%s" % (r[0]))

sql = "CREATE TABLE TEST_TABLE (COL1 NUMBER, COL2 VARCHAR(64))"
try:
    cur.execute(sql)
except cx_Oracle.DatabaseError:
    LOG.msg(sys.exc_info(),2)
