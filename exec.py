#!/usr/bin/env python3

import os
import sys
import subprocess
import re

# 初始化新命令参数数组
new_command_args = []

# 标记当前是否在处理 "--file" 后的文件参数
processing_file = False

def process_file_arg(arg):
    # 使用正则表达式移除空白行
    for line in arg.split('\n'):
        line = line.lstrip()
        if line:
            new_command_args.append(line)

# 遍历所有传入的参数
for arg in sys.argv[1:]:
    if processing_file:
        # 处理并修改 new_command_args
        process_file_arg(arg)
        processing_file = False # 重置标记
    else:
        # 检查是否为 "--file"
        if arg == "--file":
            processing_file = True
        new_command_args.append(arg)

# 获取当前运行的脚本所在的文件夹的绝对路径
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建 main.py 的绝对路径
main_py_path = os.path.join(current_script_dir, 'main.py')

# 执行命令
subprocess.run(["python3", main_py_path] + new_command_args)
