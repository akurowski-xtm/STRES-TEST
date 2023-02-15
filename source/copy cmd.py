import shutil

for i in range(1, 51):
    shutil.copy('test.txt', 'new_source({i}).txt'.format(i=i))
