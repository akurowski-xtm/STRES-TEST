import shutil

for i in range(1, 201):
    shutil.copy('test.txt', 'new_source({i}).txt'.format(i=i))
