def lengthOfLastWord(s: str) -> int:
    s_list = s.split(" ")
    for i in range(len(s_list)-1, -1, -1):
        if len(s_list[i]) != 0:
            # print(s_list[i])
            return len(s_list[i])
            # continue
        # else:
        #     print()
            
        
        
# s = "Hello World"
s = "   fly me   to   the moon  "
# s = "luffy is still joyboy"
print(lengthOfLastWord(s))