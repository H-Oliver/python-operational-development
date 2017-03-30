import sys
import os
import shutil

if len(sys.argv) < 4:
    sys.exit("usage:sed.py old_text new_text file_name")

# 假定程序的参数是正确的
# 取参数赋值
progran_ame, old_text, new_text, arg_file_name = sys.argv
print(progran_ame, old_text, new_text, arg_file_name)

if not os.path.exists(arg_file_name):
    sys.exit("文件%s不存在" % arg_file_name)


# 判断输入的参数是否为绝对路径， 如果是相对路径则取得绝对路径
if os.path.isabs(arg_file_name):
    src_file = arg_file_name
else:
    src_file = os.path.realpath(arg_file_name)

# 将原来的文件重新命名，得到备份文件名
src_path_name = os.path.dirname(src_file)
src_file_name = os.path.basename(src_file)
bak_file_name = os.path.splitext(src_file_name)[0]+'_bak'+os.path.splitext(src_file_name)[1]
back_file = src_path_name+os.sep+bak_file_name

# 备份文件
shutil.copy(src_file, back_file)

out_file = open(src_file, 'w', encoding='utf-8')
# 对文件的每一行进行遍历，同时进行替换操作
with open(back_file, encoding='utf-8') as f:
    for line in f:
        out_file.writelines(line.replace(old_text, new_text))

out_file.close()