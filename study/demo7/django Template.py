# 模版组成：HTML代码＋逻辑控制代码
# 模版的创建过程，对于模版，其实就是读取模版（其中嵌套着模版标签），然后将 Model 中获取的数据插入到模版中，最后将信息返回给用户。
#
# 逻辑控制代码的组成:
# 1  变量（使用双大括号来引用变量）：
    #     语法格式：       {{var_name}}
    #
    # >>> python manange.py shell  (进入该django项目的环境)
    # >>> from django.template import Context, Template
    # >>> t = Template('My name is {{ name }}.')
    # >>> c = Context({'name': 'Stephane'})
    # >>> t.render(c)
    # 'My name is Stephane.'
    # 同一模板，多个上下文，一旦有了模板对象，你就可以通过它渲染多个context，无论何时我们都可以像这样使用同一模板源
    # 渲染多个context，只进行 一次模板创建然后多次调用render()方法渲染会更为高效
    #
    # 深度变量的查找（万能的句点号）:在 Django 模板中遍历复杂数据结构的关键是句点字符 (.)。
    #
    # 变量的过滤器(filter)的使用:
    #     语法格式： {{obj|filter:param}}
           # 1  add          ：   给变量加上相应的值
           # 2  addslashes   :    给变量中的引号前加上斜线
           # 3  capfirst     :    首字母大写
           # 4  cut          ：   从字符串中移除指定的字符
           # 5  date         ：   格式化日期字符串
           # 6  default      ：   如果值是False,就替换成设置的默认值，否则就是用本来的值
           # 7  default_if_none:  如果值是None，就替换成设置的默认值，否则就使用本来的值
            #实例:
            # #value1="aBcDe"
            # {{ value1|upper }}<br>
            # #value2=5
            # {{ value2|add:3 }}<br>

# 2 标签(tag)的使用（使用大括号和百分比的组合来表示使用tag）:{% tags %}
    # {% if %} 的使用 :
    # {% if %}标签计算一个变量值，如果是“true”，即它存在、不为空并且不是false的boolean值,系统则会显示{% if %}和{% endif %}间的所有内容
    # {% if %} 标签接受and，or或者not来测试多个变量值或者否定一个给定的变量
    # {% if %} 标签不允许同一标签里同时出现and和or，否则逻辑容易产生歧义
    #
    # {% for %}的使用:
    # {% for %}标签允许你按顺序遍历一个序列中的各个元素,每次循环模板系统都会渲染{% for %}和{% endfor %}之间的所有内容
    # 在标签里添加reversed来反序循环列表：
    #系统不支持中断循环，系统也不支持continue语句，{% for %}标签内置了一个forloop模板变量，这个变量含有一些属性可以提供给你一些关于循环的信息
    # 1，forloop.counter表示循环的次数，它从1开始计数，第一次循环设为1:
    # { %for item in todo_list %}
    #     < p > {{forloop.counter}}: {{item}} < / p >
    # { % endfor %}
    # 2，forloop.counter0 类似于forloop.counter，但它是从0开始计数，第一次循环设为0
    # 3，forloop.revcounter
    # 4，forloop.revcounter0
    # 5，forloop.first当第一次循环时值为True，在特别情况下很有用：
    # 富有魔力的forloop变量只能在循环中得到，当模板解析器到达{% endfor %}时forloop就消失了如果你的模板context已经包含
    # 一个叫forloop的变量，Django会用{% for %}标签替代它Django会在for标签的块中覆盖你定义的forloop变量的值在其他非循
    # 环的地方，你的forloop变量仍然可用

    # {% empty %}
    # {{li}}
    # { %for i in li %}
    #     < li > {{forloop.counter0}} - ---{{i}} < / li >
    #     { % empty %}
    #     < li > this is empty! < / li >
    # { % endfor %}
    #         [11, 22, 33, 44, 55]
    #            0----11
    #            1----22
    #            2----33
    #            3----44
    #            4----55
    #
    # {%csrf_token%}：csrf_token标签
    # 用于生成csrf_token的标签，用于防治跨站攻击验证。注意如果你在view的index里用的是render_to_response方法，不会生效
    # 其实，这里是会生成一个input标签，和其他表单标签一起提交给后台的。
    #
    # {% url %}:  引用路由配置的地址
    # <form action="{% url "bieming"%}" >
    #           <input type="text">
    #           <input type="submit"value="提交">
    #           {%csrf_token%}
    # </form>
    #
    # {% with %}:用更简单的变量名替代复杂的变量名
    # {% with total=fhjsaldfhjsdfhlasdfhljsdal %} {{ total }} {% endwith %}
    #
    # { % verbatim %}: 禁止render
    # {% verbatim %}
    #          {{ hello }}
    # {% endverbatim %}
    #
    # {% load %}: 加载标签库

# 3 自定义filter和simple_tag
    # from django import template
    # from django.utils.safestring import mark_safe
    # register = template.Library()
    # @register.simple_tag
    # @register.filter
    # 其中fileter可以放在模板语言中的if条件中，而simple_tag则不能,filter参数固定，simple_tag参数任意
    # 使用simple_tag的方法：
    # 1、    在app下创建templatetags目录
    # 2、    创建py文件
    # 3、    创建template对象register
    # 4、    @register.simple_tag    @register.filter
    # 5、    在settings配置文件注册app
    # 6、    在页面文件顶部{%load py文件%}，如果存在继承，这个要放在继承下面
    # 7、    最后在页面使用的时候{% func %},如果有参数{%func 2 3 %}

4 extend模板继承
    # include 模板标签:         内建模板标签： {% include %}
    # 该标签允许在（模板中）包含其它的模板的内容。 标签的参数是所要包含的模板名称，可以是一个变量，也可以是用
    # 单/双引号硬编码的字符串。 每当在多个模板中出现相同的代码时，就应该考虑是否要使用 {% include %} 来减少重复。
    #
    #  extend(继承)模板标签:
    # 本质上来说，模板继承就是先构造一个基础框架模板，而后在其子模板中对它所包含站点公用部分和定义块进行重载。
    # 我们使用模板标签： {% block %} 。 所有的 {% block %} 标签告诉模板引擎，子模板可以重载这些部分。
    # 每个{% block %}标签所要做的是告诉模板引擎，该模板下的这一块内容将有可能被子模板覆盖。
    # <1>如果在模板中使用 {% extends %} ，必须保证其为模板中的第一个模板标记。 否则，模板继承将不起作用。
    # <2>一般来说，基础模板中的 {% block %} 标签越多越好。 记住，子模板不必定义父模板中所有的代码块，因此
    #     你可以用合理的缺省值对一些代码块进行填充，然后只对子模板所需的代码块进行（重）定义。 俗话说，钩子越
    #     多越好。
    # <3>如果发觉自己在多个模板之间拷贝代码，你应该考虑将该代码段放置到父模板的某个 {% block %} 中。
    #     如果你需要访问父模板中的块的内容，使用 {{ block.super }}这个标签吧，这一个魔法变量将会表现出父模
    #     板中的内容。 如果只想在上级代码块基础上添加内容，而不是全部重载，该变量就显得非常有用了。
    # <4>不允许在同一个模板中定义多个同名的 {% block %} 。 存在这样的限制是因为block 标签的工作方式是双向的。
    #     也就是说，block 标签不仅挖了一个要填的坑，也定义了在父模板中这个坑所填充的内容。如果模板中出现了两个
    #     相同名称的 {% block %} 标签，父模板将无从得知要使用哪个块的内容。