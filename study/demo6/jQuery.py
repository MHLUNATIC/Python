jQuery对象和DOM对象
obj = document.getElementById('sel')
$(obj)  变成jQuery对象
$('#sel')
$('#sel')[0]  变成DOM对象

文件引入 <script src="jquery-3.3.1.js"></script>


$(document).ready(founction(){})
$(founction(){})


show(时间)
hide(时间)
toggle(时间)

fadeIn(时间)
fadeOut(时间)
fadeToggle(时间)
fadeTo(时间,透明度)

滑动

自定义方法(扩展方法)：要加上自执行函数，建立私有域 (function($){})(jQuery)
$.extend({方法名：函数})     $.方法名 调用
$.fn.extend({方法名：函数})  标签对象.方法名 调用

自执行函数
(function(){})()