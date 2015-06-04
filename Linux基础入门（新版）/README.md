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

<hr>

du
---
> du -h -d 0 ~ (只查看1级目录的信息，-d指定参看目录的深度)
>
> du -h -d 1 ~ (查看2级)

dd
--
用于转换和复制文件(不同于cp)，可以用在备份硬件的引导扇区、获取一定数量的随机数据或者空数据等任务中；可以在复制时处理数据

命令项格式

> 选项=值

默认从标准输入中读取，并写入标准输出中，但可以用选项if(输出文件)和of(输出文件)改变

> dd of=test bs=10 count=1 (dd if=/dev/stdin of=test bs=10 count=1) (输出到文件)
>
> dd if=/dev/stdin of=dev/stdout bs=10 count=1 (输出到标准输出)

- bs用于指定块大小(默认单位为Byte)
- count用于指定块数量
- 多余输入将被截取并保留在stdin

创建虚拟磁盘
------------
> dd if=/dev/stdin of=test bs=10 count=1 conv=ucase (将输出的英文字符转换为大写再写入文件)

> dd if=/dev/zero of=virtual.img bs=1M count=256 (从/dev/zero设备创建一个容量为256M的空文件)
>
> mkfs.ext4 virtual.img (格式化虚拟磁盘镜像为ext4)
>
> ls -l /lib/modules/$(uname -r)/kernel/fs (查看系统支持哪些文件系统)
>
> mount -o loop -t ext4 virtual.img /mnt (把虚拟磁盘镜像挂载到/mnt目录，挂载类型可省略，会自动识别)
> 
> mount -o lopp --ro virtual.img /mnt (-o后面跟操作选项，-t后面跟文件系统类型，-w|--rw|--ro为读写权限，后面是文件系统源和挂载点)
>
> sudo umount /mnt (卸载已挂载磁盘)
>
> [/dev/loop](http://zh.wikipedia.org/wiki//dev/loop)
>
> sudo fdisk -l (查看硬盘分区表信息)
>
> sudo fdisk virtual.img (进入磁盘分区模式)
>
> 分区方案：使用128M的虚拟磁盘镜像创建一个30M的主分区，剩余部分为扩展分区，包含2个45M的逻辑分区
>
> 最后要输入w写入分区表
>
> sudo losetup /dev/loop0 virtual.img (建立镜像与loop设备的关联)
>
> sudo losetup -d /dev/loop0 (解除设备关联)
>
> sudo kpart kpartx -av /dev/loop0 (为各分区建立虚拟设备的映射，使用kpartx)
>
> sudo kpart kpartx -dv /dev/loop0 (取消映射)
>
> sudo mkfs.ext4 -q /dev/mapper/loop0p1 (格式化各分区，还有loop0p5,loop0p6)
>
> mkdir -p /media/virtualdisk\_{1..3} (在/media目录下新建4个空目录用于挂载虚拟磁盘)
>
> sudo mount /dev/mapper/loop0p1 /media/virtualdisk\_1 (挂载磁盘分区， 还有loop0p5,loop0p6，分别挂载到2和3)
>
> sudo umount /dev/mapper/loop0p1 (卸载磁盘分区，还有loop0p5和loop0p6)

<hr>

顺序执行多条命令
----------------
> sudo apt-get update; sudo apt-get install tmux; tmux (使用分号)

有选择地执行命令
----------------
> which cowsay > /dev/null && cowsay -f head-in ohch~ (&&实现选择性执行，如果前面的命令执行结果返回0则执行后面的，否则不执行。可以从$?环境变量获取上一次命令的返回结果)
>
> which cowsay > /dev/null || echo “cowsay has not been installed” (||与&&相反)
>
> which cowsay > /dev/null && echo “exist” || echo “not exist”

管道
----
管道是一种通信机制，通常用于进程间的通信（也可通过socket进行网络通信），表现形式为将前面的每一个进程的输出（stdout）直接作为下一个进程的输入（stdin）

分为：匿名管道，具名管道

> ls -al /etc | less (将ls的输出作为less的输入)
>
> cut /etc/passwd -d ‘:’ -f 1,6 (以：为分隔符的第1字段和第6字段分别表示用户名和其家目录)
>
> cut /etc/passwd -c -5 (打印文件每一行的前5个字符（含第5个）)
>
> cut /etc/passwd -c 5- (前5个之后的字符（含第5个）)
>
> cut /etc/passwd -c 5 (第五个字符)
>
> cut /etc/passwd -c 2-5 (2-5个字符)

> grep -rnI “shiyanlou” ～ (搜索～目录下所有包含shiyanlou的所有文本文件，并显示出现在文本中的行号)

- -r: 递归搜索子目录中的文件
- -n: 打印匹配项行号
- -I: 忽略二进制文件

> export | grep “.\*yanlou$” (查看环境变量中以yanlou结尾的字符串, $表示一行的末尾)

> ls -dl /etc/\*/ | wc -l (统计/etc下面所有目录数)

> cat /etc/passwd | sort (默认字典序)
>
> cat /etc/passwd | sort -r (反转排序)
>
> cat /etc/passwd | sort -t‘:’ -k 3 (按特定字段排序)

- -t:指定字段的分隔符，这里以：为分隔符
- -k 字段号：指定对哪一个字段进行排序

> cat /etc/passwd | sort -t’:’ -k 3 -n (-n使按数字排序)

> history | cut -c 8- | cut -d ‘ ‘ -f 1 | uniq (uniq只能去除连续重复的行，不是全文去重)
>
> history | cut -c 8- | cut -d ‘ ‘ -f 1 | sort | uniq (history | cut -c 8- | cut -d ‘ ‘ -f 1 | sort -u)

> history | cut -c 8- | cut -d ‘ ‘ -f 1 | sort | uniq -dc (输出重复过的行（重复的只输出一次）及重复次数)
>
> history | cut -c 8- | cut -d ‘ ‘ -f 1 | sort | uniq -D (输出所有重复的行)

<hr>

tr
==
translate or delete characters. tr [OPTION] ... SET1 [SET2]

- -d: 删除和set1匹配的字符，不是全词匹配也不是按字符顺序匹配
- -s: 去除set1指定的在输入文本中连续并重复的字符

> echo ‘hello shiyanlou’ | tr -d ‘olh’ (删除所有的o、l、h)
>
> echo ‘hello’ | tr -s ‘l’ (把ll去重为l)
>
> cat /etc/passwd | tr ‘[:lower:]’ ‘[:upper:]’ (将输入文本全部转换为大写或小写输出)

col
---
filter reverse line feeds from input. col [-bfhpx] [-l num]

- -x:将Tab转换为空格
- -h:将空格转换为Tab

> cat -A /etc/protocols (查看不可见字符，可以看到很多^I，其实是Tab转义成可见字符的符号)
>
> cat /etc/protocols | col -x | cat -A (^I不见了)

join
----
join lines of two files on a common field. join [OPTION] FILE1 FILE2

- -t:指定分隔符，默认空格
- -i:忽略大小写差异
- -1:指明第一个文件要用哪个字段来对比，默认对比第一个字段
- -2:指定第二个文件要用哪个字段对比，默认对比第一个字段

> sudo join -t ‘:’ /etc/passwd /etc/shadow
>
> sudo join -t ‘:’ -1 4 /etc/passwd -2 3 /etc/group (指定以：为分隔符，分别对比第4和第3字段)

paste
-----
类似join，在不对比数据的情况下，合并多文件，以Tab隔开

- -d:指定合并的分隔符，默认为Tab
- -s:不合并到一行，每个文件为一行

> paste -d ‘:’ file1 file2
>
> paste -s file1 file2

<hr>
