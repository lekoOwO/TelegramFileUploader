#!/usr/bin/env python3

import os
import sys
import subprocess

# 标记当前是否在处理 "--file" 后的文件参数
processing_file = False


def process_file_arg(arg) -> list[str]:
    args = []
    for line in arg.split("\n"):
        line = line.lstrip()
        if line:
            args.append(line)
    return args


def process_args(args):
    # 初始化新命令参数数组
    new_command_args = []
    # 遍历所有传入的参数
    global processing_file
    for arg in args:
        if processing_file:
            # 处理并修改 new_command_args
            new_command_args += process_file_arg(arg)
            processing_file = False  # 重置标记
        else:
            # 检查是否为 "--file"
            if arg == "--file":
                processing_file = True
            new_command_args.append(arg)
    return new_command_args


# 获取当前运行的脚本所在的文件夹的绝对路径
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建 main.py 的绝对路径
main_py_path = os.path.join(current_script_dir, 'main.py')

new_command_args = process_args(sys.argv[1:])

# 执行命令并获取返回结果
result = subprocess.run(["python3", main_py_path] + new_command_args)

# 使用命令的返回状态码作为当前脚本的退出状态码
sys.exit(result.returncode)
