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
    listconsonant = ["","T","K","S","N","TS","KN","TK","NS","KNS","TKNS","KS","TKS","TKN","TNS","TN"]

    Vowels =    ["u","o","i","ou","e","a","ei","oi","ii","ui"]
    Vowels2 =   ["you","ya","yuu","yo","yu","ai","ae","oo","aa","uu"]
    listvowel = ["","O","I","E","e","OI","Ie","OE","Ee","OIE"]

    kana = [[ "" ,"お","い","おう","え","あ","えい","おい","いい","うい"],
            ["つ","と","ち","とう","て","た","てい","とい","ちい","つい"],
            ["く","こ","き","こう","け","か","けい","こい","きい","くい"],
            ["す","そ","し","そう","せ","さ","せい","そい","しい","すい"],
            ["ぬ","の","に","のう","ね","な","ねい","のい","にい","ぬい"],
            ["る","ろ","り","ろう","れ","ら","れい","ろい","りい","るい"],
            ["む","も","み","もう","め","ま","めい","もい","みい","むい"],
            ["ふ","ほ","ひ","ほう","へ","は","へい","ほい","ひい","ふい"],
            ["づ","ど","ぢ","どう","で","だ","でい","どい","ぢい","づい"],
            ["ぐ","ご","ぎ","ごう","げ","が","げい","ごい","ぎい","ぐい"],
            ["う","を","ゐ","うぉう","ゑ","わ","うぇい","をい","うぇい","うい"],
            ["ず","ぞ","じ","ぞう","ぜ","ざ","ぜい","ぞい","じい","ずい"],
            ["ぶ","ぼ","び","ぼう","べ","ば","べい","ぼい","びい","ぶい"],
            ["ぷ","ぽ","ぴ","ぽう","ぺ","ぱ","ぺい","ぽい","ぴい","ぷい"],
            ["ヴ","ヴぉ","ヴぃ","ヴぉう","ヴぇ","ヴぁ","ヴぇい","ヴぉい","ヴぃい","ヴい"],
            ["ぅ","ぉ","ぃ","ぉう","ぇ","ぁ","ぇい","ぉい","ぃい","ぅい"],]
    
    kana2 = [["よう","や","ゆう","よ","ゆ","あい","あえ","おお","ああ","うう"],
            ["ちょう","ちゃ","ちゅう","ちょ","ちゅ","たい","たえ","とお","たあ","つう"],
            ["きょう","きゃ","きゅう","きょ","きゅ","かい","かえ","こお","かあ","くう"],
            ["しょう","しゃ","しゅう","しょ","しゅ","さい","さえ","そお","さあ","すう"],
            ["にょう","にゃ","にゅう","にょ","にゅ","ない","なえ","のお","なあ","ぬう"],
            ["りょう","りゃ","りゅう","りょ","りゅ","らい","らえ","ろお","らあ","るう"],
            ["みょう","みゃ","みゅう","みょ","みゅ","まい","まえ","もお","まあ","むう"],
            ["ひょう","ひゃ","ひゅう","ひょ","ひゅ","はい","はえ","ほお","はあ","ふう"],
            ["ぢょう","ぢゃ","ぢゅう","ぢょ","ぢゅ","だい","だえ","どお","だあ","づう"],
            ["ぎょう","ぎゃ","ぎゅう","ぎょ","ぎゅ","がい","がえ","ごお","があ","ぐう"],
            ["うぉう","うぁ","うぃう","うぉ","うぇ","わい","わえ","をお","わあ","うぅう"],
            ["じょう","じゃ","じゅう","じょ","じゅ","ざい","ざえ","ぞお","ざあ","ずう"],
            ["びょう","びゃ","びゅう","びょ","びゅ","ばい","ばえ","ぼお","ばあ","ぶう"],
            ["ぴょう","ぴゃ","ぴゅう","ぴょ","ぴゅ","ぱい","ぱえ","ぽお","ぱあ","ぷう"],
            ["ヴゃ","ヴゃ","ヴゅう","ヴょ","ヴゅ","ヴぁい","ヴぁえ","ヴぉお","ヴぁあ","ヴう"],
            ["ょう","ゃ","ゅう","ょ","ゅ","ぁい","ぁえ","ぉお","ぁあ","ぅう"],]

    if LeftVowel not in listvowel:
         LeftVowel = listvowel[9]
    if RightVowel not in listvowel:
         RightVowel = listvowel[9]

    def Make(Conso,Ys,Vowel):

        output = ""
        
        if not Conso and not Ys and not Vowel:
             output = ""
        else:
            if Ys:
                #Yが入力されていたら
                output = kana2[listconsonant.index(Conso)][listvowel.index(Vowel)]
            else:
                #そうでないとき
                output = kana[listconsonant.index(Conso)][listvowel.index(Vowel)]
        print(output)
        return output

    resultL = Make(LeftConsonant,LeftY,LeftVowel)
    resultR = ""
    result = ""

    if resultL:#ひだりに入力がある時だけ右の音を出すよ
           resultR = Make(RightConsonant,RightY,RightVowel)

    #こっからは親指のはなしです
    listParticle = ["n","t","k","tk","tn","kn","tkn",""]
    listSW = ["ん","つ","く","っ","ち","き","ー",""]#SWはセカンドワードつまり二音目
    listLParticle = ["の","て","か","で","な","に","も",""]
    listOnlyLParticle = ["ない","て","が","と","な","を","や",""]
    listRParticle = ["の","で","か","って","は","に","も",""]
    #LeftParticleになにかあって左の指の入力もあるとき
    if LeftParticle and resultL:
        resultL += listSW[listParticle.index(LeftParticle)]
    #RightParticleになにかあって右の指の入力もあるとき
    if RightParticle and resultR:
        resultR += listSW[listParticle.index(RightParticle)]

    if not resultL and not resultR:#どちらの指にも入力が無いとき
        if LeftParticle and not RightParticle:
            #左親指だけの時
            result = listOnlyLParticle[listParticle.index(LeftParticle)]
        else:
            if listParticle.index(LeftParticle) == 0 and listParticle.index(RightParticle) == 0:
                result = "ある"
            elif listParticle.index(LeftParticle) == 2 and listParticle.index(RightParticle) == 2:
                result = "かな"
            elif listParticle.index(LeftParticle) == 3 and listParticle.index(RightParticle) == 1:
                result = "こと"
            elif listParticle.index(LeftParticle) == 4 and listParticle.index(RightParticle) == 1:
                result = "なにで"
            elif listParticle.index(LeftParticle) == 4 and listParticle.index(RightParticle) == 2:
                result = "なにか"
            elif listParticle.index(LeftParticle) == 4 and listParticle.index(RightParticle) == 4:
                result = "なにが"
            elif listParticle.index(LeftParticle) == 4 and listParticle.index(RightParticle) == 6:
                result = "なにも"
            elif listParticle.index(LeftParticle) == 5 and listParticle.index(RightParticle) == 5:
                result = "のを"
            elif listParticle.index(LeftParticle) == 6 and listParticle.index(RightParticle) == 6:
                result = "もの"
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
    #↓、デバッグ用のコンソールに表示されるよ
    print(result)
    #↓、「{^^}」でスペースをなくす出力をしてるよ
    return "{^" + result + "^}"
