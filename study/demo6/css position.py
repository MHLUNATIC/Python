# position(定位):
# 1 static
# static 默认值，无定位，不能当作绝对定位的参照物，并且设置标签对象的left、top等值是不起作用的的。
# 2  position: relative／absolute
# relative 相对定位:相对定位是相对于该元素在文档流中的原始位置，即以自己原始位置为参照物。有趣的是，即使设定
#     了元素的相对定位以及偏移值，元素还占有着原来的位置，即占据文档流空间。对象遵循正常文档流，但将依据top，
#     right，bottom，left等属性在正常文档流中偏移位置。而其层叠通过z-index属性定义。
# 注意：position：relative的一个主要用法：方便绝对定位元素找到参照物。
# absolute绝对定位定义：设置为绝对定位的元素框从文档流完全删除，并相对于最近的已定位祖先元素定位，如果元素
#     没有已定位的祖先元素，那么它的位置相对于最初的包含块（即body元素）。元素原先在正常文档流中所占的空间会
#     关闭，就好像该元素原来不存在一样。元素定位后生成一个块级框，而不论原来它在正常流中生成何种类型的框。
# 重点：如果父级设置了position属性，例如position:relative;，那么子元素就会以父级的左上角为原始点进行定位。
#     这样能很好的解决自适应网站的标签偏离问题，即父级为自适应的，那我子元素就设置position:absolute;父元素设
#     置position:relative;，然后Top、Right、Bottom、Left用百分比宽度表示。
#     另外，对象脱离正常文档流，使用top，right，bottom，left等属性进行绝对定位。而其层叠通过z-index属性定义。
# 总结：参照物用相对定位，子元素用绝对定位，并且保证相对定位参照物不会偏移即可。
# 3  position:fixed
# fixed：对象脱离正常文档流，使用top，right，bottom，left等属性以窗口为参考点进行定位，当出现滚动条时，对象
#     不会随着滚动。而其层叠通过z-index属性 定义。 注意点： 一个元素若设置了 position:absolute | fixed; 则该
#     元素就不能设置float。这 是一个常识性的知识点，因为这是两个不同的流，一个是浮动流，另一个是“定位流”。
#     但是 relative 却可以。因为它原本所占的空间仍然占据文档流。
# 在理论上，被设置为fixed的元素会被定位于浏览器窗口的一个指定坐标，不论窗口是否滚动，它都会固定在这个位置。
# 4 仅使用margin属性布局绝对定位元素
# 此情况，margin-bottom 和margin-right的值不再对文档流中的元素产生影响，因为该元素已经脱离了文档流。另外，
#     不管它的祖先元素有没有定位，都是以文档流中原来所在的位置上偏移参照物。
#
# 关于css的拾遗:
# 1.inline - block 的间隙
# inline-block默认的空格符就是标签与标签之间的空隙造成的。
# (1) 我们可以通过margin:-3px来解决，但是
#     1.我们布局肯定很多元素，不可能每个都添加margin负这样维护成本太大了
#     2.我们线上代码如果压缩，那么我们就不存在哪个4px的问题了，那么我们的margin负就回造成布局混乱！
# (2)我们可以给几个标签加一个父级div，然后：div{word-spacing: -5px;}
# 2.word-wrap & word-break:
# 3.一旦给元素加上absolute或float就相当于给元素加上了display:block;。什么意思呢？比如内联元素span默认宽度
#     是自适应的，你给其加上width是不起作用的。要想width定宽，你需要将span设成display:block。但如果你给span
#     加上absolute或float，那span的display属性自动就变成block，就可以指定width了。
# 4.快写
#     div   tab
#     a     tab
#     div.main>ul>li.c*4    tab
# 5.display:flex
# 6.响应式布局
# 响应式布局是Ethan Marcotte在2010年5月份提出的一个概念，简而言之，就是一个网站能够兼容多个终端——而
# 不是为每个终端做一个特定的版本。这个概念是为解决移动互联网浏览而诞生的。
# 响应式布局可以为不同终端的用户提供更加舒适的界面和更好的用户体验，而且随着目前大屏幕移动设备的普及，
# 用“大势所趋”来形容也不为过。随着越来越多的设计师采用这个技术，我们不仅看到很多的创新，还看到了一
# 些成形的模式。