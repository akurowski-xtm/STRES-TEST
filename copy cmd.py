import shutil

for i in range(1, 101):
    shutil.copy('test.txt', 'test_new({i}).txt'.format(i=i))
