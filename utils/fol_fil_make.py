import os
new_dir_path=input()
dokomade=input()
lis=['a','b','c','d','e','f','g','h']
print('../'+new_dir_path[:3]+'/'+new_dir_path)
if not os.path.exists('../'+new_dir_path[:3]):    
    print('folder is not exists')
    exit()
if os.path.exists('../'+new_dir_path[:3]+'/'+new_dir_path):
    print('number is exists')
    exit()
if not(dokomade in lis):
    print('file\'s range is over')

os.makedirs('../'+new_dir_path[:3]+'/'+new_dir_path)






def save_file_at_dir(dir_path, filename, file_content, mode='w'):
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, filename), mode) as f:
        f.write(file_content)
for i in range(len(lis)):
    save_file_at_dir('../'+new_dir_path[:3]+'/'+new_dir_path,lis[i]+'.py',file_content='',mode='w')
    if(lis[i]==dokomade):
        break
