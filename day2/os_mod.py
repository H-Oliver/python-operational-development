import os
#cmd_res = os.system("dir")#执行命令，不保存结果
cmd_res = os.popen("dir").read()
print("--->",cmd_res)
os.mkdir("new_dir")

