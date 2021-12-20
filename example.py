# to be sorted
stringsArray = [
    'apply',
    'balance',
    'count',
    'drop',
]
# sort all strings
stringsArray = [
    'alppy',
    'aabceln',
    'cnotu',
    'dopr',
]
# sort array by strings
stringsArray = [
    'aabceln',
    'alppy',
    'cnotu',
    'dopr',
]

# TODO:
def mergeSort(toBeSorted):
    varType = type(toBeSorted)
    if varType == 'str':
        # mergeSort String
        return
    elif varType == 'list':
        # 先兩兩比較 string 後再排序
        return

def sortStringsInArray(stringsArray):
    for string in stringsArray:
        mergeSort(string)
    # TODO:
    mergeSort(stringsArray)
    
sortStringsInArray(stringsArray)
