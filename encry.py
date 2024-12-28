#!/usr/bin/env python3
"""
读取字符串 进行SHA-256加密
将结果映射为0-65535范围内的一个整数
可以通过提取哈希值的前2个字节(16)位来实现
"""

import hashlib
import argparse

def hash_to_int(input_string):
    # 计算 SHA-256 哈希值
    hash_object = hashlib.sha256(input_string.encode())
    hash_hex = hash_object.hexdigest()

    # 提取哈希值的前两个字节
    first_two_bytes = hash_hex[:4] # 每个16进制字符表示4位
    result = int(first_two_bytes, 16) # 转换为10进制数
    return result

def main():
    # 设置命令行参数解析
    parser = argparse.ArgumentParser(
        description="将输入字符串通过 SHA-256 哈希并映射到 0-65535 范围内的整数"
    )
    
    # 添加位置参数
    parser.add_argument(
        "input_string",
        type=str,
        nargs="?", # 参数可选
        help="需要加密的输入字符串(如果没有传入, 可以使用 -i 或 --input 参数)"
    )

    parser.add_argument(
        "-i", "--input",
        type=str,
        help="需要加密的输入字符串(显式传入)"
    )

    args = parser.parse_args()

    # 优先使用位置参数 `input_string`
    input_string = args.input_string or args.input
    if input_string is None:
        print("错误: 没有提供输入字符串")
        return

    # 计算结果
    result = hash_to_int(input_string)

    print(f"输入的字符串: {input_string}")
    print(f"加密结果为: {result} (范围: 0-65535)")

if __name__ == "__main__":
    main()
