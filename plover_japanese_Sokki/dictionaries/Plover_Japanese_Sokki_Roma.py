#*TKNSYOIEetkn#*TKNSOIEetkn
#正規表現(Regex)を有効化すると宣言するよ
import re

#打鍵が続けられる長さを指定するよ (Plover Python dictionary)
LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    stroke = key[0]

#ストロークが*か*-*か#のときにKeyErrorを出すよ    
    if stroke == "*" or stroke == "*-*" or stroke == "#" or stroke == "*":
        raise KeyError

    #打鍵されたキーを正規表現で見て、グループ化するよ
    regex = re.compile(r"(\*?)(T?K?N?S?)(Y?)(O?I?E?e?)(t?k?n?)(\-?#?)(\*?)(T?K?N?S?)(Y?)(O?I?E?e?)(t?k?n?)")
    regex_groups = re.search(regex, stroke)
    #グループは1から始まる
    LeftAsterisk = regex_groups.group(1)
    LeftConsonant = regex_groups.group(2)
    LeftY = regex_groups.group(3)
    LeftVowel = regex_groups.group(4)
    LeftParticle = regex_groups.group(5)
    MiddleHyphen = regex_groups.group(6)
    RightAsterisk = regex_groups.group(7)
    RightConsonant = regex_groups.group(8)
    RightY = regex_groups.group(9)
    RightVowel = regex_groups.group(10)
    RightParticle = regex_groups.group(11)

    print("LeftAsterisk\tLeftConsonant\tLeftVowel\tLeftParticle")
    print(LeftAsterisk + "\t\t" + LeftConsonant + "\t\t" + LeftVowel + "\t\t" + LeftParticle)

    print("RightAsterisk\tRightConsonant\tRightVowel\tRightParticle")
    print(RightAsterisk + "\t\t" + RightConsonant + "\t\t" + RightVowel + "\t\t" + RightParticle)

    #頻出順→『n,t,k,s,r,m,h,d,g,w,z,b,j,p』

    Consonants =    ["","t","k","s","n","r","m","h","d","g","w","z","b","p","v","x"]
    listconsonant = ["","T","K","S","N","TS","KN","TK","KNS","NS","TKNS","KS","TKS","TKN","TNS","TN"]

    Vowels =    ["u","o","i","oi","ei","a","e","ou","ii","ui"]
    Vowels2 =   ["you","ya","yuu","yo","yu","ai","ae","oo","aa","uu"]
    listvowel = ["","O","I","E","e","OI","Ie","OE","Ee","OIE"]

    if LeftVowel not in listvowel:
         LeftVowel = listvowel[9]
    if RightVowel not in listvowel:
         RightVowel = listvowel[9]

    def Make(Conso,Ys,Vowel):

        output = ""
        
        if not Conso and not Ys and not Vowel:
             output = ""
        else:
            if Ys and Consonants[listconsonant.index(Conso)] == "v":
                output = "f"
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
            elif output == "fae":
                output = "thi"
            elif output == "foo":
                output = "the"
            elif output == "faa":
                output = "thethe"
            elif output == "fuu":
                output = "thu"

        print(output)
        return output

    resultL = Make(LeftConsonant,LeftY,LeftVowel)
    resultR = ""
    result = ""

    if resultL:#ひだりに入力がある時だけ右の音を出す
           resultR = Make(RightConsonant,RightY,RightVowel)

    listParticle = ["n","t","k","tk","tn","kn","tkn",""]
    listSW = ["xn","tu","ku","xtu","ti","ki","-",""]#SWはセカンドワードつまり二音目
    listLParticle = ["no","te","ka","de","na","ni","mo",""]
    listOnlyLParticle = ["nai","te","ga","to","na","wo","ya",""]
    listRParticle = ["no","de","ka","xtute","ha","ni","mo",""]
    #LeftParticleになにかあって左の指の入力もあるとき
    if LeftParticle and resultL:
        resultL += listSW[listParticle.index(LeftParticle)]
    #RightParticleになにかあって右の指の入力もあるとき
    if RightParticle and resultR:
        resultR += listSW[listParticle.index(RightParticle)]
    if  not resultL and not resultR:#どちらの指にも入力が無いとき
        if LeftParticle and not RightParticle:
            #左親指だけの時
            result = listOnlyLParticle[listParticle.index(LeftParticle)]
        else:
            if listParticle.index(LeftParticle) == 0 and listParticle.index(RightParticle) == 0:
                result = "xn"
            elif listParticle.index(LeftParticle) == 2 and listParticle.index(RightParticle) == 2:
                result = "kana"
            elif listParticle.index(LeftParticle) == 3 and listParticle.index(RightParticle) == 1:
                result = "koto"
            elif listParticle.index(LeftParticle) == 3 and listParticle.index(RightParticle) == 3:
                result = "xtu"
            elif listParticle.index(LeftParticle) == 4 and listParticle.index(RightParticle) == 1:
                result = "nanide"
            elif listParticle.index(LeftParticle) == 4 and listParticle.index(RightParticle) == 2:
                result = "nanika"
            elif listParticle.index(LeftParticle) == 4 and listParticle.index(RightParticle) == 4:
                result = "naniga"
            elif listParticle.index(LeftParticle) == 4 and listParticle.index(RightParticle) == 6:
                result = "nanimo"
            elif listParticle.index(LeftParticle) == 5 and listParticle.index(RightParticle) == 5:
                result = "nowo"
            elif listParticle.index(LeftParticle) == 6 and listParticle.index(RightParticle) == 6:
                result = "mono"
            else:
                result = listLParticle[listParticle.index(LeftParticle)] + listRParticle[listParticle.index(RightParticle)]
    elif not resultL and resultR:
        #左略語
        raise KeyError
    elif LeftParticle and not resultL or RightParticle and not resultR:
        #略語
        raise KeyError
    else:
        result = resultL + resultR
    #↓デバッグ用のコンソールに結果を表示
    print(result)
    #↓「{^^}」でスペースをなくす
    return "{^" + result + "^}"