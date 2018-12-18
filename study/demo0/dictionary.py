# 字典是python中唯一的映射类型，采用键值对（key-value）的形式存储数据。python对key进行哈希函数运算，根据
# 计算的结果决定value的存储地址，所以字典是无序存储的，且key必须是可哈希的。可哈希表示key必须是不可变类型
# 列表是有序的对象结合，字典是无序的对象集合。两者之间的区别在于：字典当中的元素是通过键来存取的，
# 而不是通过偏移存取。          无序，key必须是唯一的,天生去重
# a={'name':'alex','age':36,'sex':'male'}         a=dict((('name','alex'),))
# 增：a['name'] ='sds'健存在则改变值
# a.setdefault('name','alex') 有返回值 健存在不改变值返回字典原值 健不存在增加新键值对并返回相应的值
# 查：通过键来查找a['name']      a.items()查所有的键值对  a.keys()查所有的键   a.values()查所有的值
# 改： a['name'] ='ddd'  a.update(b)将字典b中的更新加到字典a中
# 删： del a['name']   a.clear() 清空字典  del a  删除字典   a.pop('name')
#        a.popitem() 随机删除一组键值对并会回相应的键值对
# a..fromkeys((所有的键),统一值)   将所有的键对应的值都改成同一个值
# sorted(a) 返回一个有序的包含字典所有键的列表(根据键进行排序)
# for循环遍历字典时拿到的是键          字典的嵌套
# 格式化输出的另一种方式：st="hello{name}is{age}"  --->  st.format(name="eeeew",age=37)