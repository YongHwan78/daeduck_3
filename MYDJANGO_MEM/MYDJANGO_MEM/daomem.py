from telnetlib import DM
import pymysql


class DaoMem:

    def __init__(self):  # JAVA에서 셍성자
        self.conn = pymysql.connect(host='127.0.0.1', user='root',
                                password='python', db='python', 
                                charset='utf8', port=3305)
        self.cur = self.conn.cursor( pymysql.cursors.DictCursor)
        
        
    def selectList(self):
        sql = f"""select 
        m_id, m_name, tel, email 
        from mem
        """
        cnt = self.cur.execute(sql)
        list = self.cur.fetchall()
        return list;
    
    def selectOne(self, m_id):
        sql = f"""select 
        m_id, m_name, tel, email 
        from mem where m_id = %s
        """
        var = (m_id)
        self.cur.execute(sql , var)
        
        vo = self.cur.fetchone();
        return vo;
    def insert(self, m_id, m_name, tel, email):
        sql = f"""insert into mem 
        (m_id, m_name, tel, email) 
        values (%s,%s,%s,%s)
        """
        var = (m_id, m_name, tel, email )
        cnt = self.cur.execute(sql , var)
        # cnt = self.cur.row_count();
        if cnt > 0 :
            self.conn.commit()
        
        return cnt;
    def update(self, m_id, m_name, tel, email):
        sql = f"""update mem set 
        m_name = '{m_name}' , tel = '{tel}' , email= '{email}'
        where m_id = '{m_id}'
        """
        cnt = self.cur.execute(sql)
        
        # cnt = self.cur.row_count();
        if cnt > 0 :
            self.conn.commit()
        
        return cnt;
    def delete(self, m_id):
        sql = f"""delete from mem 
                 WHERE m_id = '{m_id}'
            """
        cnt = self.cur.execute(sql)
        
        # cnt = self.cur.row_count();
        if cnt > 0 :
            self.conn.commit()
        
        return cnt;
    
    def check(self, m_id):
        sql = f""" select count(m_id) from mem
            where m_id = '{m_id}'
            """
        self.cur.execute(sql)
        check = self.cur.fetchone();
        
        return check;
    
    def __del__(self):
        self.conn.close()
        self.cur.close()
    
if __name__ == '__main__':
    dm = DaoMem()
    list =dm.selectList();
    # print("list", list)
    # vo =dm.selectOne('1');
    # print("vo", vo)
    #
    # # cnt = dm.insert('4','4','4','4')
    # # print("cnt", cnt)
    # cnt = dm.update('4', '6', '6', '6')
    # print("cnt", cnt)
    # cnt = dm.delete('1')
    # print("cnt". cnt)