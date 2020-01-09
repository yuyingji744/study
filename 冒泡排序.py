# coding: utf-8
"""
@File:冒泡排序.py    
@E-mail:623855196@qq.com
@Time:2020-01-09 11:43 
@Author:jyy  
@Version:1.0   
@Desciption:None
"""

'''
题目：输入一个数组，进行排序。
'''


class Solution:
    # write code here.
    def bubble_sort(self, input_list):
        if not isinstance(input_list, list):
            print('输入类型错误，请输入一个数组！')
        elif len(input_list) == 0 or len(input_list) == 1:
            return print(input_list)
        while isinstance(input_list, list) and len(input_list) > 1:
            for i in range(len(input_list) - 1):
                for j in range(len(input_list) - 1 - i):
                    if input_list[j] > input_list[j + 1]:
                        input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
            return print(input_list)


if __name__ == '__main__':
    list1 = []  # 输入空数组（正用例）
    list2 = [18]  # 输入单元素的数组（正用例）
    list3 = [2, 1, 9, 11, 10, 8, 7]  # 正确的数组（正用例）
    list4 = 123  # 输入非数组（反用例）
    list5 = '123'  # 输入非数组且长度大于1（反用例）

    Solution().bubble_sort(list1)
    Solution().bubble_sort(list2)
    Solution().bubble_sort(list3)
    Solution().bubble_sort(list4)
    Solution().bubble_sort(list5)
