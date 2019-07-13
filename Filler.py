import uuid
from faker import Faker
import random


class Filler():
    def __init__(self, mysql_connection):
        self.__connection = mysql_connection
        self.__cursor = mysql_connection.cursor()

    def fill_tags(self, count):
        while count > 0:
            sql = "INSERT INTO tag(name) VALUES (%s)"
            self.__cursor.execute(sql, (str(uuid.uuid4()),))
            self.__connection.commit()
            count -= 1

    def fill_article(self, count):
        faker = Faker()
        while count > 0:
            sql = "INSERT INTO article(name, text) VALUES (%s, %s)"
            self.__cursor.execute(sql, (faker.sentence(), faker.text(),))
            self.__connection.commit()
            count -= 1

    def fill_user(self, count):
        faker = Faker()
        while count > 0:
            sql = "INSERT INTO user(name) VALUES (%s)"
            self.__cursor.execute(sql, (faker.name(),))
            self.__connection.commit()
            count -= 1

    def fill_comment(self, comments_count, articles_count, users_count):
        faker = Faker()
        while comments_count > 0:
            sql = "INSERT INTO comment(article_id, text, user_id) VALUES (%s, %s, %s)"
            article_id = random.randint(1, articles_count)
            user_id = random.randint(1, users_count)
            self.__cursor.execute(sql, (article_id, faker.text(), user_id,))
            self.__connection.commit()
            comments_count -= 1

    def fill_article_tag(self, articles_count, tags_count):
        count = (articles_count + tags_count) * 2
        while count > 0:
            sql = "INSERT INTO article_tag(article_id, tag_id) VALUES (%s, %s)"
            article_id = random.randint(1, articles_count)
            tag_id = random.randint(1, tags_count)
            self.__cursor.execute(sql, (article_id, tag_id,))
            self.__connection.commit()
            count -= 1
