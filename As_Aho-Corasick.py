# 2 作为ac自动机
'''
    make_automaton()
    完成并创建 Aho-Corasick 自动机。

    iter(string, [start, [end]]) ---->简单来说就是非贪婪匹配
    使用提供的输入执行 Aho-Corasick 搜索过程string。为在字符串中找到的键返回元组 (end_index, value) 的迭代器。

    iter_long(string, [start, [end]]) ---->简单来说，就是贪婪匹配
    返回搜索最长、非重叠匹配的迭代器（AutomatonSearchIterLong 类的对象）。
'''
import ahocorasick as ah

aca = ah.Automaton()
keywords = ["苹果", "香蕉", "梨", "橙子", "柚子", "火龙果", "柿子", "猕猴挑"]

# 1 利用 add_word方法 将关键词加入自动机！
# 该方法必须包含2个参数，第一个参数是检索词，第二个参数可以任意，作为检索到后的返回词。
for x in keywords:
    aca.add_word(x,x)
# 2 创建 Aho-Corasick 自动机
aca.make_automaton()

# 3 匹配
test_str_list = ["我最喜欢吃的水果有：苹果、梨和香蕉", "我也喜欢吃香蕉，但是我不喜欢吃梨"]
for query in test_str_list:
    for item in aca.iter_long(query): # 进行贪婪匹配
        print(item) # 返回一个tuple

print('-'*10)

for query in test_str_list:
    for item in aca.iter(query): # 进行非贪婪匹配
        print(item)

