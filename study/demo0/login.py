# user = "abc"
# key = "123"
#
# for i in range(3):
#     user_name = input("user_name:")
#     password = input("password:")
#     if user_name ==user and password == key:
#         print("welcome %s login..."%user)
#         break
#     else:
#         print("invalid user_name or password")
# else:
#     print("密码输入次数过多")

user = "abc"
key = "123"
counter = 0
while counter < 3:
    user_name = input("user_name:")
    password = input("password:")
    if user_name ==user and password == key:
        print("welcome %s login..."%user)
        break
    else:
        print("invalid user_name or password")
    counter += 1
    if counter == 3:
        keep_going_choice = input("do you want to login?[y/n]")
        if keep_going_choice == "y":
            counter = 0
else:
    print("密码输入次数过多")