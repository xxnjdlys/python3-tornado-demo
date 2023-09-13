from service import withMysql


def get_all_user():
    users = withMysql.get_all_user()
    if users:
        return users
    else:
        raise Exception("未查询到数据")


def get_user_by_id(user_id):
    users = withMysql.get_user_by_id(user_id)
    if users:
        return users[0]
    else:
        raise Exception("未查询到数据")
