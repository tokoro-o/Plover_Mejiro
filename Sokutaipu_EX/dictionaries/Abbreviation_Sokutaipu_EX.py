#*YTKNSAIOUtkn#*YTKNSAIOUtkn
import re

LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    stroke = key[0]

    if stroke == "#":
        print("key error*")
        raise KeyError
    
    regex = re.compile(r"(\*?)(Y?T?K?N?S?A?I?O?U?t?k?n?)(\-?#?)(\*?)(Y?T?K?N?S?A?I?O?U?t?k?n?)(1?2?3?4?5?6?7?8?9?0?)")
    regex_groups = re.search(regex, stroke)

    LeftAsterisk = regex_groups.group(1)
    LeftStroke = regex_groups.group(2)
    MiddleHyphen = regex_groups.group(3)
    RightAsterisk = regex_groups.group(4)
    RightStroke = regex_groups.group(5)
    Numbers = regex_groups.group(6)

    print("LeftAsterisk\tLeftConsonant\tLeftVowel\tLeftParticle")
    print(LeftAsterisk + "\t\t" + LeftStroke)

    print("RightAsterisk\tRightConsonant\tRightVowel\tRightParticle")
    print(RightAsterisk + "\t\t" + RightStroke)

    print(stroke)

    def 検索(stroke,list):
        flag = -1
        for i in range(len(list)):
            if list[i][0] == stroke:
                flag = i
        return flag
    
    kana = [["わ","い","う","え","お"],#0
            ["か","き","く","け","こ"],#1
            ["が","ぎ","ぐ","げ","ご"],#2
            ["さ","し","す","せ","そ"],#3
            ["ざ","じ","ず","ぜ","ぞ"],#4
            ["た","ち","つ","て","と"],#5
            ["だ","ぢ","づ","で","ど"],#6
            ["な","に","ぬ","ね","の"],#7
            ["は","ひ","ふ","へ","ほ"],#8
            ["ば","び","ぶ","べ","ぼ"],#9
            ["ま","み","む","め","も"],#10
            ["ら","り","る","れ","ろ"]]#11

    listvowel = ["","A","I","O","U","AI","AO","IU","OU","AIO"]
    result = ""
    if LeftVowel not in listvowel:
         LeftVowel = listvowel[9]
    if RightVowel not in listvowel:
         RightVowel = listvowel[9]

    #ストローク，語幹，段，活用
    #活用は1,2,3,4がそれぞれ五段,上一段,下一段,サ変,カ変
    五段 =   [0,1,2,2,3,3,4]
    上一段 = 1
    下一段 = 3
    サ変 =   [1,1,2,2,2,1,1,3,0]#ない、用、止、体、仮、ろ、よう、ず、れる
    カ変 =   [4,1,2,2,2,4,4]

    動詞 = [["","",3,サ変],
            ["K","",1,カ変],
            ["I","",0,上一段],
            ["TN","み",0,下一段]
            ["A","あ",11,五段]]
    
    語尾 = [["","る",2],
            ["TA","た",1],
            ["TAI","て",1],
            ["YTAI","ている",1]]
     
    def make(strokeL,strokeR):
        動詞index = 検索(strokeL)
        語尾index = 検索(strokeR)
        活用形 = 動詞[動詞index][3]
        活用 = 語尾[語尾index][2]
        output = 動詞[動詞index][1]
        if 活用形 is サ変:
            output += kana[3][サ変[活用]]
    print("{^" + result + "^}")
    return "{^" + result + "^}"