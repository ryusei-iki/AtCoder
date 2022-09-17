K=int(input())
k_b=0
count=0
for i in range(1,K+1):
    if(abs(i-k_b)<2):
        count=count+1

print(count)
