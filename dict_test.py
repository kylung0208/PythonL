ages = {}
ages['bob'] = 9
ages['alice'] = 18


ages['bob']              # 9
ages.bob                 # error: 'dict' object has no attribute 'bob'
ages.get('bob')          # 9
ages['john']             # KeyError: 'john'
ages.get('john')         # None
ages.get('john', 'N/A')  # 'N/A' ＃如果找不到'John'的歲數，回傳一個預設值'N/A'
len(ages)                # 2
list(ages)               # ['bob', 'alice'], order may differ
'bob' in ages            # True
'john' in ages           # False

#Dictionary 可以直接在大括號中指定內容：
ages = { 'bob': 9, 'alice': 18 }
ages2 = dict({'bob': 9, 'alice': 18}) # same as ages
ages3 = dict(bob=9, alice=18)          # same as ages
ages4 = dict([('bob', 9), (alice, 18)]) # same as ages