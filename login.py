import cgi

# 创建FieldStorage的实例化
form = cgi.FieldStorage()
# 获取html页面传递过来的数据值
str_data_1 = form.getvalue('data_1')
str_data_2 = form.getvalue('data_2')
# 打印输出

print("<h2>data_1:%s,data_2:%s</h2>" % (str_data_1, str_data_2))
