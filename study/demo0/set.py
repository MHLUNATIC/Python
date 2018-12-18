# 集合是一个无序的，不重复的数据组合，它的主要作用如下：
# 去重，把一个列表变成集合，就自动去重了
# 关系测试，测试两组数据之前的交集、差集、并集等关系
# 集合对象是一组无序排列的可哈希的值：集合成员可以做字典的键
# 集合分类：可变集合、不可变集合
# 可变集合(set)：可添加和删除元素，非可哈希的，不能用作字典的键，也不能做其他集合的元素
# 不可变集合(frozenset)：与上面恰恰相反
# s1 = set('alvin')
# s2 = frozenset('yuan')
# print(s1,type(s1))  #{'l', 'v', 'i', 'a', 'n'} <class 'set'>
# print(s2,type(s2))  #frozenset({'n', 'y', 'a', 'u'}) <class 'frozenset'>
# 由于集合本身是无序的，所以不能为集合创建索引或切片操作，只能循环遍历或使用in、not in来访问或判断集合元素。
# 可使用以下内建方法来更新：          只有可变集合才能更新
# a.add()               添加一个元素
# a.update("abc")       把"abc"每一个元素"a","b","c"加到s集合中
# a.update([12,"sd"])   把"12","sd"加到s集合中
# a.remove()            删除
# a.pop()               随机删一个元素
# a.clear()             清空集合
# del a                 删除集合本身　
# 集合类型操作符　
# in ,not in
# 集合等价与不等价(==, !=)
# 子集：a.issubset(t)       或   a <= b
# 超集：a.issuperset(t)     或   a >= b
# 交集: a.intersection(b)    或  a & b
# 并集：a.union(b)          或   a | b
# 差集：a.difference(b)     或   a - b   在a不在b中
# 对称差集：a.symmetric_difference(b)  或   a^ b     除a，b共有元素之外的所有元素
# a.copy()  返回 set“a”的一个浅复制
# len(a)    set的长度
