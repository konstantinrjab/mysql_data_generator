```bash
docker run --name mysql -v mysql_data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=dev -e MYSQL_USER=user -e MYSQL_PASSWORD=123123 -p 3306:3306 mysql
```

https://www.a2hosting.com/kb/developer-corner/mysql/enabling-the-slow-query-log-in-mysql

SET GLOBAL slow_query_log = 'ON';
SET GLOBAL long_query_time = 1;
SELECT SLEEP(X);

docker cp mysql:/var/lib/mysql/0f7e3e851dad-slow.log D:\