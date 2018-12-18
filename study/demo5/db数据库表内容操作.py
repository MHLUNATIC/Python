# 增：
#     insert into 表 (列名,列名...) values (值,值,值...)
#     insert into 表 (列名,列名...) values (值,值,值...),(值,值,值...)
#     insert into 表 (列名,列名...) select (列名,列名...) from 表
# 删：
#     delete from 表
#     delete from 表 where id＝1 and name＝'alex'
# 改：
#     update 表 set name ＝ 'alex' where id>1
# 查：
#     select * from 表
#     select * from 表 where id > 1
#     select nid,name,gender as gg from 表 where id > 1
# 其它：
#     a、条件
#         select * from 表 where id > 1 and name != 'alex' and num = 12;
#         select * from 表 where id between 5 and 16;
#         select * from 表 where id in (11,22,33)
#         select * from 表 where id not in (11,22,33)
#         select * from 表 where id in (select nid from 表)
#     b、通配符
#         select * from 表 where name like 'ale%'  - ale开头的所有（多个字符串）
#         select * from 表 where name like 'ale_'  - ale开头的所有（一个字符）
#     c、限制
#         select * from 表 limit 5;            - 前5行
#         select * from 表 limit 4,5;          - 从第4行开始的5行
#         select * from 表 limit 5 offset 4    - 从第4行开始的5行
#     d、排序
#         select * from 表 order by 列 asc              - 根据 “列” 从小到大排列
#         select * from 表 order by 列 desc             - 根据 “列” 从大到小排列
#         select * from 表 order by 列1 desc,列2 asc    - 根据 “列1” 从大到小排列，如果相同则按列2从小到大排序
#     e、分组
#         select num from 表 group by num
#         select num,nid from 表 group by num,nid
#         select num,nid from 表  where nid > 10 group by num,nid order nid desc
#         select num,nid,count(*),sum(score),max(score),min(score) from 表 group by num,nid
#         select num from 表 group by num having max(id) > 10
#     特别的：group by 必须在where之后，order by之前
# f、连表                             inner  join
#     无对应关系则不显示
#         select A.num, A.name, B.name from A,B Where A.nid = B.nid
#     无对应关系则不显示
#         select A.num, A.name, B.name from A inner join B on A.nid = B.nid
#     A表所有显示，如果B中无对应关系，则值为null
#         select A.num, A.name, B.name from A left join B on A.nid = B.nid
#     B表所有显示，如果B中无对应关系，则值为null
#         select A.num, A.name, B.name from A right join B on A.nid = B.nid
# g、组合
#     组合，自动处理重合
#         select nickname from A union select name from B
#     组合，不处理重合
#         select nickname from A union all select name from B
