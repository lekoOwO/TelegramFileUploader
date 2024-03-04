#!/usr/bin/env bash

# 初始化新命令变量
new_command=""

# 标记是否遇到了 --files 参数
encountered_files=false

# 遍历所有传入的参数
for arg in "$@"; do
  if $encountered_files; then
    # 如果已经遇到了 --files，后续参数视作文件名，直到遇到另一个以“--”开头的参数
    if [[ "$arg" == --* ]]; then
      encountered_files=false # 如果遇到另一个参数，重置标记
      new_command+=" $arg" # 把这个参数也加入新命令
    else
      # 添加文件到命令中，考虑到文件名中可能包含空格，使用引号
      new_command+=" \"$arg\""
    fi
  else
    # 如果当前参数是 --files，设置标记但不立即处理
    if [[ $arg == "--files" ]]; then
      encountered_files=true
    else
      # 将当前参数加入到新命令中
      new_command+=" $arg"
    fi
  fi
done

# 执行新命令，使用 eval 来正确处理特殊字符和空格
eval "python3 main.py$new_command"
