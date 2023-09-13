import pymysql

from datetime import datetime

from config import CONFIG


def connect_mysql(func):
    def wrapper(*args, **kwargs):
        dbInfo = CONFIG['mysql']
        conn = pymysql.connect(host=dbInfo['host'], port=int(dbInfo['port']), user=dbInfo['user'],
                               passwd=dbInfo['passwd'], db=dbInfo['db'], charset="utf8")
        result = func(conn, *args, **kwargs)
        conn.close()
        return result

    return wrapper


@connect_mysql
def fetchall(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    rst = cursor.fetchall()
    cursor.close()
    return rst


@connect_mysql
def fetchallToTable(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    rst = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    cursor.close()
    results = []
    for row in rst:
        row_dict = dict(zip(columns, row))
        # 处理datetime类型
        for key, value in row_dict.items():
            if isinstance(value, datetime):
                row_dict[key] = value.strftime('%Y-%m-%d %H:%M:%S')
        results.append(row_dict)
    return results


@connect_mysql
def executeInsert(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    lastId = cursor.lastrowid
    conn.commit()
    cursor.close()
    return lastId


@connect_mysql
def executeUpdate(conn, query, params=()):
    cursor = conn.cursor()
    cursor.execute(query, params)
    conn.commit()
    cursor.close()
