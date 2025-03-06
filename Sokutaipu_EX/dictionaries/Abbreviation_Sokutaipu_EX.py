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

    listvowel = ["","A","I","O","U","AI","AO","IU","OU","AIO"]
    result = ""
    if LeftVowel not in listvowel:
         LeftVowel = listvowel[9]
    if RightVowel not in listvowel:
         RightVowel = listvowel[9]

    LeftStroke = LeftY + LeftConsonant + LeftVowel + LeftParticle
    RightStroke = RightY + RightConsonant + RightVowel + RightParticle

    print("LeftAsterisk\tLeftConsonant\tLeftVowel\tLeftParticle")
    print(LeftAsterisk + "\t\t" + LeftStroke)

    print("RightAsterisk\tRightConsonant\tRightVowel\tRightParticle")
    print(RightAsterisk + "\t\t" + RightStroke)

    print(stroke)

    def 検索(stroke,list):
        flag = 0
        for i in range(len(list)):
            if list[i][0] == stroke:
                flag = i
        return flag
    
    kana = [["わ","い","う","え","お","っ"],#0
            ["か","き","く","け","こ","い"],#1
            ["が","ぎ","ぐ","げ","ご","い"],#2
            ["さ","し","す","せ","そ","し"],#3
            ["ざ","じ","ず","ぜ","ぞ","じ"],#4
            ["た","ち","つ","て","と","っ"],#5
            ["だ","ぢ","づ","で","ど","  "],#6
            ["な","に","ぬ","ね","の","ん"],#7
            ["は","ひ","ふ","へ","ほ","  "],#8
            ["ば","び","ぶ","べ","ぼ","ん"],#9
            ["ま","み","む","め","も","ん"],#10
            ["ら","り","る","れ","ろ","っ"],#11
            ["ら","い","る","れ","ろ","っ"]]#12


    五段 =   [0,1,2,2,3,3,4,5]
    上一段 = [1,1,1,1,1,1,1,1]
    下一段 = [3,3,3,3,3,3,3,3]
    カ変 =   [4,1,2,2,2,4,4,1]
    サ変 =   [1,1,2,2,2,3,1,1]#ない、用、止、体、仮、ろ、よう、て・た
                #ストローク，語幹，段, 活用
    動詞リスト = [
                ["","",3,サ変],#する
                ["KSIU","よろしくおねがい",3,サ変],#よろしくおねがいする
                ["k","",1,カ変],#くる
                ["I","",0,上一段],#いる
                ["kn","",1,上一段],#きる
                ["Otn","お",5,上一段],#おちる
                ["N","",7,上一段],#にる
                ["TKSI","の",9,上一段],#のびる
                ["KNkn","で",1,上一段],#できる
                ["TN","",10,上一段],#みる
                ["KSI","か",11,上一段],#かりる
                ["AI","",0,下一段],#える
                ["IU","ゆ",11,下一段],#ゆれる
                ["SAk","さ",1,下一段],#さける
                ["Y","いた",3,五段],#いたす
                ["YKSIU","よろしくおねがいいた",3,五段],#よろしくおねがいいたす
                ["A","あ",11,五段],#ある
                ["OU","い",0,五段],#いう
                ["NI","し",7,五段],#しぬ
                ["TNAI","ため",3,五段],#ためす
                ["NSO","ござ",12,五段],#ござる
                ["AIO","ありがとうござ",12,五段],#ありがとうござる
                ["YAIO","もうしわけござ",12,五段]]#もうしわけござる
                #ストローク，語幹，活用形
    語尾リスト = [
                ["","",2],
                ["k",",",1],
                ["kn","",1],
                ["t",".",2],
                ["n","ん",2],
                ["KO","こと",2],
                ["NO","の",2],
                ["TO","と",2],
                ["SO","そう",2],
                ["TNAI","ため",2],
                ["KA","から",2],
                ["OU","という",2],
                ["OUt","といった",2],
                ["OUtn","といって",2],
                ["OUk","といいます",2],
                ["OUkn","といいまして",2],
                ["NA","ない",0],
                ["NAn","なくて",0],
                ["NAt","なかった",0],
                ["TNAt","ました",1],
                ["TNAk","まして",1],
                ["TNAn","ません",1],
                ["TNAtn","ませんでした",1],
                ["TNA","ます",1],
                ["TA","た",7],
                ["TAt","たって",7],
                ["TAn","なかった",0],
                ["TAI","て",7],
                ["TAIk","まして",1],
                ["TAIn","なくて",0],
                ["TAIt","てた",7],
                ["I","ている",7],
                ["In","てない",7],
                ["It","ていた",7],
                ["Itn","てなかった",7],
                ["Itkn","ていませんでした",7],
                ["Itn","ていません",7],
                ["Itk","ていました",7],
                ["Ik","ています",7],
                ["Y","う",6],
                ["TS","ず",0],
                ["TKSA","ば",4],
                ["YI","よ",5],
                ["KSO","",5]]

    い動詞 = [1,2]
    ん動詞 = [7,9,10]
    っ動詞 = [0,5,11]
    
    動詞index = 検索(LeftStroke,動詞リスト)
    語尾index = 検索(RightStroke,語尾リスト)
    動詞 = 動詞リスト[動詞index]
    語尾 = 語尾リスト[語尾index]

    result = 動詞[1] + kana[動詞[2]][動詞[3][語尾[2]]]
    if 語尾[2] == 2 and 動詞[3] != 五段:
        result += "る"
    elif 語尾[0] == "Y" and 動詞[3] == 五段:
        result += "よ"
    elif 語尾[0] == "Y" and 動詞[3] != 五段:
        result += "よ"
    elif 語尾[0] == "TKSA" and 動詞[3] != 五段:
        result += "れ"
    elif 語尾[0] == "KSO" and 動詞[3] != 五段 and 動詞[3] != カ変:
        result += "ろ"

    result += 語尾[1]
    result = result.replace('んて', 'んで').replace('んた', 'んだ').replace('あらな', 'な').replace('すろ', 'しろ').replace('しず', 'せず')

    if LeftAsterisk:
        print("{^" + result + "^}")
        return "{^" + result + "^}"
    else:
        print("key error*")
        raise KeyError