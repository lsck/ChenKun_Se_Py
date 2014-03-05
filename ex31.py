#coding=utf-8
print '''
饥肠辘辘的你，在绝望之际却发现了一座小木屋。
木屋有两扇门。你想打开哪扇门？
左边选1，右边先2
'''\
.decode('utf-8').encode('gb2312')
door = raw_input("> ")
if door == "1":
    print "打开左边的门，这有一个小矮人正在吃叫化鸡。你想对它做什么？".decode('utf-8').encode('gb2312')
    print "1. 抢走叫化鸡.".decode('utf-8').encode('gb2312')
    print "2. 跟小矮人交谈，请求分给你一些叫化鸡.".decode('utf-8').encode('gb2312')
    bear = raw_input("> ")
    if bear == "1":
        print "小矮人转过头来攻击你的脸. 你侧身闪掉了，干得漂亮!".decode('utf-8').encode('gb2312')
    elif bear == "2":
        print "小矮人没有理你，继续吃叫化鸡，你被华丽丽的无视了!".decode('utf-8').encode('gb2312')
    else:
        print "好吧, 你的【%s】行为惹怒了小矮人. 小矮人把叫化鸡砸向了你.".decode('utf-8').encode('gb2312') % bear
elif door == "2":
    print "打开右边的门，你仔细发现了如下物品：".decode('utf-8').encode('gb2312')
    print "1. 一大块蓝莓蛋糕.".decode('utf-8').encode('gb2312')
    print "2. 一件破旧的黄色皮夹克.".decode('utf-8').encode('gb2312')
    print "3. 一把子弹上膛的沙漠之鹰.".decode('utf-8').encode('gb2312')
    insanity = raw_input("> ")
    if insanity == "1" or insanity == "2":
        print "你是一个爱好和平的人，直接无视了沙漠之鹰.".decode('utf-8').encode('gb2312')
    else:
        print "抄起沙漠之鹰，并将沙漠之鹰在你手上转成陀螺，潇洒哥!".decode('utf-8').encode('gb2312')
else:
    print "你没打开任何一扇门，转身离开!".decode('utf-8').encode('gb2312')
