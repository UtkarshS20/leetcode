def strStr(haystack: str, needle: str) -> int:
    # index = 0
    # hay_list = haystack.split(needle)
    # if needle not in haystack:
    #     return -1
    # elif hay_list[0] == '':
    #     return 0
    # else:
    #     for i in range(len(hay_list)):
    #         print(hay_list[i])
    #         if hay_list[i] != '':
    #             index = index + len((hay_list)[i])
    #             # index = 0
    #         else:
    #             break
    #     return index - 1
     return haystack.find(needle)
                
            
        # print(hay_list)
        # return len(hay_list[0]) 
    # for i in haystack:
    #     for 
    
    
haystack = "abc"
needle = "c"
# haystack = "hello"
# needle = "ll"
print(strStr(haystack=haystack, needle=needle))
