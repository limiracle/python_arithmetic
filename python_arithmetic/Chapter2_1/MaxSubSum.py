# encoding: utf-8
# module python_arithmetic
# by lizhi limiracle@163.com

"""
 最大子序列和问题
 问题描述：给定整数（可以为负数），A1，A2，A3,....,AN,求子序列最大的值
 例如：对于整数列：－１，１１，－４，１３，－５，－２　最大的序列值为：２０（１１，－４，１３）
 此例子给出三个算法实现，时间复杂度分别为：O(n2),O(nlogn),O(n)
"""

# 此算法时间复杂度为O(n2)，也是最先想到的算法实现
def maxSubSum1(*a):
    max=0
    for i,value in enumerate(a):
        thisMax=0
        for j in a[i:]:
            thisMax+=j
            if thisMax>max :
                max=thisMax
    return max

#大招，使用递归实现算法，时间复杂度为：O(nlogn)
def maxSubSum2(left,right,*a):
    if left==right:     #base case
        return a[left]

    center =(left+right)/2
    maxLeft=maxSubSum2(left,center,*a)
    maxRight=maxSubSum2(center+1,right,*a)

    leftSum=0
    maxLeftSum=0
    i=center
    while i>=0:
        leftSum+=a[i]
        if leftSum>maxLeftSum:
            maxLeftSum=leftSum
        i=i-1

    rightSum = 0
    maxRightSum = 0
    i = center+1
    while i <=right :
        rightSum += a[i]
        if rightSum > maxRightSum:
            maxRightSum = rightSum
        i = i + 1

    return max(maxLeft,maxRight,maxLeftSum+maxRightSum)

#大大招，时间复杂度为：O(n)
def max(*a):
    max=0
    for i in a:
        if i>max:
            max=i
    return max


def maxSubSum3(*a):
    max=0
    thisMax=0
    for i in a:
        thisMax+=i
        if thisMax>max:
            max=thisMax
        if thisMax<0:
            thisMax=0
    return max

if __name__=='__main__' :
    print maxSubSum1(-1,11,-4,13,-5,-2)
    print maxSubSum2(0,5,-1, 11, -4, 13, -5, -2)
    print maxSubSum3(-1, 11, -4, 13, -5, -2)