# Module Imports
# pip install pymysql
import pymysql


conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='python', charset='utf8', port=3305)


# pymysql.cursors.DictCursor
cur = conn.cursor( pymysql.cursors.DictCursor) # 튜플 형태로 준다 Dictionary Cursor --> JSON 과 같다.

sql = """INSERT INTO emp 
    (e_id, e_name, gen, addr)
    VALUES
    ( %s, %s, %s , %s)
    """

cnt = cur.execute(sql , ("4","4","4","4"))
results = cur.fetchall()

print("cnt", cur.rowcount)  # 파이썬 계열에선 rowcount 계열을 쓸 것
conn.commit()
cur.close()
conn.close()