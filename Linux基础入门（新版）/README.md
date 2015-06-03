Linux基础入门（新版）
====================

四层架构
--------
- 应用程序
- 系统调用
- 内核
- 硬件

其中，操作系统工作在系统调用与内核两层（上述顺序为从外至内）

Linux历史简介
-------------
- 批处理程序：从文件或穿孔卡片读取数据，输出到另外文件或打印机
- 交互式操作系统
- 分时操作系统
- Multics
- UNIX
- Linux
- GNU项目

UNIX进化史
---------
![image](/Linux%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%EF%BC%88%E6%96%B0%E7%89%88%EF%BC%89/1.svg)

Linux重要人物
-------------
- Ken Thompson: father of C and UNIX
- Dennis Ritchie: father of C and UNIX
- Stallman: hacker, founder of GNU, Emacs and gcc and bash shell
- Bill Joy: BSD
- Tanenbaum: Minix
- Linus Torvalds: father of Linux

学习路径
--------
![image](/Linux%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%EF%BC%88%E6%96%B0%E7%89%88%EF%BC%89/2.png)

console和terminal和区别
-----------------------
- 终端：对应着Linux上的/dev/tty设备
- terminal：virtual console

shell(壳) &  UNIX/Linux内核(核)

一些常用快捷键
--------------
- ctrl+c:强制终止当前程序
- ctrl+d:键盘输入结束/退出终端
- ctrl+s:暂停当前程序，暂停后按下任意键恢复运行
- ctrl+z:将当前程序放到后台运行。恢复到前台的命令为fg
- ctrl+a:将光标移至输入行头，相当于home键
- ctrl+e:将光标移至输入行末，相当于end键
- ctrl+k:删除从光标所在位置到行末
- alt+backspace:向前删除一个单词
- shift+pgup:将终端显示向上滚动
- shift+pgdn:将终端显示向下滚动

使用通配符
----------
- \*:匹配0或多个字符
- ?:匹配任意一个字符
- [list]:匹配list中的任意单一字符
- [!list]:匹配除list中的任一字符以外的字符
- [c1-c2]:匹配c1-c2中的任一字符
- {string1, string2, ...}:匹配string或string2（或更多）其一字符串
- {c1..c2}:匹配c1-c2中全部字符

> touch love{1..10}linux.txt
> 
> love1linux.txt, love2linux.txt, ..., love10linux.txt

Manual Page
-----------
- 1:一般命令
- 2:系统调用
- 3:库函数（涵盖C标准函数库）
- 4:特殊文件（通常是/dev中的设备）和驱动程序
- 5:文件格式和约定
- 6:游戏和屏保
- 7:杂项
- 8:系统管理命令和守护进程

> man 3 printf

- n: 切换到下一个关键字所在
- shift+n:切换到上一个关键字所在
- Enter:向下滚动一行
- h:显示帮助

> man ls
> 
> info ls (更详细的帮助)
> 
> ls --help (快速查看某个具体参数的作用)

查看用户
--------
> who am i

> who mom likes

- 第一列：打开当前伪终端的用户的用户名
- 第二列：pts表示伪终端（相对于/dev/tty设备而言），后面的数字表示打开的伪终端序号
- 第三列：当前伪终端的启动时间

创建用户
--------
使用sudo的两个条件：

- 知道当前登录用户的密码
- 当前用户在sudo用户组

> sudo adduser lilei (新建一个叫lilei的用户，然后按照提示输入)
> 
> ls /home (显示所有用户)
>
>su -l lilei (切换登录用户)

用户组
------
> groups shiyanlou (冒号之前表示用户，之后表示所属用户组)
>
>cat /etc/group | sort (cat用于读取指定文件的内容并打印到终端，sort将读取的文本进行字典序排列再输出)
>
>cat /etc/group | grep -E “shiyanlou|sudo” (过滤掉一些不想看到的结果)

/etc/group文件格式说明

- 内容包括：用户组，用户组口令，GID，该用户组所包含的用户
- 每个用户组一条纪录，格式为： groupname:password:GID:userlist

>sudo usermod -G sudo lilei (usermod可以为用户添加用户组，将lilei添加到sudo用户组)
>
>sudo deluser lilei --remove-home (删除用户)

Linux文件权限
------------
> ls -l

- 文件类型和权限
    - 第一个字母
        - d：目录
        - l：软链接
        - b：块设备
        - c：字符设备
        - s：socket
        - p：管道
        - -：普通文件
    - 2-4字母：拥有者权限
        - r:读
        - w:写
        - x:执行
    - 5-7字母：所属用户组权限
    - 8-10字母：其他用户权限
- 链接数
- 所有者
- 所属用户组
- 文件大小
- 最后修改时间
- 文件名

ls的一些用法
------------
> ls -lh
>
> ls -A (ls -Al) (A为显示除.和..之外的所有文件)
>
> ls -dl <filename> (查看一个目录的完整属性)
>
> ls -AsSh (显示所有文件大小，s为显示文件大小，S为按文件大小排列)

变更文件所有者
--------------
> touch test (以lilei登录)
>
> cd /home/lilei
>
> sudo chown shiyanlou test
>
> cp test /home/shiyanlou

修改文件权限
------------
- 二进制数字表示

> echo “echo \”hello shiyanlou\”” > test
>
>chmod 700 test (其他用户无法读取test文件)

- 加减赋值操作

> chmod go-rw test (g, o, u分别代表group, other, user, +,-分别表示增加，去掉权限)


