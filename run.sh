#!/usr/bin/env bash

# 初始化新命令参数数组
declare -a new_command_args

# 标记当前是否在处理 "--file" 后的文件参数
processing_file=false

process_file_arg() {
  local arg="$1"
  # 使用过程替换来避免子shell问题
  while IFS= read -r line; do
    new_command_args+=("$line")
  done < <(echo "$arg" | sed '/^[[:space:]]*$/d')
}

# 遍历所有传入的参数
for arg in "$@"; do
  if $processing_file; then
    # 处理并修改 new_command_args
    process_file_arg "$arg"
    processing_file=false # 重置标记
  else
    # 检查是否为 "--file"
    if [[ "$arg" == "--file" ]]; then
      processing_file=true
    new_command_args+=("$arg")
    fi
  fi
done

# 执行命令
python3 main.py "${new_command_args[@]}"

