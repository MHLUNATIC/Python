menu = {
        '北京': {
            '朝阳': {
                '国贸':{
                    'CICC':{},
                    "HP":{},
                    'CCTV':{}
                },
                '望京':{
                    '默默':{},
                    "奔驰":{},
                    '360':{}
                },
                '三里屯':{
                    '优衣库':{},
                    "apple":{},
                }
            },
            '昌平': {
                '沙河':{
                    '老男孩':{},
                    '阿泰包子':{}
                },
                '天通苑':{
                    '链家': {},
                    '我爱我家': {}
                },
                "回龙观":{},
                },
            '海淀':{
                '五道口':{
                    '谷歌':{},
                    '网易':{},
                    '搜狐':{},
                    'shougou':{},
                },
                '中关村':{
                    'youku':{},
                    '汽车之家':{},
                }
            }

        },
        '上海':{},
        '山东':{}
    }
layer = menu
flayer = []
while True:
    for i in layer:
        print(i)
    choice = input('输入').strip()
    if len(choice) == 0:continue
    if choice in layer:
        flayer.append(layer)
        layer = layer[choice]
    elif choice == "b":
        if flayer:
            layer = flayer.pop()
    elif choice == "p":
        break
    else:
        print('无此项')