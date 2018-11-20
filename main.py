# -*- coding: utf-8 -*-
"""
 0 1 2
 3 4 5
 6 7 8

 从0开始，从6结束
 只能水平或垂直走，不能斜着走或跳跃，例如从0开始，下一步只能是1或者3，而不能去4（斜着走）或者2（跳跃）
 不能返回，例如从0走到1后，理论上从1可以去0、2、4，但不允许返回0

 第一行的第一个节点开始，最后一行第一个节点结束
 某个节点最多有4种走法，分别是该节点的左右（如果有的话）以及上下（如果有的话）
 某个节点下一步（理论值）可去的节点是该节点加减1和该节点加减列数
 某个节点下一步可去的值是理论值减去曾经走过的节点

"""
from __future__ import unicode_literals, print_function, division
import sys


def list_next_nodes(row, column, node):
    next_nodes = []
    if node % column == 0:
        if node + column >= row * column:
            return []
        next_nodes.append(node + 1)
    elif (node + 1) % column == 0:
        next_nodes.append(node - 1)
    else:
        next_nodes.extend([node + 1, node - 1])
    if node + column < row * column:
        next_nodes.append(node + column)
    if node - column >= 0:
        next_nodes.append(node - column)
    return next_nodes


def print_rooms(rooms):
    length = len(str(rooms[-1][-1]))
    for nodes in rooms:
        print('\t'.join('{{:{}}}'.format(length).format(node) for node in nodes))


def print_node_next_in_rooms(rooms):
    for nodes in rooms:
        for node in nodes:
            print('{} next: {}'.format(node, list_next_nodes(row, column, node)))


def visit_node(row, column, node, visited):
    next_nodes = set(list_next_nodes(row, column, node))
    available_next_nodes = next_nodes - set(visited)
    if not available_next_nodes:
        return [[node]]
    else:
        nexts = []
        for next_node in available_next_nodes:
            visited.append(node)
            nexts.extend(visit_node(row, column, next_node, visited))
            visited.pop()
        for n in nexts:
            n.insert(0, node)
        return nexts


if __name__ == '__main__':
    row, column = sys.argv[1:]
    row = int(row)
    column = int(column)

    rooms = [range(row * column)[i: i + column] for i in range(0, row * column, column)]
    print_rooms(rooms)

    start = rooms[0][0]
    end = rooms[-1][0]

    visited = []
    results = visit_node(row, column, start, visited)
    print(results)
    print(len([r for r in results if r[-1] == end and len(r) == row * column]))
