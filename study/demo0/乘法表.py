a = 1
while a <= 9 :
    b = 1
    while b <= a :
        print(str(b)+"*"+str(a)+"="+str(b*a),end="\t")
        b += 1
    print()
    a += 1

#print("\n".join("\t".join(["%s*%s=%s" %(x,y,x*y) for y in range(1, x+1)]) for x in range(1, 10)))