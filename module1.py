from random import *
def arvud_loendis():
    """ Sortiruet zadanij spisok
    zaprashivaet koli4estvo generiruemih 4isel
    zaprashivaet diapazon 4isel minimum i maksimum
    generiruet 4isla (v zadanom diapazone) v spiske
        pri nepravilno zadanih min zna4enii i maks zna4enii menjaet ih mestami
    sortiruet spisok ot naimenshego do bolshego
    sozdaet otdelnie spiski s negativnimi, polozhitelnimi 4islami i nuljami
    s4itaet srednie 4isla v polozitelnom spiske i negativom spiske
    dobavljaet srednie 4isla v izna4alnii spisok
    sortiruet spisok
    """
    print("Данные:")
    n=abs(int(input("Сколько целых чисел генерируем в список? => ")))
    mini=int(input("Введите минимальное число диапазона => "))
    maxi=int(input("Введите максимальное число диапазона => "))
    if mini>maxi:
        mini,maxi=vahetus(mini,maxi)
    s=[]
    generaator(n,s,mini,maxi)
    print()
    print("Результаты:")
    print("Полученный список от",mini,"до",maxi,s)
    s.sort()
    print("Отсортированный список",s)
    pos=[]
    neg=[]
    null=[]
    jagamine(s,pos,neg,null)
    print("Список положительных элементов",pos)
    print("Список отрицательных элементов",neg)
    print("Список нулевых элементов",null)
    kesk=keskmine(pos)
    lisamine(s,kesk)
    print("Среднее положительных:",kesk)
    kesk=keskmine(neg)
    lisamine(s,kesk)
    print("Среднее отрицательных:",kesk)
    print("Добавляем средние в изначалный массив:")
    s.sort()
    print(s)

def vahetus(a:int,b:int):
    """Menjaet dva zna4enija mesdu dvumja peremenjimi
    Vosvrashaet pomenenije peremenie
    :param int a: pervoja peremenaja
    :param int b: vtoraja peremenaja
    rtype: int
    """
    abi=a
    a=b
    b=abi
    return a,b

def generaator(n:int,loend,a:int,b:int):
    """ generiruet spisk
    :param int n: koli4estvo tsifr
    :param list loend: spisok v kotorom budut sgenerirovani tsifri
    :param int a: minimalnoe zna4enie
    :param int b: maksimalnoe zna4enie
    """
    for i in range (n):
        loend.append(randint(a,b))
    

def jagamine(loend,p,n,nol):
    """otdeljaet positivnie 4isla ot nigativnih i otdeljaet nuli v otdelnie spiski
    :param list loend: spisk so vsemi zna4enijami
    :param list p: spisk s positivom
    :param list n: spisk s negativom
    :param list nol: spisk s nuljami
    """
    for el in loend:
        if el>0:
            p.append(el)
        elif el<0:
            n.append(el)
        else:
            nol.append(el)

def keskmine(loend):
    """nahodit srednie zna4enie v spiske
    vosvrashaet srednie zna4enie
    :param list loend: spisok v kotorom ishut srednie 4islo
    rtype: float
    """
    n=len(loend)
    if n==0:
        kesk=0
    else:
        sum=0
        for i in loend:
            sum+=i
        kesk=round(sum/n,2)
    return kesk

def lisamine(loend,el:float):
    """dobavljaet zadanoe zna4enie v zadanii spisk spisok
    :param list loend: spisok v kotorii dobavitsja zna4enie
    :param float el: element kotorii dobavitsja v spisk
    """
    loend.append(el)
    loend.sort()