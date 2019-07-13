class DatabaseCreator:
    def __init__(self, mysql_connection):
        self.__mysql_connection = mysql_connection

    def create_db_structure(self):
        cursor = self.__mysql_connection.cursor()
        cursor.execute("CREATE TABLE tag (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
        cursor.execute("CREATE TABLE article_tag (id INT AUTO_INCREMENT PRIMARY KEY, tag_id INT, article_id INT)")
        cursor.execute("CREATE TABLE article (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), text TEXT)")
        cursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))")
        cursor.execute(
            "CREATE TABLE comment (id INT AUTO_INCREMENT PRIMARY KEY, article_id INT, user_id VARCHAR(255), text VARCHAR(255))")
