#*YTHKSAIOXtkn#*YTHKSAIOXtkn
import re

LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    stroke = key[0]

    if stroke == "*" or stroke == "*-*" or stroke == "-*" or stroke == "*-" or stroke == "#":
        print("key error*")
        raise KeyError
    
    regex = re.compile(r"(\*?)(Y?)(T?H?K?S?)(A?I?O?X?)(t?k?n?)(\-?#?)(\*?)(Y?)(T?H?K?S?)(A?I?O?X?)(t?k?n?)(1?2?3?4?5?6?7?8?9?0?)")
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

    print("LeftAsterisk\tLeftConsonant\tLeftVowel\tLeftParticle")
    print(LeftAsterisk + "\t\t" + LeftConsonant + "\t\t" + LeftVowel + "\t\t" + LeftParticle)

    print("RightAsterisk\tRightConsonant\tRightVowel\tRightParticle")
    print(RightAsterisk + "\t\t" + RightConsonant + "\t\t" + RightVowel + "\t\t" + RightParticle)

    #頻出順→『n,t,k,s,r,m,h,d,g,w,z,b,j,p』

    Consonants =    ["","n","k","t","s","h","m","z","g","r","d","w","p","x","b","f"]
    listconsonant = ["","T","H","K","S","TH","TK","TS","KS","HS","HK","THK","TKS","THKS","THS","HKS"]

    #Vowels =    ["u","a","i","o","ii","e","ou","yuu","oo","ui"]
    #Vowels2 =   ["you","ai","ya","yo","yu","ei","oi","aa","ae","uu"]
    Vowels =    ["u","a","i","o","ya","e","ou","yuu","yu","aa"]
    Vowels2 =   ["you","ai","yo","oi","ui","ei","oo","ii","ae","uu"]
    listvowel = ["","A","I","O","X","AI","AO","IX","OX","AIO"]
    firstvowel = [["A","YA","YOX","AIO"],["I","YIX"],["","YX","YAIO"],["AI","YAI"],["O","AO","YO","YAO"],["X"],["OX","IX"],["Y","YI"]]# a,i,u,e,o,ya,yu,yo
    secondvowel = [["YX","YA","YIX","YO","YAI"],["AO","Y","IX","YAIO"],["YOX"],["YAO"]]# i,u,e,o
    ConsonantOrder = ["","k","s","t","n","h","m","r","w","g","d","z","b","p","f","x"]

    kana = [["あ","い","う","え","お","や","ゆ","よ"],
            ["か","き","く","け","こ","きゃ","きゅ","きょ"],
            ["さ","し","す","せ","そ","しゃ","しゅ","しょ"],
            ["た","ち","つ","て","と","ちゃ","ちゅ","ちょ"],
            ["な","に","ぬ","ね","の","にゃ","にゅ","にょ"],
            ["は","ひ","ふ","へ","ほ","ひゃ","ひゅ","ひょ"],
            ["ま","み","む","め","も","みゃ","みゅ","みょ"],
            ["ら","り","る","れ","ろ","りゃ","りゅ","りょ"],
            ["わ","ゐ","う","ゑ","を","うぃ","うぇ","うぉ"],
            ["が","ぎ","ぐ","げ","ご","ぎゃ","ぎゅ","ぎょ"],
            ["だ","ぢ","で","づ","ど","てぃ","でゅ","でぃ"],
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
        for i in range(8):
            if Vowel in firstvowel[i]:
                answer = i
        return answer
    def searchVowel2(Vowel):
        answer = 99
        for i in range(4):
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
        elif かな == "dyou":
            output = "でい"
        elif かな == "dei":
            output = "でぃ"
        elif かな == "dyuu":
            output = "てぃ"
        else:
            output = kana[ConsonantOrder.index(Consonants[listconsonant.index(Conso)])][searchVowel(Ys + Vowel)]
            if searchVowel2(Ys + Vowel) != 99:
                output += kana[0][searchVowel2(Ys + Vowel) + 1]
            if output == "うぇう":
                output = ""
            elif output == "うぉう":
                output = ""
            elif output == "でゅう":
                output = ""
            elif output == "でぃう":
                output = ""

        print(output)
        return output

    resultL = Make(LeftY,LeftConsonant,LeftVowel)
    resultR = ""
    result = ""

    if resultL or RightY or RightConsonant or RightVowel:#ひだりに入力がある時だけ右の音を出す
        resultR = Make(RightY,RightConsonant,RightVowel)

    listParticle = ["","n","t","k","tk","tn","kn","tkn"]
    listSecondWord = ["","ん","つ","く","っ","ち","き","ー"]
    listLParticle = ["","}{#Space}{","}{#F6}{","}{#F7}{","}{#F8}{","}{#F9}{","}{#F10}{","}{#F10}{#F10}{"]
    listRParticle = ["","}{#Return}{",".",",","?",".}{#Return}{",",}{#Return}{","!"]

    助詞 = ["","の","で","が","を","に","は","も"]
    めいし = ["こ","た","と","き","も","は","に","ほ"]
    名詞 = ["こと","ため","ところ","とき","もの","はなし","なに","ほう"]

    どうし = ["","い","て","あ","く","す","な","み","だ","で","ゆ","げ","さ","う","か"]
    動詞 = [["","ない","た","ます","ました","って","ません","なかった"],
          ["いる","いない","いた","います","いました","いて","いません","い"],
          ["ている","ていない","ていた","ています","ていました","ていて","ていません","てい"],
          ["ある","ない","あった","あります","ありました","あって","ありません","あり"],
          ["くる","こない","きた","きます","きました","きて","きません","き"],
          ["する","しない","した","します","しました","して","しません","し"],
          ["なる","ならない","なった","なります","なりました","なって","なりません","なり"],
          ["みる","みない","みた","みます","みました","みて","みません","み"],
          ["だ","ではない","だった","です","でした","であって","ではありません","であり"],
          ["できる","できない","できた","できます","できました","できて","できません","でき"],
          ["いう","いわない","いった","いいます","いいました","いって","いいません","いい"],
          ["あげる","あげない","あげた","あげます","あげました","あげて","あげません","あげ"],
          ["させる","させない","させた","させます","させました","させて","させません","させ"],
          ["おもう","おもわない","おもった","おもいます","おもいました","おもって","おもいません","おもい"],
          ["かんがえる","かんがえない","かんがえた","かんがえます","かんがえました","かんがえて","かんがえません","かんがえ"]]
    
    if LeftAsterisk and (resultL or LeftParticle):
            if resultL in どうし:
                resultL = 動詞[どうし.index(resultL)][listParticle.index(LeftParticle)]
            elif resultL in めいし:
                resultL = 名詞[めいし.index(resultL)] + 助詞[listParticle.index(LeftParticle)]
    if RightAsterisk and (resultR or RightParticle):
            if resultR in どうし:
                resultR = 動詞[どうし.index(resultR)][listParticle.index(RightParticle)]
            elif resultR in めいし:
                resultR = 名詞[めいし.index(resultR)] + 助詞[listParticle.index(RightParticle)]
    
    #LeftParticleになにかあって左の指の入力もあるとき
    if not LeftAsterisk and LeftParticle and (resultL or resultR):
        resultL += listSecondWord[listParticle.index(LeftParticle)]
        print(resultL)
    #RightParticleになにかあって右の指の入力もあるとき
    if not RightAsterisk and RightParticle and (resultR or resultL and LeftParticle):
        resultR += listSecondWord[listParticle.index(RightParticle)]
        print(resultR)
    elif  not resultL and not resultR:#どちらの指にも入力が無いとき
        if not Numbers:
            result = listLParticle[listParticle.index(LeftParticle)] + listRParticle[listParticle.index(RightParticle)]
        else:
            result = Numbers

    if result == "":
        result = resultL + resultR

    if not resultL and resultR and not LeftParticle:
        print("右手略語")
        return ""
    else:
        print("{^" + result + "^}")
        return "{^" + result + "^}"
