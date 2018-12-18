# CSS是Cascading Style Sheets的简称，中文称为层叠样式表，用来控制网页数据的表现，可以使网页的表现与数据内容分离。
#
# 清除浮动(脱离文档流的影响)： .clearfix: after{
#                                     content: '.';
#                                     display: block;
#                                     clear: both;
#                                     visibility: hidden;
#                                     height: 0;
#                              }
#
# CSS四种引入方式：
#     链接式：<link href="文件位置例如：mystyle.css" rel="stylesheet" type="text/css"/>
#     行内式：
#     嵌入式：
#     导入式：  <style>标记也是写在<head>标记中
#         <style type="text/css">
#             @import"mystyle.css"; 此处要注意.css文件的路径
#         </style>　
# 导入式会在整个网页装载完后再装载CSS文件，因此这就导致了一个问题，如果网页比较大则会儿出现先显示无样式的页面，
# 闪烁一下之后，再出现网页的样式。这是导入式固有的一个缺陷。使用链接式时与导入式不同的是它会以网页文件主体装载
# 前装载CSS文件，因此显示出来的网页从一开始就是带样式的效果的
#
# CSS的选择器（Selector）： “选择器”指明了{}中的“样式”的作用对象，也就是“样式”作用于网页中的哪些元素
# 1 基础选择器
# ＊ ：          通用元素选择器，匹配任何元素                     * { margin:0; padding:0; }
# E  ：          标签选择器，匹配所有使用E标签的元素              p { color:green; }
# .info和E.info: class选择器，匹配所有class属性中包含info的元素   .info { background:#ff0; }    p.info { background:blue; }
# #info和E#info  id选择器，匹配所有id属性等于footer的元素         #info { background:#ff0; }   p#info { background:#ff0; }
# 2 组合选择器
# E, F         多元素选择器，同时匹配所有E元素或F元素，E和F之间用逗号分隔div, p{color:  # f00; }
# 注意嵌套规则：
#     块级元素可以包含内联元素或某些块级元素，但内联元素不能包含块级元素，它只能包含其它内联元素。
#     有几个特殊的块级元素只能包含内联元素，不能包含块级元素。如h1,h2,h3,h4,h5,h6,p,dt
#     li内可以包含div
#     块级元素与块级元素并列、内联元素与内联元素并列
# 3 属性选择器
# E[att]         匹配所有具有att属性的E元素，不考虑它的值。（注意：E在此处可以省略，比如“[cheacked]”。以下同。）   p[title] { color:#f00; }
# E[att=val]     匹配所有att属性等于“val”的E元素   div[class=”error”] { color:#f00; }
# E[att~= val]    匹配所有att属性具有多个空格分隔的值、其中一个值等于“val”的E元素   td[class~=”name”] { color:#f00; }
# E[attr ^= val]    匹配属性值以指定值开头的每个元素    div[class^="test"]{background:#ffff00;}
# E[attr$=val]    匹配属性值以指定值结尾的每个元素      div[class$="test"]{background:#ffff00;}
# E[attr *= val]    匹配属性值中包含指定值的每个元素    div[class*="test"]{background:#ffff00;}
# 4 伪类(Pseudo - classes)
# CSS伪类是用来给选择器添加一些特殊效果。
# anchor伪类：专用于控制链接的显示效果
# a:link（没有接触过的链接）,用于定义了链接的常规状态。
# a:hover（鼠标放在链接上的状态）,用于产生视觉效果。
# a:visited（访问过的链接）,用于阅读文章，能清楚的判断已经访问过的链接。
# a:active（在链接上按下鼠标时的状态）,用于表现鼠标按下时的链接状态。
# 伪类选择器 : 伪类指的是标签的不同状态:
#            a ==> 点过状态 没有点过的状态 鼠标悬浮状态 激活状态
# a:link {color: #FF0000} /* 未访问的链接 */
# a:visited {color: #00FF00} /* 已访问的链接 */
# a:hover {color: #FF00FF} /* 鼠标移动到链接上 */
# a:active {color: #0000FF} /* 选定的链接 */ 格式: 标签:伪类名称{ css代码; }
# 补充：         .outer:hover .right{color: red}
#     before after伪类 ：
#         :before    p:before       在每个<p>元素之前插入内容
#         :after     p:after        在每个<p>元素之后插入内容
#         p:before    在每个 <p> 元素的内容之前插入内容        p:before{content:"hello";color:red}
#         p:after     在每个 <p> 元素的内容之前插入内容        p:after{ content:"hello"；color:red}
# 5 css优先级和继承
# CSS优先级:
#     所谓CSS优先级，即是指CSS样式在浏览器中被解析的先后顺序。
#     样式表中的特殊性描述了不同规则的相对权重，它的基本规则是：
#           1 内联样式表的权值最高       style=""-------------------1000；
#     　　  2 统计选择符中的ID属性个数。    #id    －－－－－－－－－－－－－100
#     　　  3 统计选择符中的CLASS属性个数。 .class  －－－－－－－－－－－－－10
#           4 统计选择符中的HTML标签名个数。     p     －－－－－－－－－－－－－-1
#     按这些规则将数字符串逐位相加，就得到最终的权重，然后在比较取舍时按照从左到右的顺序逐位比较。
# CSS的继承性:        有一些属性不能被继承，如：border, margin, padding, background等。
# 继承是CSS的一个主要特征，它是依赖于祖先 - 后代的关系的。
# 继承是一种机制，它允许样式不仅可以应用于某个特定的元素，还可以应用于它的后代。例如一个BODY定义了的颜色值也会应用到段落的文本中。
# 然而CSS继承性的权重是非常低的，是比普通元素的权重还要低的0。任何显示申明的规则都可以覆盖其继承样式。　
# 附加说明:
#     1、文内的样式优先级为1,0,0,0，所以始终高于外部定义。这里文内样式指形如<div style="color:red>blah</div>的样式，而外部定义指经由<link>或<style>卷标定义的规则。
# 　　2、有!important声明的规则高于一切。
# 　　3、如果!important声明冲突，则比较优先权。
# 　　4、如果优先权一样，则按照在源码中出现的顺序决定，后来者居上。
# 　　5、由继承而得到的样式没有specificity的计算，它低于一切其它规则(比如全局选择符*定义的规则)。
#
# CSS的常用属性:
# 1  颜色属性      <div style="color:blueviolet">ppppp</div>
# 2  字体属性      <h1 style="font-style: oblique">老男孩</h1>
# font-size: 20px/50%/larger
# font-family:'Lucida Bright'
# font-weight: lighter/bold/border/
# 3  背景属性
# background-color: cornflowerblue
# background-image: url('1.jpg');
# background-repeat: no-repeat;(repeat:平铺满)
# background-position: right top（20px 20px）;(横向：left center right)(纵向：top center bottom)
# 注意：如果将背景属性加在body上，要记得给body加上一个height，否则结果异常，这是因为body为空，
#       无法撑起背景图片；另外，如果此时要设置一个width＝100px，你也看不出效果，除非你设置出html。
# 4  文本属性
# font-size: 10px;
# text-align: center;   横向排列
# line-height: 200px;   文本行高 通俗的讲，文字高度加上文字上下的空白区域的高度 50%:基于字体大小的百分比
# vertical-align:－4px  设置元素内容的垂直对齐方式 ,只对行内元素有效，对块级元素无效
# text-indent: 150px;   首行缩进
# letter-spacing: 10px;
# word-spacing: 20px;
# text-transform: capitalize;
# 5   边框属性
# border-style: solid;
# border-color: chartreuse;
# border-width: 20px;
# 简写：border: 30px rebeccapurple solid;
# 6   列表属性
# ul,ol{   list-style: decimal-leading-zero;
#          list-style: none; <br>         list-style: circle;
#          list-style: upper-alpha;
#          list-style: disc; }
# 7  dispaly属性
# none
# block
# inline
# display:inline-block可做列表布局，其中的类似于图片间的间隙小bug可以通过如下设置解决：
# #outer{
#             border: 3px dashed;
#             word-spacing: -5px;
#         }
# 8  外边距和内边
# margin:            用于控制元素与元素之间的距离；margin的最基本用途就是控制元素周围空间的间隔，从视觉角度上达到相互隔开的目的。
# padding:           用于控制内容与边框之间的距离；
# Border(边框)       围绕在内边距和内容外的边框。
# Content(内容)      盒子的内容，显示文本和图像。
# 元素的宽度和高度:
# 重要: 当您指定一个CSS元素的宽度和高度属性时，你只是设置内容区域的宽度和高度。要知道，完全大小的元素，你还必须添加填充，边框和边距。.
# margin:10px 5px 15px 20px;-----------上 右 下 左
# margin:10px 5px 15px;----------------上 右左 下
# margin:10px 5px;---------------------上下  右左
# margin:10px;    ---------------------上右下左
# body本身也是一个盒子（外层还有html），在默认情况下，   body距离html会有若干像素的margin，具体数值因各个浏览器不尽相同，所以body中的盒子不会紧贴浏览器窗口的边框
# margin collapse（边界塌陷或者说边界重叠）:
#     外边距的重叠只产生在普通流文档的上下外边距之间，这个看起来有点奇怪的规则，其实有其现实意义。
#     设想，当我们上下排列一系列规则的块级元素（如段落P）时，那么块元素之间因为外边距重叠的存在，段落之间就不会产生双倍的距离。
#     1兄弟div：上面div的margin - bottom和下面div的margin - top会塌陷，也就是会取上下两者margin里最大值作为显示值
#     2父子div: if 父级div中没有border，padding，inline content，子级div的margin会一直向上找，直到找到某个标签包括border，padding，inline content 中的其中一个，然后按此div 进行margin ；
#      解决方法：
#         border:1px solid transparent
#         padding:1px
#         over-flow:hidden;
