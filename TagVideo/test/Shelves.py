# Delete Dir
import shelve
import os
dbase = shelve.open("mydbase")
object1 = ['The', 'bright', ('side', 'of'), ['life']]
object2 = {'name': 'Brian', 'age': 33, 'motto': object1}
dbase['brian']  = object2
dbase['knight'] = {'name': 'Knight', 'motto': 'Ni!'}

print len(dbase)
del dbase['brian']
print len(dbase)

dbase.close()


os.remove('mydbase')
