




"""
【任务执行总时长】
题目描述：
任务编排服务负责对任务进行组合调度。参与编排的任务有两种类型，
其中一种执行时长为taskA，另一种执行时长为taskB。任务一旦
开始执行不能被打断，且任务可连续执行。服务每次可以编排num个
任务。请编写一个方法，生成每次编排后的任务所有可能的总执行时长。
输入描述：
第1行输入分别为第1种任务执行时长taskA，第2种任务执行时长taskB，
这次要编排的任务个数num，以逗号分隔。
输出描述：
数组形式返回所有总执行时时长，需要按从小到大排列。
"""


if __name__ == '__main__':
    taska,taskb,num = map(int,input().split(' '))
    res = []
    for i in range(num+1):
        res.append(i*taska+(num-i)*taskb)
    print(sorted(list(set(res))))
