# _*_ coding: utf-8 _*_
# @Time : 2022/3/10 13:52 
# @Author : YU RUI
# @File : test.py
# @desc :
def func(num):
    res_lists = [
        [1, 3, 2],
        [6, 4, 5],
        [9, 8, 7],
        [0]
    ]
    for res_list in res_lists:
        print(res_list)
        time = 1
        for i in res_list:
            print(i)
            if int(num) == i:
                time += 1
        return time


def run():
    nums = "37259"
    sum = 0
    for num in nums:
        sum += func(num)
    print(sum)


if __name__ == '__main__':
    run()
