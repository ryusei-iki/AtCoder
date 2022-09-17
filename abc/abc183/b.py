#@
sx,sy,gx,gy=map(int,input().split())

kata=(sy+gy)/(sx-gx)

b=sy-kata*sx

print(-b/kata)
