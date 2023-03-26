# 1 作为trie使用
import ahocorasick
A = ahocorasick.Automaton()

# 构建trie
for index,key in enumerate('he her hers she'.split()):
    # print(index,key)
    A.add_word(key,(index,key))
# 查询trie中是否存在某些字符串
print('he' in A)
print('hers' in A)
print('his' in A)
