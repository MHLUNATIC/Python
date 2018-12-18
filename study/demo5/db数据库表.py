# 创建表：
# create table 表名(
#     列名  类型  是否可以为空，
#     列名  类型  是否可以为空
# )ENGINE=InnoDB DEFAULT CHARSET=utf8
# not null    - 不可空
# null        - 可空
# 创建列时可以指定默认值：defalut
# 如果为某列设置自增列，插入数据时无需设置此列，默认将自增（表中只能有一个自增列）：auto_increment
#             注意：1、对于自增列，必须是索引（含主键）。2、对于自增可以设置步长和起始值
# 主键，一种特殊的唯一索引，不允许有空值，如果主键使用单个列，则它的值必须唯一，如果是多列，则其组合必须唯一。
# 外键，一个特殊的索引，只能是指定内容
# create table tb1(
#     nid int not null auto_increment primary key,
#     num int null,
#     index(nid)，
#     primary key(nid,num)
# )ENGINE=InnoDB DEFAULT CHARSET=utf8
# 删除表：
#   drop table 表名
# 清空表：
#   delete from 表名
#   truncate table 表名
#
# 修改表：
#     添加列：alter table 表名 add 列名 类型
#     删除列：alter table 表名 drop column 列名
#     修改列：
#             alter table 表名 modify column 列名 类型;  -- 类型
#             alter table 表名 change 原列名 新列名 类型; -- 列名，类型
#     添加主键：
#             alter table 表名 add primary key(列名);
#     删除主键：
#             alter table 表名 drop primary key;
#             alter table 表名  modify  列名 int, drop primary key;
#     添加外键：alter table 从表 add constraint 外键名称（形如：FK_从表_主表） foreign key 从表(外键字段) references 主表(主键字段);
#     删除外键：alter table 表名 drop foreign key 外键名称
#     修改默认值：ALTER TABLE testalter_tbl ALTER i SET DEFAULT 1000;
#     删除默认值：ALTER TABLE testalter_tbl ALTER i DROP DEFAULT;
# MySQL的数据类型大致分为：数值、时间和字符串
# bit[(M)]
#             二进制位（101001），m表示二进制位的长度（1-64），默认m＝1
#
#         tinyint[(m)] [unsigned] [zerofill]
#
#             小整数，数据类型用于保存一些范围的整数数值范围：
#             有符号：
#                 -128 ～ 127.
#             无符号：
# ～ 255
#
#             特别的： MySQL中无布尔值，使用tinyint(1)构造。
#
#         int[(m)][unsigned][zerofill]
#
#             整数，数据类型用于保存一些范围的整数数值范围：
#                 有符号：
#                     -2147483648 ～ 2147483647
#                 无符号：
# ～ 4294967295
#
#             特别的：整数类型中的m仅用于显示，对存储范围无限制。例如： int(5),当插入数据2时，select 时数据显示为： 00002
#
#         bigint[(m)][unsigned][zerofill]
#             大整数，数据类型用于保存一些范围的整数数值范围：
#                 有符号：
#                     -9223372036854775808 ～ 9223372036854775807
#                 无符号：
#  ～  18446744073709551615
#
#         decimal[(m[,d])] [unsigned] [zerofill]
#             准确的小数值，m是数字总个数（负号不算），d是小数点后个数。 m最大值为65，d最大值为30。
#
#             特别的：对于精确数值计算时需要用此类型
#                    decaimal能够存储精确值的原因在于其内部按照字符串存储。
#
#         FLOAT[(M,D)] [UNSIGNED] [ZEROFILL]
#             单精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。
#                 无符号：
#                     -3.402823466E+38 to -1.175494351E-38,
#                     1.175494351E-38 to 3.402823466E+38
#                 有符号：
#                     1.175494351E-38 to 3.402823466E+38
#
#             **** 数值越大，越不准确 ****
#
#         DOUBLE[(M,D)] [UNSIGNED] [ZEROFILL]
#             双精度浮点数（非准确小数值），m是数字总个数，d是小数点后个数。
#
#                 无符号：
#                     -1.7976931348623157E+308 to -2.2250738585072014E-308
#                     2.2250738585072014E-308 to 1.7976931348623157E+308
#                 有符号：
#                     2.2250738585072014E-308 to 1.7976931348623157E+308
#             **** 数值越大，越不准确 ****
#
#
#         char (m)
#             char数据类型用于表示固定长度的字符串，可以包含最多达255个字符。其中m代表字符串的长度。
#             PS: 即使数据小于m长度，也会占用m长度
#         varchar(m)
#             varchars数据类型用于变长的字符串，可以包含最多达255个字符。其中m代表该数据类型所允许保存的字符串的最大长度，只要长度小于该最大值的字符串都可以被保存在该数据类型中。
#
#             注：虽然varchar使用起来较为灵活，但是从整个系统的性能角度来说，char数据类型的处理速度更快，有时甚至可以超出varchar处理速度的50%。因此，用户在设计数据库时应当综合考虑各方面的因素，以求达到最佳的平衡
#
#         text
#             text数据类型用于保存变长的大字符串，可以组多到65535 (2**16 − 1)个字符。
#
#         mediumtext
#             A TEXT column with a maximum length of 16,777,215 (2**24 − 1) characters.
#
#         longtext
#             A TEXT column with a maximum length of 4,294,967,295 or 4GB (2**32 − 1) characters.
#
#
#         enum
#             枚举类型，
#             An ENUM column can have a maximum of 65,535 distinct elements. (The practical limit is less than 3000.)
#             示例：
#                 CREATE TABLE shirts (
#                     name VARCHAR(40),
#                     size ENUM('x-small', 'small', 'medium', 'large', 'x-large')
#                 );
#                 INSERT INTO shirts (name, size) VALUES ('dress shirt','large'), ('t-shirt','medium'),('polo shirt','small');
#
#         set
#             集合类型
#             A SET column can have a maximum of 64 distinct members.
#             示例：
#                 CREATE TABLE myset (col SET('a', 'b', 'c', 'd'));
#                 INSERT INTO myset (col) VALUES ('a,d'), ('d,a'), ('a,d,a'), ('a,d,d'), ('d,a,d');
#
#         DATE
#             YYYY-MM-DD（1000-01-01/9999-12-31）
#
#         TIME
#             HH:MM:SS（'-838:59:59'/'838:59:59'）
#
#         YEAR
#             YYYY（1901/2155）
#
#         DATETIME
#
#             YYYY-MM-DD HH:MM:SS（1000-01-01 00:00:00/9999-12-31 23:59:59    Y）
#
#         TIMESTAMP
#
#             YYYYMMDD HHMMSS（1970-01-01 00:00:00/2037 年某时）

# 二进制数据：TinyBlob、Blob、MediumBlob、LongBlob