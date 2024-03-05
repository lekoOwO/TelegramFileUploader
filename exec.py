#!/usr/bin/env python3

import os
import subprocess
import sys
from argparse import ArgumentParser


# 自定义处理 --files 参数，去除回车
def process_files_arg(files):
    processed_files = []
    for file_arg in files:
        processed_files.extend(
            [arg.lstrip() for arg in file_arg.splitlines() if arg.strip()]
        )
    return processed_files


# 使用 argparse 处理命令行参数
parser = ArgumentParser(prog="TelegramFileUploader", epilog="@GitHub:xz-dev")
parser.add_argument("--to", help="Chat ID or username")
parser.add_argument("--message", help="Message")
# 由于 --files 参数可能包含换行符，这里通过 nargs='+' 允许多值输入
parser.add_argument("--files", help="Files", nargs="+")
args = parser.parse_args()

# 对 --files 参数进行特别处理，去除回车
if args.files:
    args.files = process_files_arg(args.files)


# 将处理后的参数组装为命令行参数形式，传递给 subprocess
def build_command_args():
    cmd_args = []
    if args.to:
        cmd_args.extend(["--to", args.to])
    if args.message:
        cmd_args.extend(["--message", args.message])
    if args.files:
        cmd_args.append("--files")
        for file_path in args.files:
            cmd_args.append(file_path)
    return cmd_args


# 获取当前运行的脚本所在的文件夹的绝对路径
current_script_dir = os.path.dirname(os.path.abspath(__file__))

# 构建 main.py 的绝对路径
main_py_path = os.path.join(current_script_dir, "main.py")

new_command_args = build_command_args()

# 执行命令并获取返回结果
print(f"exec: python3 {main_py_path} {' '.join(new_command_args)}")
result = subprocess.run(["python3", main_py_path] + new_command_args)

# 使用命令的返回状态码作为当前脚本的退出状态码
sys.exit(result.returncode)
