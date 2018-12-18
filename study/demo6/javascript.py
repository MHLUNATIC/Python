字符串转化成数字类型失效时出现NaN,NaN是number的一个类型
NaN参与的所有的运算都是false,，除了不等于（NaN != 0）时

Math是一个内置对象，拿来就用，不需要new一下

将a标签自身功能阉割(不发生跳转和href=‘#’功能相似) <a href ="javascript:void()" onclick=func1(this)>d</a>
this 指向方法的调用者，在当前例子中了a标签(在页面中点击“d”就会获得a标签)

window.onload