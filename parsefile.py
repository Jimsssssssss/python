#! /usr/bin/env python3
import os
import sys


def parse_file(path):
    """
    分析给定文本文件，返回其空格，制表符，行的相关信息
    """
    fd = open(path)
    i = 0
    spaces = 0
    tabs = 0
    for i,line in enumerate (fd):
        spaces += line.count(' ')
        tabs += line.count('\t')
    fd.close()
    return spaces, tabs, i + 1
def main(path):
    """
    函数用于打印文件分析结果
    """
    if os.path.exists(path):
        spaces, tabs, lines = parse_file(path)
        print("Spaces {}. tabs{}. lines {}".format(spaces, tabs, lines))
        return True
    else:
        return False
if __name__== '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        sys.exit(-1)
    sys.exit(0)

