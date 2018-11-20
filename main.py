# -*- coding: utf-8 -*-
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
        return [node]
    else:
        nexts = []
        for next_node in available_next_nodes:
            visited.append(node)
            nexts.extend(visit_node(row, column, next_node, visited))
            visited.pop()
        return [[node, e] for e in nexts]


if __name__ == '__main__':
    row, column = sys.argv[1:]
    row = int(row)
    column = int(column)

    rooms = [range(row * column)[i: i + column] for i in range(0, row * column, column)]
    print_rooms(rooms)

    start = rooms[0][0]
    end = rooms[-1][0]

    visited = []
    print(visit_node(row, column, start, visited))
