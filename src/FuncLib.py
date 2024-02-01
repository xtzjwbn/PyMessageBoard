import uuid


def getUniqueUUID(cursor, table_name):
    current_uuid_result = cursor.execute('''select UUID from '''+table_name).fetchall()
    while True:
        user_uuid = uuid.uuid1().hex
        flag = False
        for current_uuid in current_uuid_result:
            if user_uuid == current_uuid[0]:
                flag = True
                break
        if not flag:
            return user_uuid
