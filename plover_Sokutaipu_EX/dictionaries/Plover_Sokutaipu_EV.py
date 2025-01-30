#*YTHKSAIOXtkn#*YTHKSAIOXtkn
import re

LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    stroke = key[0]

    if stroke == "*-" or stroke == "-*" or stroke == "*-*" or stroke == "#":
        raise KeyError

    regex = re.compile(r"(\*?)(Y?)(T?H?K?S?)(A?I?O?X?)(t?k?n?)(\-?#?)(\*?)(Y?)(T?H?K?S?)(A?I?O?X?)(t?k?n?)")
    regex_groups = re.search(regex, stroke)

    LeftAsterisk = regex_groups.group(1)
    LeftY = regex_groups.group(2)
    LeftConsonant = regex_groups.group(3)
    LeftVowel = regex_groups.group(4)
    LeftParticle = regex_groups.group(5)
    MiddleHyphen = regex_groups.group(6)
    RightAsterisk = regex_groups.group(7)
    RightY = regex_groups.group(8)
    RightConsonant = regex_groups.group(9)
    RightVowel = regex_groups.group(10)
    RightParticle = regex_groups.group(11)

    print("LeftAsterisk\tLeftConsonant\tLeftVowel\tLeftParticle")
    print(LeftAsterisk + "\t\t" + LeftConsonant + "\t\t" + LeftVowel + "\t\t" + LeftParticle)

    print("RightAsterisk\tRightConsonant\tRightVowel\tRightParticle")
    print(RightAsterisk + "\t\t" + RightConsonant + "\t\t" + RightVowel + "\t\t" + RightParticle)

    #頻出順→『n,t,k,s,r,m,h,d,g,w,z,b,j,p』

    Consonants =    ["","t","h","k","s","b","m","z","d","r","n","p","w","x","v","b"]
    listconsonant = ["","T","H","K","S","TH","TK","TS","HK","HS","KS","THK","TKS","THKS","THS","HKS"]

    Vowels =    ["u","a","i","o","oi","e","ou","ii","oo","uu"]
    Vowels2 =   ["you","ai","yuu","yo","yu","ei","ae","yu","aa","ui"]
    listvowel = ["","A","I","O","X","AI","AO","IX","OX","AIO"]

    if LeftVowel not in listvowel:
         LeftVowel = listvowel[9]
    if RightVowel not in listvowel:
         RightVowel = listvowel[9]

    def Make(Ys,Conso,Vowel):

        output = ""
        
        if not Ys and not Conso and not Vowel:
            output = ""
        else:
            output = Consonants[listconsonant.index(Conso)]

            if Ys:
                #Yが入力されていたら
                output += Vowels2[listvowel.index(Vowel)]
            else:
                #そうでないとき
                output += Vowels[listvowel.index(Vowel)]

            if output == "wu":
                output = "u"
            elif output == "wya":
                output = "uxa"
            elif output == "wyu":
                output = "uxe"
            elif output == "wyuu":
                output = "uxi"
            elif output == "wyo":
                output = "uxo"
            elif output == "dyuu":
                output = "dhi"
            elif output == "dyu":
                output = "dhu"

        print(output)
        return output

    resultL = Make(LeftY,LeftConsonant,LeftVowel)
    resultR = ""
    result = ""

    if resultL:#ひだりに入力がある時だけ右の音を出す
        resultR = Make(RightY,RightConsonant,RightVowel)

    listParticle = ["","n","t","k","tk","tn","kn","tkn"]
    listSecondWord = ["","xn","tu","ku","xtu","ti","ki","-"]
    listLParticle = ["","no","te","ka","de","na","ni","mo"]
    listRParticle = ["","no","de","ka","xtute","ha","ni","mo"]
    listOnlyLParticle = ["","nai","te","ga","to","na","wo","ya"]

    #LeftParticleになにかあって左の指の入力もあるとき
    if LeftParticle and resultL:
        resultL += listSecondWord[listParticle.index(LeftParticle)]
    #RightParticleになにかあって右の指の入力もあるとき
    if RightParticle and resultR:
        resultR += listSecondWord[listParticle.index(RightParticle)]

    if  not resultL and not resultR:#どちらの指にも入力が無いとき
        if LeftParticle and not RightParticle:
            #左親指だけの時
            result = listOnlyLParticle[listParticle.index(LeftParticle)]
        else:
            Particle = LeftParticle + RightParticle
            if Particle == "nn":
                result = "xn"
            elif Particle == "kk":
                result = "kana"
            elif Particle == "tkt":
                result = "koto"
            elif Particle == "tktk":
                result = "xtu"
            elif Particle == "tnt":
                result = "nanide"
            elif Particle == "tnk":
                result = "nanika"
            elif Particle == "tntn":
                result = "naniga"
            elif Particle == "tntkn":
                result = "nanimo"
            elif Particle == "knkn":
                result = "nowo"
            elif Particle == "tkntkn":
                result = "mono"
            else:
                result = listLParticle[listParticle.index(LeftParticle)] + listRParticle[listParticle.index(RightParticle)]
    elif not resultL and resultR:
        #左略語
        raise KeyError
    elif LeftParticle and not resultL or RightParticle and not resultR:
        #その他略語
        raise KeyError
    else:
        result = resultL + resultR
    #↓デバッグ用のコンソールに結果を表示
    print(result)
    #↓「{^^}」でスペースをなくす
    return "{^" + result + "^}"