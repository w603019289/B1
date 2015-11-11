# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 23:00:51 2015

@author: wuyifan
"""

<html>
<head>
    <titile><h1>添加图书</h1></title>
</head>
<body>
    <form action="/add/" method="get">
        <input type="text" name="q" value={{book.name}}><h3>姓名</h3>
        <input type="text" name="p" value={{book.book}}><h3>书籍</h3>
        
    </form>   
</body>
</html>