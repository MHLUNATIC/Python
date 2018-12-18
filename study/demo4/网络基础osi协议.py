# http://www.cnblogs.com/linhaifeng/articles/5937962.html
# http://www.cnblogs.com/linhaifeng/articles/5951486.html   子网
# http://www.cnblogs.com/yuanchenqi/articles/5722574.html  事件驱动模型 五种IO Model：blocking IO,nonblocking IO,IO multiplexing,signal driven IO,asynchronous IO
# OSI是Open System Interconnection的缩写，意为开放式系统互联。国际标准化组织（ISO）制定了OSI模型，
# 该模型定义了不同计算机互联的标准，是设计和描述计算机网络通信的基本框架。
# OSI模型把网络通信的工作分为7层，分别是物理层、数据链路层、网络层、传输层、会话层、表示层和应用层。
# 操作系统:(Operating System，简称OS)是管理和控制计算机硬件与软件资源的计算机程序，是直接运行在“裸机”上的最基本
# 的系统软件，任何其他软件都必须在操作系统的支持下才能运行。注：hardware－>os－>application
# 连接两台计算机之间的internet实际上就是一系列统一的标准，这些标准称之为互联网协议，互联网的本质就是一系列的协议，
# 总称为‘互联网协议’（Internet Protocol Suite).
# 互联网协议的功能：定义计算机如何接入internet，以及接入internet的计算机通信的标准。
# 互联网协议按照功能不同分为osi七层或tcp/ip五层或tcp/ip四层:
# 1.物理层功能：主要是基于电器特性发送高低电压(电信号)，高电压对应数字1，低电压对应数字0
# 2.数据链路层的功能：定义了电信号的分组方式  以太网协议(ethernet)  mac地址  广播
# 3.网络层功能：引入一套新的地址用来区分不同的广播域／子网，这套地址即网络地址
# IP协议  ip地址分成两部分(网络部分：标识子网 主机部分：标识主机)  子网掩码   ip数据包   ARP协议
# 4.传输层功能：建立端口到端口的通信(端口范围0-65535，0-1023为系统占用端口)
# tcp协议  udp协议  tcp报文  tcp三次握手和四次挥手
# 5.应用层功能：规定应用程序的数据格式。 http FTP等
# 想实现网络通信，每台主机需具备四要素:本机的IP地址,子网掩码,网关的IP地址,DNS的IP地址
