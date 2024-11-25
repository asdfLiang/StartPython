import re

# | 或
print(re.match("[0-9]?[a-zA-Z]+|123", "123").group())
print(re.match("[0-9]?[a-zA-Z]+|123", "1a3").group())

# () 分组; \num 引用分组
print(re.match("<(html)>\w*</\\1>", "<html>python</html>").group())

# (?P<name>) 给分组起别名; (?P=name)通过别名引用 -> 注意括号很重要，不能省略
print(
    re.match(
        "<(?P<g1>html)> <(?P<g2>h1)> \w* </(?P=g2)> </(?P=g1)>",
        "<html> <h1> python </h1> </html>",
    ).group()
)
