from common import mysqlService


def get_all_user():
    return mysqlService.fetchallToTable("select id,name,create_time from `python-test`")


def get_user_by_id(user_id):
    return mysqlService.fetchallToTable("select id,name,create_time from `python-test` where id = %s", (user_id))
