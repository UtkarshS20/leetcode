def longestCommonPrefix(strs: list[str]) -> str:
    strs = sorted(strs)
    output = ""
    for string in strs:
        for index in range(len(string)):
            if strs[0][index] == strs[-1][index]:
                output = output + string[index]
            else:
                break
        break
    return output

strs = ["flower","flow","flight"]

print(longestCommonPrefix(strs))