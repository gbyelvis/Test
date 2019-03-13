#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
#定义初始值
start=1
while True:
#判断start的值若其为51，则说明上一次已经输出了100，跳出循环
   if start==51:
     break
   print start*2
   start +=1
