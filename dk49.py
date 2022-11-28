"""
■ 题目描述
【转骰子】
骰子是一个立方体，每个面一个数字，初始为左1，右2，前3(观察者方向)，后4，上5，下6，用123456表示这个状态，放置在平面上，
可以向左翻转(用L表示向左翻转1次)，
可以向右翻转(用R表示向右翻转1次)，
可以向前翻转(用F表示向前翻转1次)，
可以向后翻转(用B表示向后翻转1次)，
可以逆时针旋转(用A表示逆时针旋转90度)，
可以顺时针旋转(用C表示顺时针旋转90度)，
现从123456这个初始状态开始，根据输入的动作序列，计算得到最终的状态。
骰子的初始状态和初始状态转动后的状态如图所示。
输入描述
输入一行，为只包含LRFBAC的字母序列，最大长度为50，字母可重复。
输出描述
输出最终状态
示例1 输入输出示例仅供调试，后台判题数据一般不包含示例
输入
L R
输出
123456
"""


class Cube:
    def __init__(self, left, right, front, back, top, bottom):
        self.left = left
        self.right = right
        self.front = front
        self.back = back
        self.top = top
        self.bottom = bottom


def left_rotate(cube):
    left = cube.left
    right = cube.right
    top = cube.top
    bottom = cube.bottom
    cube.left = top
    cube.right = bottom
    cube.top = right
    cube.bottom = left
    return cube


def right_rotate(cube):
    left = cube.left
    right = cube.right
    top = cube.top
    bottom = cube.bottom
    cube.left = bottom
    cube.right = top
    cube.top = left
    cube.bottom = right
    return cube


def front_rotate(cube):
    front = cube.front
    back = cube.back
    top = cube.top
    bottom = cube.bottom
    cube.front = top
    cube.back = bottom
    cube.top = back
    cube.bottom = front
    return cube


def back_rotate(cube):
    front = cube.front
    back = cube.back
    top = cube.top
    bottom = cube.bottom
    cube.front = bottom
    cube.back = top
    cube.top = front
    cube.bottom = back
    return cube


def a_rotate(cube):
    front = cube.front
    back = cube.back
    left = cube.left
    right = cube.right
    cube.front = left
    cube.back = right
    cube.left = back
    cube.right = front
    return cube


def c_rotate(cube):
    front = cube.front
    back = cube.back
    left = cube.left
    right = cube.right
    cube.front = right
    cube.back = left
    cube.left = front
    cube.right = back
    return cube


if __name__ == '__main__':
    s = input()
    s = s.split(' ')
    cube = Cube(1, 2, 3, 4, 5, 6)
    cur = Cube(1, 2, 3, 4, 5, 6)
    for i in range(0, len(s)):
        if s[i] == 'L':
            cur = left_rotate(cur)
        elif s[i] == 'R':
            cur = right_rotate(cur)
        elif s[i] == 'F':
            cur = front_rotate(cur)
        elif s[i] == 'B':
            cur = back_rotate(cur)
        elif s[i] == 'A':
            cur = a_rotate(cur)
        elif s[i] == 'C':
            cur = c_rotate(cur)
    res = ""
    res += str(cur.left)
    res += str(cur.right)
    res += str(cur.front)
    res += str(cur.back)
    res += str(cur.top)
    res += str(cur.bottom)
    print(res)
