import dbconfig

class MysqlController:
    def __init__(self, host, id, pw, db_name):
        self.conn = dbconfig.connect(host=host, user=id, password=pw, db=db_name, charset='utf8')
        self.curs = self.conn.cursor()

    def insert_enterprise(self, enterprise):
        sql = 'INSERT INTO seramin (enterprise) VALUES (%s)'
        self.curs.execute(sql,(enterprise))
        self.conn.commit()