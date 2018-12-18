a_list = [("iphone","8000"),("mac book","9000"),("coffee","32"),("Python book","80"),("bicyle","1500")]
salary = input("how much money you have:")
shopping_car = []
if salary.isdigit():
    salary = int(salary)
    while True:
        for i,v in enumerate(a_list,1):
            print(i,v)
        choice = input("选择商品编号【退出：q】")
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(a_list):
                p_item = a_list[choice-1]
                if int(p_item[1]) < salary:
                    salary -= int(p_item[1])
                    shopping_car.append(p_item)
                else:
                    print("余额不足，还剩%s"%salary)
                print(p_item)
        elif choice =="q":
            print("------------您已购买以下商品-------------")
            for i in shopping_car:
                print(i)
            print("你还剩%s元钱"%salary)
            break
        else:
            print("invalid input")