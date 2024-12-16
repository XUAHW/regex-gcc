import re

def test_regex(pattern, test_strings):
    """
    测试正则表达式在多组字符串上的匹配结果。

    :param pattern: 正则表达式模式 (str)
    :param test_strings: 测试字符串列表 (list of str)
    """
    print(f"正则表达式: {pattern}")
    print("-" * 40)
    for string in test_strings:
        matches = re.findall(pattern, string)  # 获取所有匹配的部分
        if matches:
            # 输出所有匹配的子串
            print(f"字符串: \"{string}\" -> 匹配: {', '.join(matches)}")
        else:
            print(f"字符串: \"{string}\" -> 无匹配")
    print("-" * 40)


if __name__ == "__main__":
    # 预定义测试字符串列表
    test_strings = [
        "Hello, World!",          # 普通字符串
        "abc123xyz",              # 混合字母和数字
        "123456",                 # 全数字
        "email@example.com",      # 邮箱地址
        "https://example.com",    # URL 地址
        "192.168.1.1",            # IP 地址
        "01/01/2024",             # 日期格式
        "Phone: +1-800-555-1234", # 电话号码
        "Special chars: *&^%$",   # 特殊字符
        "Whitespace   here",      # 包含空格的字符串
        "New\nline",              # 包含换行符
        "tab\tseparated",         # 包含制表符
        "123-45-6789",            # 社保号格式
        "UpperCASElowercase",     # 大小写混合
    ]

    while True:
        # 输入正则表达式
        pattern = input("请输入正则表达式（按 Enter 退出）：")
        if not pattern:  # 如果输入为空，退出循环
            print("程序结束")
            break

        # 调用函数测试正则表达式
        test_regex(pattern, test_strings)