# coding=utf-8

name = raw_input("你叫什么名字啊？")
age = raw_input("你今年几岁了啊？")

after_ten = int(age) + 10

print((name+'你好').center(60, "="))
print "你的名字叫：", name
print "你今年有 "+age+" 岁了。"
print "再过十年你就会有 "+str(after_ten)+"岁了。"