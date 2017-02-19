#!/usr/bin/python
# -*- coding: utf-8 -*-
# Author:      Jianghan LI <helloworld11010111@gmail.com>
# File:        generate.py
# Create Date: 2017-02-20
# Descripton:  Generate markdown table code in readme.
#              Thanks to Illuz.
import os
import operator
import re

solved = 0
total = 0


def get_solution_info_by_files(files):
    solution_info = {}
    solution_types = set()
    notes = []
    solution_info['li'] = False
    solution_info['yin'] = False
    for file in files:
        # File type
        if file[-3:] == 'cpp':
            solution_types.add('C++')
        elif file[-4:] == 'java':
            solution_types.add('Java')
        elif file[-2:] == 'py':
            solution_types.add('Python')
        elif file[-2:] == 'js':
            solution_types.add('Js')
        elif file[-2:] == 'sh':
            solution_types.add('Shell')
        elif file[-3:] == 'sql':
            solution_types.add('Sql')
        elif file[-2:] == 'md':
            notes.append(file)
        # Author
        if file[:2] == 'li':
            solution_info['li'] = True
        elif file[:3] == 'yin':
            solution_info['yin'] = True
    solution_info['types'] = list(solution_types)
    solution_info['notes'] = notes
    return solution_info


def get_problem_map():
    global solved
    global total
    problem_map = {}
    for path, subdirs, files in os.walk('.'):
        # bypass .
        if len(path) < 2:
            continue
        # fix gdb file in mac
        if '.git' in path:
            continue
        problem_name = path[2:]
        problem_map[problem_name] = get_solution_info_by_files(files)

        total += 1
        if problem_map[problem_name]['types']:
            solved += 1
    # sort and generate
    return sorted(problem_map.items(), key=operator.itemgetter(0))


def print_table(problem_map):
    global solved
    global total
    title = [
        "LeetCode",
        "========",
        "请在题目对应文件夹下提交解答, 开头使用作者名字。例如：yin.cpp，li.py",
        "请在解答内，写清思路，添加必要的注释，以便自己和他人回看。",
        "建议写清作者，方便引用。"]
    for l in title:
        print(l)

    print('| No.| Problem | Han | Yin | Note |')
    print('|----|---------|-----|-----|------|')
    for long_name, solution_info in problem_map:
        # problem_id, short_name(link)
        problem_id = long_name[:3]
        problem_name = re.sub('_', ' ', long_name[4:])
        short_name = long_name if len(long_name) < 48 else long_name[:44] + '... '
        p = '| ' + problem_id + ' | [' + short_name[4:] + '](' + long_name + ') | '
        # add solution_info
        if solution_info:
            p += ' ![](done.png) |' if solution_info['li'] else ' ![](yet.png) |'
            p += ' ![](done.png) |' if solution_info['yin'] else ' ![](yet.png) |'
            p += '&nbsp;' * 8 + '[Notes](./' + long_name + ')' + '&nbsp;' * 8 + '|'\
                if solution_info['notes'] else ' &nbsp;Coming soon |'
        else:
            p += ' ![](yet.png) | ![](yet.png) | &nbsp;Coming soon &nbsp;|'
        print(p)

if __name__ == '__main__':
    problem_map = get_problem_map()
    print_table(problem_map)
