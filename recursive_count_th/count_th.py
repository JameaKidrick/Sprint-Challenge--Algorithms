'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
arr = []
def count_th(word):
    count = 0
    if 'th' not in word:
        global arr
        count = len(arr)
        arr = []
        print(count)
        return count
    else:
        arr.append('th')
        word = word.replace('th', 'a', 1)

    return count_th(word)


# count_th('worthy') # 1
# count_th('') # 0
# count_th("abcthxyz") # 1
# count_th("abcthefthghith") # 3
# count_th("thhtthht") # 2
# count_th("THtHThth") # 1