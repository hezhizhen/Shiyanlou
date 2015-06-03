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

Linux目录结构
-------------
- FHS标准：定义了系统中每个区域的用途、所需最小构成的文件和目录，例外处理和矛盾处理
    - 第一层：/下面的各个目录应该放什么文件数据
    - 第二层：/usr和/var两个目录的子目录存放内容

![image](/Linux%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%EF%BC%88%E6%96%B0%E7%89%88%EF%BC%89/3.png)

> tree /

目录的四种交互作用的形态
------------------------

![image](/Linux%E5%9F%BA%E7%A1%80%E5%85%A5%E9%97%A8%EF%BC%88%E6%96%B0%E7%89%88%EF%BC%89/4.png)

Linux文件的基本操作
-------------------
- 新建

> mkdir -p father/son/grandson (同时创建父目录)

- 复制

> cp -r father family (复制目录，递归复制。 -R)

- 删除

> chmod 444 test; rm test (删除只读文件)
> 
> rm -f test (强制删除)
>
> rm -r family (删除目录)

- 移动

> mv file1 Documents (把file1移到Documents中)

- 重命名

> mv file1  file2 (重命名)
>
>touch file{1..5}.txt
>
> rename ‘s/\.txt/\.c/’ \*.txt (批量把这5个txt文件的后缀改成c)
>
> rename ‘y/a-z/A-Z/’ \*.c (批量把文件名改成大写)

- 查看文件

    - cat：打印文件内容到标准输出，正序显示
    
    > cat -n test (显示行号)

    - tac：打印文件内容到标准输出，倒序显示

    - nl：添加行号并打印
        - -b:指定添加行号的方式，有 -b a 和 -b t。
        - -n:设置行号的样式，有 -n ln (最左端显示)和 -n rn (最右端显示，不加0)和 -n rz(最右端显示，加0)。
        - -w:行号字段占用的位数(默认为6位)

    - more

    - less

    - head

    - tail

    > tail -n 1 test (只查看最后一行)
    >
    > tail -f test (不停地读取某文件的内容并显示，可以动态查看日志，起到实时监视的作用)

- 文件类型
    - file

- 编辑文件

标准输入输出
------------
当我们执行一个shell命令行时，通常会自动打开三个标准文件：stdin， stdout, stderr

- stdin：标准输入文件，默认对应终端的键盘
- stdout：标准输出文件，对应被重定向到终端的屏幕
- stderr：标准错误输出文件，对应被重定向到终端的屏幕

变量
----
> tmp=shiyanlou (创建一个变量tmp，并赋值为shiyanlou)
>
> echo $tmp (读取变量的值。 $用于表示引用一个变量的值)

环境变量
--------
- 当前shell进程私有用户自定义变量，只在当前shell中有效
- shell本身内建的变量
- 从自定义变量导出的环境变量

- set：显示当前shell所有环境变量
- env：显示与当前用户相关的环境变量
- export：显示从shell中导出成环境变量的变量

> temp=shiyanlou
>
> export tempenv=shiyanlou
>
> env|sort>env.txt
>
> export|sort>export.txt
>
> set|sort>set.txt
>
>vimdiff env.txt export.txt set.txt

简单地说，在当前进程的子进程中有效的变量即环境变量，否则不是

为了与普通变量区分，通常我们习惯将环境变量名设为大写

添加自定义路径到PATH环境变量
----------------------------
> PATH=$PATH:/path/to/mybin (一定要用绝对路径，使用：作为分隔符)
>
> echo “PATH=$PATH:/path/to/mybin” >> .zshrc (>>表示将标准输出以追加的方式重定向到一个文件中，>以覆盖的方式重定向到一个文件中)

变量修改
-------
- ${变量名#匹配字串}：从头向后开始匹配，删除符合匹配字串的最短数据
- ${变量名##匹配字串}：从头向后匹配，删除符合匹配字串的最长数据
- ${变量名%匹配字串}：从尾向前开始匹配，删除复合匹配字串的最短数据
- ${变量名%%匹配字串}：从尾向前匹配，删除符合匹配字串的最长数据
- ${变量名/旧的字串/新的字串}：将符合旧字串的第一个字串替换为新的字串
- ${变量名//旧的字串/新的字串}：将符合旧字串的全部字串替换为新的字串

变量删除
-------
> unset temp (删除一个环境变量)

让环境变量立即生效
------------------
>source .zshrc
>
>. ./.zhsrc

搜索文件
--------
- whereis

    > whereis who

- which

- find

    > find /etc/ -name interfaces (在指定目录搜索指定文件名的文件)
    >
    > find命令的路径是第一个参数，基本命令格式为find [path] [option] [action]
    >
    > find ～ -mtime 0 (列出home目录中当天(24小时之内)有改动的文件)
    >
    > find ～ -newer Documents/test.c\～ (列出home目录下比test.c还要新的文件)

- locate

    > locate /etc/sh
    >
    > locate /usr/share/\*.jpg

常用压缩包格式
--------------
- \*.zip：zip程序打包压缩的文件
- \*.rar：rar程序压缩的文件
- \*.7z：7zip程序压缩的文件
- \*.tar：tar程序打包，未压缩的文件
- \*.gz：gzip程序(GNU zip)压缩的文件
- \*.xz：xz程序压缩的文件
- \*.bz2：bzip2程序压缩的文件
- \*.tar.gz：tar打包，gzip压缩的文件
- \*.tar.xz：tar打包，xz压缩的文件
- \*.tar.bz2：tar打包，bzip2压缩的文件
- \*.tar.7z：tar打包，7zip压缩的文件

zip
----
> zip -r -q -o shiyanlou.zip /home/shiyanlou (-r递归打包，-q静默模式，-o输出文件)
>
> zip -r -9 -q -o shiyanlou9.zip /home/shiyanlou -x ～/\*.zip (压缩级别1-9,9最大，表示体积最小但耗时最久； -x排除我们上一次创建的zip文件)
>
> du -h -d 0 \*.zip ～ | sort (分别查看默认压缩级别、最低和最高压缩级别以及未压缩文件的大小)
>
> zip -r -e -o shiyanlouencryption.zip /home/shiyanlou (创建加密zip包)
>
> zip -r -l -o shiyanlou.zip /home/shiyanlou (-l参数将LF(Linux下的换行)转换为CR+LF(Windows下的回车加换行))
>
> unzip -q shiyanlou.zip -d ziptest (静默解压至指定目录)
>
> unzip -l shiyanlou.zip (不解压只查看压缩包内容)
>
> unzip -O GBK 中文压缩文件.zip (大写o，指定编码类型)

rar
---
rar的命令参数没有-，加上会报错

> rar a shiyanlou.rar . (a参数添加一个目录～到一个归档文件中，不存在则创建)
>
> rar d shiyanlou.rar .zshrc (从指定压缩包中删除某个文件)
>
> rar l shiyanlou.rar (查看不解压文件)
>
> unrar x shiyanlou.rar (全路径解压)
>
> unrar e shiyanlou.rar tmp/ (去掉路径解压)
>
> 上述俩命令不明白?

tar
---
> tar -cf shiyanlou.tar ~ (创建一个tar包， -c表示创建一个tar包，-f表示指定创建的文件名，文件名需紧随其后， -v以可视化的方式输出打包文件)
>
> 会自动去掉表示绝对路径的/， 可使用-P保留绝对路径
>
> tar -xf shiyanlou.tar -C tardir (解包一个文件(-x)到指定路径的存在目录（-C）)
>
> tar -tf shiyanlou.tar (-t只查看不解包文件)
>
> tar -cphf etc.tar /etc (-p保留文件的属性，-h保留链接指向的源文件)
>
> tar -czf shiyanlou.tar.gz ~ (-z表示使用gzip来压缩文件)
>
> tar -xzf shiyanlou.tar.gz (解压tar.gz文件)
>
> tar -xJf shiyanlou.tar.xz (解压tar.xz文件)
>
> tar -xjf shiyanlou.tar.bz2 (解压tar.bz2文件)

