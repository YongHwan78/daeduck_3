# Module Imports
# pip install pymysql
import pymysql


conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='python', charset='utf8', port=3306)


# pymysql.cursors.DictCursor
cur = conn.cursor( pymysql.cursors.DictCursor) # 튜플 형태로 준다 Dictionary Cursor --> JSON 과 같다.

sql = """select 
        e_id, e_name, gen, addr 
        from emp
    """

cur.execute(sql)
results = cur.fetchall()

print(results)

conn.close()