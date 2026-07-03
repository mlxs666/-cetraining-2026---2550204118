import re
from collections import Counter


def count_words(file_path):
    """
    统计一个文本文件中每个单词出现的次数。

    参数:
        file_path (str): 文本文件的路径

    返回:
        dict: 单词 -> 出现次数的字典，按次数降序排列

    规则:
        - 单词定义为连续的字母字符（a-z, A-Z），忽略数字和标点
        - 大小写不敏感，"Hello" 和 "hello" 视为同一个单词
        - 空文件返回空字典
    """
    word_counter = Counter()

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            # 提取每行中的所有英文单词（连续字母），统一转为小写
            words = re.findall(r'[a-zA-Z]+', line)
            words_lower = [w.lower() for w in words]
            word_counter.update(words_lower)

    # 按出现次数降序排列
    return dict(word_counter.most_common())


if __name__ == '__main__':
    import sys

    if len(sys.argv) != 2:
        print("用法: python add_function.py <文件路径>")
        sys.exit(1)

    result = count_words(sys.argv[1])

    if not result:
        print("文件中没有找到任何单词。")
    else:
        print(f"{'单词':<20} {'次数':>6}")
        print("-" * 28)
        for word, count in result.items():
            print(f"{word:<20} {count:>6}")