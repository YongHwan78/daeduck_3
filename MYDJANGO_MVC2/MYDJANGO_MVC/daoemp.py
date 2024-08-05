'''
Created on 2024. 4. 17.

@author: PC-02
'''
import pymysql

class DaoEmp:
    def __init__(self): # JAVA에서 셍성자
        self.conn = pymysql.connect(host='127.0.0.1', user='root',
                                password='python', db='python', 
                                charset='utf8', port=3306)
        self.cur = self.conn.cursor( pymysql.cursors.DictCursor) # 튜플 형태로 준다 Dictionary Cursor --> JSON 과 같다.
        
    def selectList(self):
        sql = f"""select 
        e_id, e_name, gen, addr 
        from emp
        """

        cnt = self.cur.execute(sql)
        list = self.cur.fetchall()
        return list
    
    def selectOne(self, e_id):
        sql = f"""select 
        e_id, e_name, gen, addr 
        from emp where e_id= '{e_id}'
        """
        self.cur.execute(sql)
        list = self.cur.fetchone(); # 상위 배열 하나만을 리턴한다.
        return list
    def insert(self, e_id,e_name,gen,addr):
        sql = f"""INSERT INTO emp    
        (e_id, e_name, gen, addr)
        VALUES
        ( '{e_id}', '{e_name}', '{gen}' ,'{addr}')
        """
        cnt = self.cur.execute(sql)
        if cnt>0: 
            self.conn.commit()
        return cnt
    
    def insert2(self, e_id,e_name,gen,addr):
        sql = """INSERT INTO emp 
        (e_id, e_name, gen, addr)
        VALUES
        ( %s, %s, %s , %s)
        """
        
        var = (e_id,e_name,gen,addr)
        
        cnt = self.cur.execute(sql , var)
        self.conn.commit()
    
    def update(self, e_id,e_name,gen,addr):
        
        sql = f"""UPDATE emp SET 
             e_name = '{e_name}', addr='{addr}', gen='{gen}'
             WHERE e_id = '{e_id}'
            """
        
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    def delete(self, e_id):
        
        sql = f"""delete from emp 
             WHERE e_id = '{e_id}'
            """
        
        cnt = self.cur.execute(sql)
        self.conn.commit()
        return cnt
    
    
        
    def __del__(self):
        
        self.cur.close()
        self.conn.close()
    
if __name__ == '__main__':
    de = DaoEmp()    
    # list = de.selectList()
    # list2 = de.selectOne('1')
    # cnt = de.insert('3','3','3','3')
    # cnt2 = de.insert2('5','5','5','5')
    cnt2 = de.update('2','4','3','4')
    cnt3 = de.delete('1');
    # cnt3 = de.update2('3','2251','1525','1525')
    # print(list)
    # print(list2)
    # print(cnt) 
    print(cnt2) 
    # print(cnt3) 