#from string import *
##1
#vokaali=["a","e","u","o","i","ü","ö","õ","ä"]
#konsonanti="qwrtpsdfghlkzxcvbnmj"
#markid=punctuation
#v=k=m=t=0
#tekst=input("Sisesta sõna või lause: ").lower()#ABCD->"abcd!"
#tekst_list=list(tekst) #["a","b","c","d","!"]
#for sümbol in tekst_list:
#    if sümbol in vokaali:
#        v+=1
#    elif sümbol in konsonanti:
#        k+=1
#    elif sümbol in markid:
#        m+=1
#    elif sümbol==" ":
#        t+=1
#print("vokaali:",v,"konsonanti:",k)
#print("markid:", m)
#print("Tühikud:",t)

#2
nimed=[]
for i in range(5):
    nimi=input("Sisesta nimed: ").capitalize
    nimed.append(nimi)

print("loetelu oli: ",nimed)
nimed.sort()
print("Loetelu sorteeritud: ",nimed)
for n in range(len(nimed)):
    print(n+1,". ",nimed[n],sep="")
print("Vimasena oli lisatud: ",nimi)

uued_nimed=[]
for nimi in nimed:
    if nimi not in uued_nimed:
        uued_nimed.append(nimi)
print(uued_nimed)

uued_nimed=list(set(nimed))