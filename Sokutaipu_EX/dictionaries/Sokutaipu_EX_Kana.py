#*YTKNSAIOUtkn#*YTKNSAIOUtkn
import re

LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    stroke = key[0]

    if stroke == "#":
        print("key error*")
        raise KeyError
    
    regex = re.compile(r"(\*?)(Y?)(T?K?N?S?)(A?I?O?U?)(t?k?n?)(\-?#?)(\*?)(Y?)(T?K?N?S?)(A?I?O?U?)(t?k?n?)(1?2?3?4?5?6?7?8?9?0?)")
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
    Numbers = regex_groups.group(12)

    LeftStroke = LeftConsonant + LeftVowel + LeftParticle
    RightStroke = RightConsonant + RightVowel + RightParticle
    print("LeftAsterisk\tLeftConsonant\tLeftVowel\tLeftParticle")
    print(LeftAsterisk + "\t\t" + LeftConsonant + "\t\t" + LeftVowel + "\t\t" + LeftParticle)

    print("RightAsterisk\tRightConsonant\tRightVowel\tRightParticle")
    print(RightAsterisk + "\t\t" + RightConsonant + "\t\t" + RightVowel + "\t\t" + RightParticle)

    print(stroke)
    #頻出順→『n,t,k,s,r,m,h,d,g,w,z,b,j,p』

    Consonants =    ["","t","k","n","s","h","m","z","g","r","d","w","p","x","b","f"]
    listconsonant = ["","T","K","N","S","TK","TN","TS","NS","KS","KN","TKN","TNS","TKNS","TKS","KNS"]

    #Vowels =    ["u","a","i","o","ii","e","ou","yuu","oo","ui"]
    #Vowels2 =   ["you","ai","ya","yo","yu","ei","oi","aa","ae","uu"]
    Vowels =    ["u","a","i","o","ya","e","ou","yuu","yu","aa"]
    Vowels2 =   ["you","ai","yo","oi","ui","ei","oo","ii","ae","uu"]
    listvowel = ["","A","I","O","U","AI","AO","IU","OU","AIO"]
    firstvowel = [["A","YA","YOU","AIO"],["I","YIU"],["","YU","YAIO"],["AI","YAI"],["O","AO","YO","YAO"],["U"],["OU","IU"],["Y","YI"]]# a,i,u,e,o,ya,yu,yo
    secondvowel = [["AIO"],["YU","YA","YIU","YO","YAI"],["AO","Y","IU","YAIO"],["YOU"],["YAO"]]# a,i,u,e,o
    ConsonantOrder = ["","k","s","t","n","h","m","r","w","g","d","z","b","p","f","x"]

    excepts_in = ["ni","nu","nyuu","nyou",
                  "mi","mu",
                  "wya","wyu","wyo","wyuu","wyou","wii","wui","wuu","wei",
                  "di","du","de","dya","dyo","dyuu","dyou","dii","dei",
                  "fu","fyuu","fyou"]
    excepts_out = ["ぬ","に","にょう","にゅう",
                   "む","み",
                   "やあ","いう","よね","ええ","うえ","ゐ","あお","うぅ","ゑ",
                   "てぃ","で","づ","ちぇ","しぇ","でぃ","でい","じぇ","ぢ",
                   "ヴ","くぁ","くぉ"]

    kana = [["あ","い","う","え","お","や","ゆ","よ"],
            ["か","き","く","け","こ","きゃ","きゅ","きょ"],
            ["さ","し","す","せ","そ","しゃ","しゅ","しょ"],
            ["た","ち","つ","て","と","ちゃ","ちゅ","ちょ"],
            ["な","に","ぬ","ね","の","にゃ","にゅ","にょ"],
            ["は","ひ","ふ","へ","ほ","ひゃ","ひゅ","ひょ"],
            ["ま","み","む","め","も","みゃ","みゅ","みょ"],
            ["ら","り","る","れ","ろ","りゃ","りゅ","りょ"],
            ["わ","うぃ","う","うぇ","を","うゃ","うゅ","うょ"],
            ["が","ぎ","ぐ","げ","ご","ぎゃ","ぎゅ","ぎょ"],
            ["だ","ぢ","づ","で","ど","でゃ","でゅ","でょ"],
            ["ざ","じ","ず","ぜ","ぞ","じゃ","じゅ","じょ"],
            ["ば","び","ぶ","べ","ぼ","びゃ","びゅ","びょ"],
            ["ぱ","ぴ","ぷ","ぺ","ぽ","ぴゃ","ぴゅ","ぴょ"],
            ["ふぁ","ふぃ","ヴ","ふぇ","ふぉ","ふゃ","ふゅ","ふょ"],
            ["ぁ","ぃ","ぅ","ぇ","ぉ","ゃ","ゅ","ょ"]]

    if LeftVowel not in listvowel:
         LeftVowel = listvowel[9]
    if RightVowel not in listvowel:
         RightVowel = listvowel[9]
    def searchVowel(Vowel):
        for i in range(len(firstvowel)):
            if Vowel in firstvowel[i]:
                answer = i
        return answer
    def searchVowel2(Vowel):
        answer = 99
        for i in range(len(secondvowel)):
            if Vowel in secondvowel[i]:
                answer = i
        if answer == 99:
            return 99
        else:
            return answer
    def Make(Ys,Conso,Vowel):

        output = ""
        かな = Consonants[listconsonant.index(Conso)]

        if Ys:
            #Yが入力されていたら
            かな += Vowels2[listvowel.index(Vowel)]
        else:
            #そうでないとき
            かな += Vowels[listvowel.index(Vowel)]

        if not Ys and not Conso and not Vowel:
            output = ""
        else:
            output = kana[ConsonantOrder.index(Consonants[listconsonant.index(Conso)])][searchVowel(Ys + Vowel)]
            if searchVowel2(Ys + Vowel) != 99:
                output += kana[0][searchVowel2(Ys + Vowel)]
            if かな in excepts_in:
                output = excepts_out[excepts_in.index(かな)]

        print(output)
        return output

    resultL = Make(LeftY,LeftConsonant,LeftVowel)
    resultR = ""
    result = ""

    if resultL or RightY or RightConsonant or RightVowel:#ひだりに入力がある時だけ右の音を出す
        resultR = Make(RightY,RightConsonant,RightVowel)

    listParticle = ["","n","t","k","tk","tn","kn","tkn"]
    listSecondWord = ["","ん","つ","く","っ","ち","き","ー"]
    listLParticle = ["","て","は","の","と","か","に","へ"]
    listRParticle = ["","、","." ,"," ,"を","で","が","も"]

    助詞in = ["は、","の、","と、","か、","に、","へ、","て.","は.","の.","と.","か.","に.","へ.","はを","へを","はで","へで","にが","へが","はも"]
    助詞out = ["ては","ての","を,","で,","が,","も,","ては","では","のは","とは","かは","には","へは","をは","をも","では","でも","での","もが","もは"]
    
    #LeftParticleになにかあって左の指の入力もあるとき
    if not LeftAsterisk and LeftParticle and (resultL or resultR):
        resultL += listSecondWord[listParticle.index(LeftParticle)]
        print(resultL)
    #RightParticleになにかあって右の指の入力もあるとき
    if not RightAsterisk and RightParticle and (resultR or resultL and LeftParticle or LeftAsterisk):
        resultR += listSecondWord[listParticle.index(RightParticle)]
        print(resultR)
    elif  not resultL and not resultR:#どちらの指にも入力が無いとき
        if not Numbers:
            result = listLParticle[listParticle.index(LeftParticle)] + listRParticle[listParticle.index(RightParticle)]
            if result in 助詞in:
                result = 助詞out[助詞in.index(result)]
        else:
            result = Numbers
            if "#" in MiddleHyphen:
                if result == 0:
                    result = 11
                result = "}{#F" + Numbers + "}{"

    if result == "":
        result = resultL + resultR

    if (resultL or resultR) and "#" in MiddleHyphen:
        print("{^" + result * 2 + "^}")
        return "{^" + result * 2 + "^}"
    else:
        print("{^" + result + "^}")
        return "{^" + result + "^}"