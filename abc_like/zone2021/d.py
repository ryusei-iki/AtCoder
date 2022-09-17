# s=input()
# turn=-1
# t=''
# for i in range(len(s)):
#     if(s[i]=='R'):
#         turn=turn*(-1)
#     else:
#         if(turn==1):
#             if(len(t)==0):
#                 t=s[i]+t
#             else:
#                 if(t[0]==s[i]):
#                     t=t[1:]
#                 else:
#                     t=s[i]+t
#         else:
#             # print(s,i)
#             # print(t)
#             if(len(t)==0):
#                 t=t+s[i]
#             else:
#                 if(t[-1]==s[i]):
#                     t=t[:-1]
#                 else:
#                     t=t+s[i]
# if(turn==1):
#     print(t[::-1])
# else:
#     print(t)
#
s=input()
turn=-1
t=[]
for i in range(len(s)):
    if(s[i]=='R'):
        turn=turn*(-1)
    else:
        if(turn==1):
            if(len(t)==0):
                t.insert(0,s[i])
            else:
                if(t[0]==s[i]):
                    t.pop(0)
                else:
                    t.insert(0,s[i])
        else:
            # print(s,i)
            # print(t)
            if(len(t)==0):
                t.append(s[i])
            else:
                if(t[-1]==s[i]):
                    t.pop(-1)
                else:
                    t.append(s[i])
ans=''
for i in range(len(t)):
    ans=ans+t[i]
if(turn==1):
    print(ans[::-1])
else:
    print(ans)
