import random as rd
gens=["Othman","Aya","Mehdi","Nour","Adem","Yanis","Alex","Noureddine","Alexandre","Aminata","Clément","Dayna","Fatima","Ismaël","Jeras","Kevindra","Nolan","Ruben","Rémi","Sidy","Tom","Walid","Yassine","Youcef","Younes","Younouss Soussi"]


def Determine():
    Dico={}
    for i in gens:
        b=0
        for j in creadata(rd.randint(5,20)):
            for iti in j:
                if iti==i:
                    b+=200-(j.index(iti)*10)
        Dico[i]=round(b)
    return Dico


def one(n):
    L=[]
    if n<=len(gens):
        for i in range(n):
            a=rd.randint(0,len(gens)-1)
            while gens[a] in L:
                a=rd.randint(0,len(gens)-1)
            if gens[a] not in L:
                L.append(gens[a])

    if n> len(gens):
        print('C est trop grand bg')
    if n == 0:
        print()
    return L

def creadata(n):
    L=[]
    for i in range(n):
        a=rd.randint(0,len(gens)-1)
        if a ==0:
            a=rd.randint(0,len(gens)-1)

        b=one(a)
        L.append(b)
    return L

def Aide_Maj():
    Dico=Determine()
    a=0
    L=[]
    LL=[]
    Tri=[]
    for values in Dico.values():
        a+=values
    for index,i in enumerate(Dico):
        b= Dico[i]
        Pourcentage= (b*100)/a
        Pourcentage=round(Pourcentage,2)
        L.append((Pourcentage,index))
        Tri.append((Pourcentage,i))
    L=sorted(L)
    Tri=sorted(Tri)
    for item in range (len(Tri)):
        print("Dans la globalité de ton travail,",Tri[item][1],"t'as aidé(e) à:",Tri[item][0],"%")
    Aide= [index for Pourcentage,index in L[-1:]]
    for k in Aide:
        m=Dico.keys()
        m=list(m)
        LL.append(m[k])
    print()
    print("Donc celui qui t'as le plus aidé(e) est ",LL[0])