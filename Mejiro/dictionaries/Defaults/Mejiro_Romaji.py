#*YTKNSAIOUtkn#*YTKNSAIOUtkn
import re

LONGEST_KEY = 1

def lookup(key):
    assert len(key) <= LONGEST_KEY
    stroke = key[0]

    if stroke == "#":
        print("key error*")
        raise KeyError

    regex = re.compile(r"(Y?)(T?K?N?S?)(A?I?O?U?)(t?k?n?)(\-?#?)(\*?)(Y?)(T?K?N?S?)(A?I?O?U?)(t?k?n?)")
    regex_groups = re.search(regex, stroke)

    LeftY = regex_groups.group(1)
    LeftConsonant = regex_groups.group(2)
    LeftVowel = regex_groups.group(3)
    LeftParticle = regex_groups.group(4)
    Hyphen = regex_groups.group(5)
    Asterisk = regex_groups.group(6)
    RightY = regex_groups.group(7)
    RightConsonant = regex_groups.group(8)
    RightVowel = regex_groups.group(9)
    RightParticle = regex_groups.group(10)

    print("stroke:" + stroke)

    #頻出順→『n,t,k,s,r,m,h,d,g,w,z,b,j,p』

    Consonants =    ["","t","k","n","s","h","m","z","g","r","d","w","p","l","b","f"]
    listconsonant = ["","T","K","N","S","TK","TN","TS","NS","KS","KN","TKN","TNS","TKNS","TKS","KNS"]

    Vowels =    ["u","a","i","o","ya","e","ou","yuu","yu","au"]
    Vowels2 =   ["you","ai","yo","oi","ui","ei","oo","ii","ae","uu"]
    listvowel = ["","A","I","O","U","AI","AO","IU","OU","AIO"]
    
    excepts_in = [
                  "ni","nu","nyuu","nyou",
                  "mi","mu",
                  "wya","wyu","wyo","wyuu","wyou","wii","wui","wuu","wei",
                  "di","du","de","dya","dyo","dyuu","dyou","dii","dei",
                  "fu","fyuu","fyou"]
    excepts_out = [
                   "nu","ni","nyou","nyuu",
                   "mu","mi",
                   "yaa","iu","yone","ee","ue","wi","ao","ulu","we",
                   "thi","de","du","tye","sye","dhi","dei","zye","di",
                   "vu","qa","qo"]

    if LeftVowel not in listvowel:
         LeftVowel = listvowel[9]
    if RightVowel not in listvowel:
         RightVowel = listvowel[9]

    def 修正(result):
        return result.replace('hu', 'fu').replace('si', 'shi').replace('sy', 'sh').replace('zi', 'ji').replace('zy', 'j').replace('ti', 'chi').replace('ty', 'ch').replace('tu', 'tsu').replace('wu', 'u').replace('ltsuk', 'kk').replace('ltsus', 'ss').replace('ltsut', 'tt').replace('ltsuc', 'cc').replace('ltsuh', 'hh').replace('ltsum', 'mm').replace('ltsur', 'rr').replace('ltsuw', 'ww').replace('ltsug', 'gg').replace('ltsuz', 'zz').replace('ltsuj', 'jj').replace('ltsud', 'dd').replace('ltsup', 'pp').replace('ltsub', 'bb').replace('nnk', 'nk').replace('nns', 'ns').replace('nnt', 'nt').replace('nnc', 'nc').replace('nnh', 'nh').replace('nnm', 'nm').replace('nnr', 'nr').replace('nnw', 'nw').replace('nng', 'ng').replace('nnz', 'nz').replace('nnj', 'nj').replace('nnd', 'nd').replace('nnp', 'np').replace('nnb', 'nb')
    
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

            if output in excepts_in:
                output = excepts_out[excepts_in.index(output)]

        print(output)
        return output

    resultL = Make(LeftY,LeftConsonant,LeftVowel)
    resultR = ""
    result = ""

    if resultL or RightY or RightConsonant or RightVowel:#ひだりに入力がある時だけ右の音を出す
        resultR = Make(RightY,RightConsonant,RightVowel)

    listParticle = ["","n","t","k","tk","tn","kn","tkn"]
    listSecondWord = ["","nn","tsu","ku","ltsu","chi","ki","-"]
    listLParticle = ["",",","ni","no","de","to","wo","ka"]
    listRParticle = ["",",","ha","ga","mo","ha,","ga,","mo,"]

    助詞in = ["ha,","ga,","mo,",",ha",",ga",",mo",",ha,",",ga,",",mo,","niga","niga,","dega","dega,","kaga","kaga,","woga","woga,"]
    助詞out = [".",",","-","ha,","ga,","mo,","!","?","nn","noni","noni,","node","node,","noka","noka,","nowo","nowo,"]
    
    #LeftParticleになにかあって左の指の入力もあるとき
    if not Asterisk and LeftParticle and (resultL or resultR):
        print("zyoshi")
        resultL += listSecondWord[listParticle.index(LeftParticle)]
        print(resultL)
    #RightParticleになにかあって右の指の入力もあるとき
    if not Asterisk and RightParticle and (resultR or resultL and LeftParticle):
        resultR += listSecondWord[listParticle.index(RightParticle)]
        print(resultR)
    if  (resultL or resultR) and not LeftParticle and RightParticle == "n" and not Hyphen and not Asterisk:#どちらの指にも入力が無いとき
        print("suuji")
        result = ""
        if LeftY:
            result += "1"
        if "K" in LeftConsonant:
            result += "2"
        if "S" in LeftConsonant:
            result += "3"
        if "I" in LeftVowel:
            result += "4"
        if "U" in LeftVowel:
            result += "5"
        if "U" in RightVowel:
            result += "6"
        if "I" in RightVowel:
            result += "7"
        if "S" in RightConsonant:
            result += "8"
        if "K" in RightConsonant:
            result += "9"
        if RightY:
            result += "0"

    if  not resultL and not resultR:#どちらの指にも入力が無いとき
        result = listLParticle[listParticle.index(LeftParticle)] + listRParticle[listParticle.index(RightParticle)]
        if result in 助詞in:
            result = 助詞out[助詞in.index(result)]
            
    if result == "":
        result = resultL + resultR

    result = 修正(result)

    if (resultL or resultR) and "#" in Hyphen:
        print("{^" + result * 2 + "^}")
        return "{^" + result * 2 + "^}"
    else:
        print("{^" + result + "^}")
        return "{^" + result + "^}"