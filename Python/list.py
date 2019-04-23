##列表
import random
x = random.randint(1,100)
mix = ['牡丹','水仙','2']
mix.append(x)
mix.extend([x,'string'])
mix.insert(2,'玫瑰')
rose = mix[2]
print (mix)

##列表元素的删mix.remove('2')
del mix[1]
mix.pop()         ##删除列表的最后一个元素，name = mix.pop()
mix.pop(2)       ##加index参数
mix.insert(1,'rose')
print (mix,'\n',mix[1:3])

##列表分片(slice)
mix[1:3]           ##表示取列表中下标index为1到2的元素
mix[:3]                 ##表示取列表中下标index为0到2的元素
mix[:]                  ##表示所有列表的元素
mix[1:]
mix1 = mix[:]           ##拷贝mix1独立于mix，而mix2=mix赋值，mix2会随mix变化而变化

##列表还可以进行+-*/>< and or 运算

##列表的内置函数
dir(list)
mix.count('rose')   ##计算‘rose’在列表中存在的个数
mix.index('rose',0,3)

mix.reverse()           ##头尾互换

mix.sort()              ##升序排列
mix.sort(reverse=true)              ##降序排列sort(func，key，revese)
