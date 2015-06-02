Linux system monitor tools
    process monitor:top(better alternative: htop)
    virtual memory statistics:vmstat
        vmstat 2 1: 2 means the interval of time of sampling(seconds), 1 means the times of sampling
        r:表示运行队列。若太大，表示CPU繁忙
        b:阻塞的进程数
        swpd:虚拟内存已使用的大小。若大于0，表示机器物理内存不足。
        free
        buff:系统占用的缓存大小
        cache:直接用来记忆我们打开的文件，给文件做缓冲
        si:每秒从磁盘读入虚拟内存的大小。若大于0，表示物理内存不足。
        us:用户CPU时间
        sy:系统CPU时间
        so:每秒虚拟内存写入磁盘的大小。若大于0，表示物理内存不足。
        id:空闲CPU时间。一般id+us+sy=100
        wt:等待IO的CPU时间
    list open files:lsof
    network package analyser: tcpdump
    network states statistics: netstat
    iotop
    iostat 
        sudo apt-get install sysstat
        iostat
        avg-cpu各项含义：
            %user:在用户级别运行所使用的CPU的百分比
            %nice:优先进程消耗的CPU时间，占所有CPU的百分比
            %system:在系统级别运行使用的CPU百分比
            %iowait:CPU等待硬件IO时，所占用CPU百分比
            %steal:管理程序维护另一个虚拟处理器时，虚拟CPU的无意识等待时间百分比
