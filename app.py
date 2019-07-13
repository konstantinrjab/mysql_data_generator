import mysql.connector
from Filler import Filler
from DatabaseCreator import DatabaseCreator
import time

mysql_connection = mysql.connector.connect(
    user='user', password='123123',
    host='127.0.0.1',
    auth_plugin='mysql_native_password',
    database='dev'
)

DatabaseCreator(mysql_connection).create_db_structure()
filler = Filler(mysql_connection)

articles_count = 1000
comments_count = 10000
tags_count = 1000
users_count = 1000

filler.fill_tags(tags_count)
filler.fill_article(articles_count)
filler.fill_user(users_count)
filler.fill_comment(comments_count, articles_count, users_count)
filler.fill_article_tag(articles_count, tags_count)





# roughly check execution time
# my_database = mysql_connection.cursor()
# sql_query = 'select * from user join comment on user.id = comment.user_id join article on article.id = comment.article_id join article_tag on article_tag.id = article_tag.id join tag on tag.id = article_tag.id limit 100000;'
#
# start_time = int(round(time.time() * 1000))
# my_database.execute(sql_query)
# output = my_database.fetchall()
# finish_time = int(round(time.time() * 1000))
#
# print(finish_time - start_time)
