# htyper text markup language 即超文本标记语言
# 超文本: 就是指页面内可以包含图片、链接，甚至音乐、程序等非文字元素。
# 标记语言: 标记（标签）构成的语言.
# 网页 == HTML文档，由浏览器解析，用来展示的
# 静态网页：静态的资源，如xxx.html                      html文档树形结构
# 动态网页：html代码是由某种开发语言根据用户请求动态生成的
# 标签是由一对尖括号包裹的单词构成，所有标签中的单词不可能以数字开头.标签不区分大小写.推荐使用小写.
# 标签分为两部分: 开始标签<a>和结束标签</a>. 两个标签之间的部分叫做标签体.标签可以嵌套.但不能交叉嵌套.
# 有些标签功能比较简单.使用一个标签即可.这种标签叫做自闭和标签.例如: <br/> <hr/> <input /> <img />
# 属性通常是以键值对形式出现的. 例如 name="alex"
# 属性只能出现在开始标签 或 自闭和标签中.
# 属性名字全部小写. *属性值必须使用双引号或单引号包裹 例如 name="alex"
# 如果属性值和属性名完全一样.直接写属性名即可. 例如 readonly
#
# 如果你的页面添加了<!DOCTYPE html>那么，那么就等同于开启了标准模式，那么浏览器就得老老实实的按照W3C
# 的标准解析渲染页面，这样一来，你的页面在所有的浏览器里显示的就都是一个样子了。
#
# head标签：
# <meta>标签的由两个属性http-equiv属性和name属性组成，不同的属性又有不同的参数值，实现了不同的网页功能。
# 1: name属性主要用于描述网页，与之对应的属性值为content，content中的内容主要是便于搜索引擎机器人查找信息
#     和分类信息用的。
# < meta name = "keywords" content = "meta总结,html meta,meta属性,meta跳转" >
# < meta name = "description" content = "老男孩培训机构是由一个老的男孩创建的" >
# 2: http-equiv顾名思义，相当于http的文件头作用，它可以向浏览器传回一些有用的信息，以帮助正确和精确地显示
#     网页内容，与之对应的属性值为content，content中的内容其实就是各个参数的变量值。
# <meta http-equiv="Refresh" content="2;URL=https://www.baidu.com"> //(注意后面的引号，分别在秒数的前面和网址的后面)
# <meta http-equiv="content-Type" charset=UTF8">
# <meta http-equiv = "X-UA-Compatible" content = "IE=EmulateIE7" />
# 非meta标签：
# < title > oldboy < / title >
# < link rel = "icon" href = "http://www.jd.com/favicon.ico" >
# < link rel = "stylesheet" href = "css.css" >
# < script src = "hello.js" > < / script >　
#
# body标签：
# <hn>: n的取值范围是1~6; 从大到小. 用来表示标题.
# <p>: 段落标签. 包裹的内容被换行.并且也上下内容之间有一行空白.
# <b> <strong>: 加粗标签.
# <strike>: 为文字加上一条中线.
# <em>: 文字变成斜体.
# <sup>和<sub>: 上角标 和 下角表.
# <br>:换行.
# <hr>:水平线
# <div><span>
# 块级标签：<p><h1><table><ol><ul><form><div>
# 内联标签：<a><input><img><sub><sup><textarea><span>
# block（块）元素:总是在新行上开始；宽度缺省是它的容器的100%，除非设定一个宽度。它可以容纳内联元素和其他块元素
# inline元素:和其他元素都在一行上；宽度就是它的文字或图片的宽度，不可改变内联元素只能容纳文本或者其他内联元素
# 特殊字符: &lt; &gt；&quot；&copy;&reg;
# 1.图形标签: <img>
# src: 要显示图片的路径.
# alt: 图片没有加载成功时的提示.
# title: 鼠标悬浮时的提示信息.
# width: 图片的宽
# height:图片的高 (宽高两个属性只用一个会自动等比缩放.)
# 2.超链接标签(锚标签)<a>
# href:要连接的资源路径 格式如下: href="http://www.baidu.com"
# target: _blank : 在新的窗口打开超链接. 框架名称: 在指定框架中打开连接内容.
# name: 定义一个页面的书签.
# 用于跳转 href : #id.（锚）
# 3.列表标签：
# <ul>: 无序列表
# <ol>: 有序列表
#          <li>:列表中的每一项.
# <dl>  定义列表
#          <dt> 列表标题
#          <dd> 列表项
# 4.表格标签: <table>
# border: 表格边框.
# cellpadding: 内边距
# cellspacing: 外边距.
# width: 像素 百分比.（最好通过css来设置长宽）
# <tr>: table row
#          <th>: table head cell
#          <td>: table data cell
# rowspan:  单元格竖跨多少行
# colspan:  单元格横跨多少列（即合并单元格）
# <th>: table header <tbody>(不常用): 为表格进行分区.
# 5.表单标签<form>
# 表单用于向服务器传输数据。表单能够包含 input 元素，比如文本字段、复选框、单选框、提交按钮等等。表单还可以
#     包含textarea、select、fieldset和 label 元素。
# 表单属性
#     action: 表单提交到哪. 一般指向服务器端一个程序,程序接收到表单提交过来的数据（即表单元素值）作相应处理，比如https://www.sogou.com/web
#     method: 表单的提交方式 post/get 默认取值 就是 get（信封）
#                           get: 1.提交的键值对.放在地址栏中url后面. 2.安全性相对较差. 3.对提交内容的长度有限制.
#                           post:1.提交的键值对 不在地址栏. 2.安全性相对较高. 3.对提交内容的长度理论上无限制.
#                           get/post是常见的两种请求方式.    都不太安全
#表单元素
#       <input>  标签的属性和对应值
#                 type:    text       文本输入框
#                          password   密码输入框
#                          radio      单选框
#                          checkbox   多选框
#                          submit     提交按钮
#                          button     按钮(需要配合js使用.) button和submit的区别？
#                          file       提交文件：form表单需要加上属性enctype="multipart/form-data"
#                 name: 表单提交项的键.注意和id属性的区别：name属性是和服务器通信时使用的名称；而id属性是浏览器端
#                     使用的名称，该属性主要是为了方便客户端编程，而在css和javascript中使用的
#                 value: 表单提交项的值.对于不同的输入类型，value属性的用法也不同：
#                             checked:  radio 和 checkbox 默认被选中
#                             readonly: 只读. text 和 password
#                             disabled: 对所用input都好使.
#        上传文件注意两点：1 请求方式必须是post  2 enctype="multipart/form-data"
#       <select> 下拉选标签属性
#                 name: 表单提交项的键.
#                 size：选项个数multiple：multiple
#                 < option > 下拉选中的每一项属性：
#                             value: 表单提交项的值.selected: selected下拉选默认被选中\
#                                       < optgroup > 为每一项加上分组
#       <textarea> 文本域
#                 name:    表单提交项的键.
#                 cols:    文本域默认有多少列
#                 rows:    文本域默认有多少行
#         <label>
#               <label for="www">姓名</label>
#               <input id="www" type="text">
#         <fieldset>
#                 <fieldset>
#                     <legend>登录吧</legend>
#                     <input type="text">
#                 </fieldset>