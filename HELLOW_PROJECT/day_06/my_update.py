'''
Created on 2024. 4. 24.

@author: PC-02
'''
import pymysql


conn = pymysql.connect(host='127.0.0.1', user='root', password='python', db='python', charset='utf8', port=3305)

e_id = "6"
e_name = "3"
gen = "2"
addr = "4"
# pymysql.cursors.DictCursor
cur = conn.cursor( pymysql.cursors.DictCursor) # 튜플 형태로 준다 Dictionary Cursor --> JSON 과 같다.

sql = f"""UPDATE emp SET 
     e_name = {e_name}, addr={addr}, gen={gen}
     WHERE e_id = {e_id}; 
    """

cnt = cur.execute(sql)
results = cur.fetchall()

print("cnt", cur.rowcount)  # 파이썬 계열에선 rowcount 계열을 쓸 것
conn.commit()
cur.close()
conn.close()