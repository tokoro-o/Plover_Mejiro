#*NTSKYAIOotkn#*NTSKYAIOotkn
#正規表現(Regex)を有効化すると宣言するよ
import re

#打鍵が続けられる長さを指定するよ (Plover Python dictionary)
LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    stroke = key[0]

#ストロークが*か*-*か#のときにKeyErrorを出すよ    
    if stroke == "*" or stroke == "*-*" or stroke == "#":
        raise KeyError

    #打鍵されたキーを正規表現で見て、グループ化するよ
    regex = re.compile(r"(\*?)(N?T?S?K?)(Y?A?I?O?o?)(t?k?n?)(\-?#?)(\*?)(N?T?S?K?)(Y?A?I?O?o?)(t?k?n?)")
    regex_groups = re.search(regex, stroke)

    #グループ化したキーの呼び方を決めてるよ、グループは1から始まるよ
    LeftAsterisk = regex_groups.group(1)
    LeftConsonant = regex_groups.group(2)
    LeftVowel = regex_groups.group(3)
    LeftParticle = regex_groups.group(4)
    MiddleHyphen = regex_groups.group(5)
    RightAsterisk = regex_groups.group(6)
    RightConsonant = regex_groups.group(7)
    RightVowel = regex_groups.group(8)
    RightParticle = regex_groups.group(9)

    #↓のprintって書いてあるやつは、デバッグ用のコンソールに表示されるよ
    print("LeftAsterisk\tLeftConsonant\tLeftVowel\tLeftParticle")
    print(LeftAsterisk + "\t\t" + LeftConsonant + "\t\t" + LeftVowel + "\t\t" + LeftParticle)

    print("RightAsterisk\tRightConsonant\tRightVowel\tRightParticle")
    print(RightAsterisk + "\t\t" + RightConsonant + "\t\t" + RightVowel + "\t\t" + RightParticle)

    #return

    #頻出順→『n,t,k,s, r,m,h,d,g,w ,z,b,j,p』
    if LeftVowel == "AIO" or LeftVowel == "AIo" or LeftVowel == "AOo":
          LeftVowel = "AIOo"
    if RightVowel == "AIO" or RightVowel == "AIo" or RightVowel == "AOo":
          RightVowel = "AIOo"
    def Make(Conso,Vowel):
        Consonants = ["n","t","k","s","r","m","h","d","g","w","z","b","p","v","x"]
        listconsonant = ["N","T","K","S","TK","NS","NT","TS","NK","SK","NSK","NTS","NTK","TSK","NTSK"]

        Vowels = ["a","i","o","ou","e","ae","uu","oo","xn","you","ya","yu","yo","yuu","ei","ai","ii","oi","ui"]
        listvowel = ["A","I","O","o","AI","AO","Io","Oo","AIOo","Y","YA","YI","YO","Yo","YAI","YAO","YIo","YOo","YAIOo"]

        output = ""

        if Conso == "":
                if Vowel == "":
                      #母音も子音も何もなかったら出力も無
                      output = ""
                else:
                      #母音だけなら母音リストの出番！
                      output = Vowels[listvowel.index(Vowel)]
        else:
                #子音の入力があればとりあえずその子音を入れる
                output = Consonants[listconsonant.index(Conso)]
                if Vowel == "":#母音の入力が無かったらウ行を送ることにしてるよ
                        if output == "w":
                               output = "u"
                        else:
                               output += "u"
                elif Vowel == "AIOo":
                       #略語
                       output = ""
                else:
                       output += Vowels[listvowel.index(Vowel)]
        print(output)
        return output

    resultL = Make(LeftConsonant,LeftVowel)
    resultR = ""

    if resultL != "":#ひだりに入力がある時だけ右の音を出すよ
           resultR = Make(RightConsonant,RightVowel)
    else:#略語を出力するよ
           resultR = ""

    listParticle = ["n","t","k","tk","tn","kn","tkn"]
    listSW = ["xn","tu","ku","xtu","ti","ki","-"]#SWはセカンドワードつまり二音目
    #LeftParticleになにかあって左の指の入力もあるとき
    if LeftParticle != "" and resultL != "":
        resultL += listSW[listParticle.index(LeftParticle)]
    #RightParticleになにかあって右の指の入力もあるとき
    if RightParticle != "" and resultR != "":
        resultR += listSW[listParticle.index(RightParticle)]

    result = ""

    if resultL == "" and LeftParticle != "" or resultR == "" and RightParticle != "":
        #略語
        result = ""
    else:
        result = resultL + resultR
    #↓、デバッグ用のコンソールに表示されるよ
    print(result)
    #↓、「{^^}」でスペースをなくす出力をしてるよ
    return "{^" + result + "^}"
