def jumbled_letters():

    z=int(input("Enter the number of test cases: "))

    for k in range(z):

        a= str(input("Enter the sentence: "))
        b=str(a.replace(" ", ""))

        c = len(b)
        s1=[]

        ochar=[]
        echar=[]

        for i in  range(0,c):
            if i%2==0:
                echar.append(b[i])
            else:
                ochar.append(b[i])
        ochar.reverse()

        z=len(ochar)
        for q in range(z):
            echar.append(ochar[q])
        
        ea=str("".join(echar))
    
        print(ea)

if __name__ == "__main__":
    jumbled_letters()
