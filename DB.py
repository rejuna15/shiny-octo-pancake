import pymysql

HOST='localhost'
USER='root'
PWD='admin'
PORT=3306
DB_NAME='shorturl'

class DB():
    def __init__(self):
        self.con = pymysql.connect(host=HOST,
                                   user=USER,
                                   password=PWD,
                                   port=PORT,
                                   db=DB_NAME, autocommit=True)

    def cursor(self):
        cursor = self.con.cursor()
        return cursor

    def createTable(self):
        self.cursor().execute(f"CREATE TABLE `urls` ( "
                              f"`id` int(10) unsigned NOT NULL AUTO_INCREMENT,"
                              f"`long_url` longtext DEFAULT NULL, "
                              f"`short_url` varchar(50) DEFAULT NULL, "
                              f"PRIMARY KEY (`id`) "
                              f") ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;")
        self.con.close()
