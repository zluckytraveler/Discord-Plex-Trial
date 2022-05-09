import sqlite3

class DB:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()
        self.create_table()
        
    def create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 email TEXT UNIQUE,
                 trial_end TEXT,
                 ended BOOLEAN DEFAULT 0
                 )"""
        self.cur.execute(sql)
        self.conn.commit()
        
    def insert(self, id, name, email, trial_end):
        sql = """INSERT INTO users (id, name, email, trial_end)
                 VALUES (?, ?, ?, ?)"""
        self.cur.execute(sql, (id, name, email, trial_end))
        self.conn.commit()
        
    def update_user(self, id, name, email, trial_end, ended):
        sql = """UPDATE users SET name = ?, email = ?, trial_end = ?, ended = ? WHERE id = ?"""
        self.cur.execute(sql, (name, email, trial_end, ended, id))
        self.conn.commit()
    
    def get_user(self, id):
        sql = """SELECT * FROM users WHERE id = ?"""
        self.cur.execute(sql, (id,))
        return self.cur.fetchone()
    
    def get_all_users(self):
        sql = """SELECT * FROM users"""
        self.cur.execute(sql)
        return self.cur.fetchall()
    
    def remove_user(self, id):
        sql = """DELETE FROM users WHERE id = ?"""
        self.cur.execute(sql, (id,))
        self.conn.commit()