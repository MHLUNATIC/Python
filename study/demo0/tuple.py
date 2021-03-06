# 元组被称为只读列表，即数据可以被查询，但不能被修改，所以，列表的切片操作同样适用于元组。
# 元组写在小括号(())里，元素之间用逗号隔开。
# 虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
# tup1 = ()      # 空元组
# tup2 = (20,)   # 一个元素，需要在元素后添加逗号
# 它只有2个方法，一个是count,一个是index
# 1 对于一些数据我们不想被修改，可以使用元组；
# 2 另外，元组的意义还在于，元组可以在映射（和集合的成员）中当作键使用——而列表则不行；
#        元组作为很多内建函数和方法的返回值存在