# Python使用使用中括号 [ ] 来解析列表。列表是可变的（mutable）——可以改变列表的内容。
# a=["sdd",'231',"334"]    a=list(("sdd",'231',"334"))                            索引，切片
# 查（［］） a[1:] null表示取到最后   a[0:-1] 取到倒数第二个值为止
# 增（append，insert）  a.append('d')  a.insert(1,'s')在索引位置为1的地方插入s
# 改（重新赋值）          insert 方法用于将对象插入到列表中，而append方法则用于在列表末尾追加新的对象
# 删（remove，del，pop） a.remove()填要删的值   del a[2]  也可删列表 del a     a.clear() 清空列表
#                        a.pop()是有一个返回值的 默认删最后一个 也可以添加索引选择删除
# count 方法统计某个元素在列表中出现的次数                          a.count("231")
# extend 方法可以在列表的末尾一次性追加另一个序列中的多个值。       a.extend(b)
# index 方法用于从列表中找出(从左到右)某个值第一个匹配项的索引位置：a.index("231")　
# reverse 方法将列表中的元素反向存放。                              a.reverse()
# sort 方法用于在原位置对列表进行排序。   按种类类型                a.sort()
#
# 不可变数据类型:数字,字符串,元组    可变类型:列表,字典            type(a) is list

# 深浅拷贝：(可变类型:列表,字典)
# 浅：只拷贝第一层    数据间存在联系
# 深：克隆一份        数据相互独立
# 浅-------------------------------------------------------------------------
# a=[['dsd','11'],'231',"334"]
# b=a.copy()      #拷贝的是列表内元素的内存地址（第一个元素内存地址是小列表的内存地址）
# b[0][1]=1111111
# b[2]=222222
# print(b)            #[['dsd', 1111111], '231', 222222]
# print(a)            #[['dsd', 1111111], '231', '334']
# 浅-------------------------------------------------------------------------
# a = [['dsd', '11'], '231', "334"]
# b=a               #拷贝的是a列表的内存地址
# b[0][1]=1111111
# b[2]=222222
# print(b)          [['dsd', 1111111], '231', 222222]
# print(a)          [['dsd', 1111111], '231', 222222]
# 深-------------------------------------------------------------------------
# a=[['dsd','11'],'231',"334"]
# import copy
# b=copy.deepcopy(a)
# b[0][1]=1111111
# print(b)            [['dsd', 1111111], '231', '334']
# print(a)            [['dsd', '11'], '231', '334']

