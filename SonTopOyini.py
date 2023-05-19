from random import randint
print("Keling o'ylagan sonni topish o'yinini o'ynaymiz")
def son_top(x=10):
    tasodifiy_son=randint(1,x)
    print(f"Men 1 dan {x} gacha son o'yladim topa olasizmi")
    urinish=0
    while True:
        urinish+=1
        taxmin=int(input(">>>"))
        if taxmin<tasodifiy_son:
            print("Xato men o'ylagan son bundan kattaroq yana harakat qiling")
        elif taxmin>tasodifiy_son:
            print("Xato men o'ylagan son bundan kichikroq yana harakat qiling")
        else:
            break
    print(f"Tabriklaymiz siz {urinish} ta urinishda topdiz")
    return urinish




def son_top_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugmani bosing.Men topaman")
    quyi=1
    yuqori=x
    urinish_pc=0
    while True:
        urinish_pc+=1
        if quyi!=yuqori:
            taxmin_pc=randint(quyi,yuqori)
        else:
            taxmin_pc=quyi
        javob=input(f"Siz {taxmin_pc}sonini o'yladingiz:to'g'r(t),"
                    f"men o'ylagan son bundan kattaroq (+),yoki kichikroq(-)".lower())
        if javob=="-":
            yuqori=taxmin_pc-1
        elif javob=="+":
            quyi=taxmin_pc+1
        else:
            break
    print(f"Topdim {urinish_pc} ta urinishda")
    return urinish_pc
def play(x=10):
    yana=True
    while yana:
        taxminlar_user=son_top()
        taxminlar_pc=son_top_pc()

        if taxminlar_user>taxminlar_pc:
            print("Men yutdim")
        elif taxminlar_user<taxminlar_pc:
            print("Siz yutdingiz")
        else:
            print("Durrang")
        yana=int(input("Yana o'ynaysizmi Ha(1)/Yo'q(0)"))
play()