import bcrypt

def hash_password(password):
    # 生成哈希值
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def verify_password(hashed_password, input_password):
    # 验证输入的密码是否与哈希值匹配
    return bcrypt.checkpw(input_password.encode('utf-8'), hashed_password)

# 示例用法
if __name__ == "__main__":
    # 假设这是从数据库或其他地方获取的哈希值
    stored_hashed_password = b'$2b$12$uNyb.B3srrCH3Hrck/mnDu92Rc/ARJMX7eyehhbz5fnmeFk5tRddi'

    # 用户输入的密码
    input_password = input("Enter your password: ")

    # 验证密码是否匹配
    if verify_password(stored_hashed_password, input_password):
        print("Password matched!")
    else:
        print("Password incorrect!")
