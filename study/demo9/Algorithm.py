# 递归的两个特点：1.调用自身  2.结束条件
#
# 算法（Algorithm）：一个计算过程，解决问题的方法
#     时间复杂度：用来评估算法运行效率的一个东西
#     空间复杂度：用来评估算法内存占用大小的一个式子
#
#     时间复杂度是用来估计算法运行时间的一个式子（单位）。
#     一般来说，时间复杂度高的算法比复杂度低的算法慢。
#     常见的时间复杂度（按效率排序）
#     O(1)<O(logn)<O(n)<O(nlogn)<O(n**2)<O(n**2logn)<O(n**3)
#     不常见的时间复杂度（看看就好）
#     O(n!) O(2n) O(nn) …
#
# 1.冒泡排序： 首先，列表每两个相邻的数，如果前边的比后边的大，那么交换这两个数……
#            如果冒泡排序中执行一趟而没有交换，则列表已经是有序状态，可以直接结束算法。
def bubble_sort(li):
    for i in range(len(li) - 1):
        exchange = False
        for j in range(len(li) - i - 1):
            if li[j] > li[j+1]:
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            break
    return li
# 2.选择排序：  一趟遍历记录最小的数，放到第一个位置；
#             再一趟遍历记录剩余列表中最小的数，继续放置；
def select_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i+1,len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
    return li
# 3.插入排序：   列表被分为有序区和无序区两个部分。最初有序区只有一个元素。
#               每次从无序区选择一个元素，插入到有序区的位置，直到无序区变空
def insert_sort(li):
    for i in range(1, len(li)):
        tmp = li[i]
        j = i - 1
        while j >= 0 and li[j] > tmp:
            li[j+1]=li[j]
            j = j - 1
        li[j + 1] = tmp
    return li
# 优化空间：应用二分查找来寻找插入点（并没有什么卵用）

# 4.快速排序：    取一个元素p（第一个元素），使元素p归位；
#                 列表被p分成两部分，左边都比p小，右边都比p大；
#                递归完成排序。
def quick_sort(data,left,right):
    if left < right:
        mid = partition(data,left,right)
        quick_sort(data,left,mid - 1)
        quick_sort(data,mid + 1,right)
        return data
def partition(data,left,right):
   tmp = data[left]
   while left < right:
       while left < right and data[right] >= tmp:
           right -= 1
       data[left] = data[right]
       print(data[left])
       while left < right and data[left] <= tmp:
           left += 1
       data[right] = data[left]
   data[left] = tmp
   return left
# 问题：极端情况下排序效率低
#
# 树是一种数据结构（比如：目录结构）
# 一些概念根节点、叶子节点，树的深度（高度），树的度，，孩子节点/父节点，子树
# 二叉树：度不超过2的树（节点最多有两个叉）
# 特殊的二叉树：满二叉树，完全二叉树
# 二叉树存储方式：链式存储方式，顺序存储方式（列表）
# 父节点和左(右)孩子节点的编号下标有什么关系：i -> 2i+1 (i -> 2i+2)
# 完全二叉树可以用列表来存储，通过规律可以从父亲找到孩子或从孩子找到父亲
#
# 堆:
# 大根堆：一棵完全二叉树，满足任一节点都比其孩子节点大
# 小根堆：一棵完全二叉树，满足任一节点都比其孩子节点小
# 当根节点的左右子树都是堆时，可以通过一次向下的调整来将其变换成一个堆
# 5.堆排序:   建立堆(大根堆，小根堆)
#             得到堆顶元素，为最大元素（调整）
#             去掉堆顶，将堆最后一个元素放到堆顶，此时可通过一次调整重新使堆有序。
#             堆顶元素为第二大元素。
#             重复步骤3，直到堆变空。
def sift(data, low, high):
    i = low
    j = 2 * i + 1
    tmp = data[i]
    while j <= high:
        if j < high and data[j] < data[j + 1]:
            j += 1
        if tmp < data[j]:
            data[i] = data[j]
            i = j
            j = 2 * i + 1
        else:
            break
        data[i] = tmp
def heap_sort(data):
    n = len(data)
    for i in range(n // 2 - 1, -1, -1):
        sift(data, i, n - 1)
    for i in range(n - 1, -1, -1):
        data[0], data[i] = data[i], data[0]
        sift(data, 0, i - 1)
    return data

# 6.归并排序：    分解：将列表越分越小，直至分成一个元素。
#                 一个元素是有序的。
#                 合并：将两个有序列表归并，列表越来越大。
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
    li[low:high+1] = ltmp
def merge_sort(li, low, high):
    if low < high:
        mid = (low + high) // 2
        merge_sort(li,low, mid)
        merge_sort(li, mid+1, high)
        merge(li, low, mid, high)
    return li

# 7.希尔排序： 希尔排序是一种分组插入排序算法。
def shell_sort(li):        #相对有序的，缺少最后一次排序的
    gap = int(len(li) // 2)
    while gap >= 1:
        for i in range(gap, len(li)):
            tmp = li[i]
            j = i - gap
            while j >= 0 and tmp < li[j]:
                li[j + gap] = li[j]
                j -= gap
            li[i - gap] = tmp
        gap = gap // 2
    return li

