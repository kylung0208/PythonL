#動物園 A 和動物園 B 飼養著許多動物, 有重覆的動物, 也有在某個動物園才看得到的動物, 兩個動物園的動物集合如下:

zooA = {'elephant', 'tiger', 'lion', 'giraffe', 'leopard', 'antelop'}
zooB = {'lion', 'cheetah', 'giraffe', 'zebra', 'wildebeest', 'elephant'}

'''
#請你試著完成以下集合, 並印出內容:

    set1: 在 zooA 而且也在 zooB 的動物集合
    set2: zooA 和 zooB 所有動物集合
    set3: 在 zooA 但不在 zooB 的動物集合
    set4: 在 zooB 但不在 zooA 的動物集合
    set5: 在 zooA 或是 zooB, 但不同時存在兩個動物園的動物集合
'''

print('zooA: ',zooA)
print('zooB: ',zooB)
print('zooA & zooB: ',zooA & zooB)
print('zooA or zooB: ',zooA | zooB)
print('zooA - zooB: ',zooA - zooB)
print('zooA xor zooB: ',zooA ^ zooB)