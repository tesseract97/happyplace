from libs.user import User
from libs.db import DBConnection

def initialize_user(name="tessa"):
    username = User(name)
    return username.user_to_json()
    

def test_connection(uri="mongodb://127.0.0.1:27018/"):
    conn= DBConnection(uri)
    conn.get_client()
    conn.get_users_collection()
    #conn.add_user(initialize_user())
    return conn.update_user(initialize_user())


if __name__ == '__main__':
    print(initialize_user())
    print(test_connection())
