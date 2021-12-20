# to be sorted
stringsList = [
    'apply',
    'drop',
    'count',
    'balance',
]
# sort all strings
""" stringsList = [
    'alppy',
    'dopr',
    'cnotu',
    'aabceln',
] """
# sort array by strings
""" stringsList = [
    'aabceln',
    'alppy',
    'cnotu',
    'dopr',
] """
# sorting strings in list
class sorting:
    def mergeSort(list):
        # 分割：到每列表只剩 1 元素為止
        if len(list) > 1:
            mid = len(list) // 2
            left_list = list[:mid] # 0 ~ mid - 1 => Left
            right_list = list[mid:] # mid ~ end => Right

            sorting.mergeSort(left_list)
            sorting.mergeSort(right_list)

            # 整合
            right_index = 0
            left_index = 0
            merged_index = 0
            # 從兩列表的第一項開始比較大小，依序往後比較
            while right_index < len(right_list) and left_index < len(left_list):
                # 較小的數值先放入最終的合併列表中
                if right_list[right_index] < left_list[left_index]:
                    list[merged_index] = right_list[right_index]
                    # 被放入的數值的列表的 index 往後一位
                    right_index = right_index + 1
                else:
                    list[merged_index] = left_list[left_index]
                    left_index = left_index + 1
                # 合併列表的 index 往後一位
                merged_index = merged_index + 1

            # 放入右列表剩餘項
            while right_index < len(right_list):
                list[merged_index] = right_list[right_index]
                right_index = right_index + 1
                merged_index = merged_index + 1

            # 放入左列表剩餘項
            while left_index < len(left_list):
                list[merged_index] = left_list[left_index]
                left_index = left_index + 1
                merged_index = merged_index + 1

    def mergeSortWithDifferentType(toBeSorted):
        varType = type(toBeSorted)
        # 排序字串
        if varType == str:
            toBeSorted = list(toBeSorted)
            sorting.mergeSort(toBeSorted)
            toBeSorted = "".join(toBeSorted)
        # 排序列表，先兩兩比較 string 後再排序
        elif varType == list:
            sorting.mergeSort(toBeSorted)
        return toBeSorted


def sortStringsInList(stringsList):
    for string in stringsList:
        stringIndex = stringsList.index(string)
        stringsList[stringIndex] = sorting.mergeSortWithDifferentType(string)

    sorting.mergeSort(stringsList)

    return stringsList
    
result = sortStringsInList(stringsList)
print(result)
