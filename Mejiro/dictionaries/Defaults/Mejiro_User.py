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
                output += Vowels2[listvowel.index(Vowel)]
            else:
                output += Vowels[listvowel.index(Vowel)]
            if output in excepts_in:
                output = excepts_out[excepts_in.index(output)]
        print(output)
        return output

    if Asterisk == "*":
        asterisk_map = {
            'a': 'I', 'i': '1', 'u': 'という', 'e': 'A', 'o': 'O',
            'ka': 'かわ', 'ki': 'X', 'ku': '9', 'ke': 'K', 'ko': 'こと',
            'kya': 'から', 'kyu': 'Q', 'kyo': 'これ',
            'ga': 'がわ', 'gi': 'とき', 'gu': 'くり', 'ge': 'わけ', 'go': '5',
            'gya': 'がら', 'gyu': 'グラム', 'gyo': 'この',
            'sa': '3', 'shi': 'C', 'su': 'S', 'se': 'ソ', 'so': 'として',
            'sha': 'さま', 'shu': 'する', 'sho': 'それ',
            'za': 'とし', 'ji': 'G', 'zu': 'Z', 'ze': 'J', 'zo': 'そこ',
            'ja': 'した', 'ju': 'して', 'jo': 'その',
            'ta': 'あと', 'chi': 'H', 'tsu': '日', 'te': 'T', 'to': 'とり',
            'cha': 'だけ', 'chu': 'づくり', 'cho': 'とか',
            'da': 'W', 'di': 'ません', 'du': '・', 'de': 'D', 'do': 'など',
            'dya': 'では', 'dyu': 'すい', 'dyo': 'とも',
            'na': '7', 'ni': '2', 'nu': 'N', 'ne': '年度', 'no': 'ので',
            'nya': 'なら', 'nyu': 'には', 'nyo': 'にも',
            'ha': '8', 'hi': 'ひと', 'fu': 'F', 'he': '平成', 'ho': 'ほど',
            'hya': 'ドル', 'hyu': 'ふうに', 'hyo': 'ように',
            'ba': 'れば', 'bi': 'B', 'bu': 'V', 'be': 'ボ', 'bo': 'かた',
            'bya': 'ビュ', 'byu': 'ふうな', 'byo': 'ような',
            'pa': '%', 'pi': 'P', 'pu': 'プロ', 'pe': 'ページ', 'po': 'ほか',
            'pya': '00', 'pyu': '000', 'pyo': 'ようで',
            'ma': 'まで', 'mi': 'メートル', 'mu': 'M', 'me': 'ため', 'mo': 'もの',
            'mya': 'まえ', 'myu': 'いま', 'myo': 'もと',
            'ya': 'やま', 'yu': 'U', 'yo': '4',
            'ra': 'R', 'ri': 'より', 'ru': 'L', 're': '0', 'ro': '6',
            'rya': 'られ', 'ryu': 'れる', 'ryo': 'ところ',
            'wa': 'Y', 'wi': 'イン', 'we': '.', 'wo': 'ー',
            'ヲ': ',', 'ヮ': 'わり', 'ッ': 'について', 'ヴ': 'において'
        }

        resultL = Make(LeftY, LeftConsonant, LeftVowel)
        resultR = Make(RightY, RightConsonant, RightVowel)
        
        # `si`を`shi`に変換するなどの処理を適用
        corrected_L = 修正(resultL)
        corrected_R = 修正(resultR)

        combined_key = corrected_L + corrected_R
        
        final_output = ""
        # まず結合したキー（例: "ki"）で辞書を検索
        if combined_key and combined_key in asterisk_map:
            final_output = asterisk_map[combined_key]
        # 結合したキーに一致するものがない場合、左右個別のキーで検索
        else:
            outputL = asterisk_map.get(corrected_L, "") if corrected_L else ""
            outputR = asterisk_map.get(corrected_R, "") if corrected_R else ""
            final_output = outputL + outputR

        if final_output:
            return "{^" + final_output + "^}"
        else:
            # どのキーにも一致しなかった場合はエラー
            raise KeyError

    # --- 以下、アスタリスクが押されていない場合の通常の処理 ---
    
    resultL = Make(LeftY,LeftConsonant,LeftVowel)
    resultR = ""
    result = ""

    if resultL or RightY or RightConsonant or RightVowel:
        resultR = Make(RightY,RightConsonant,RightVowel)

    listParticle = ["","n","t","k","tk","tn","kn","tkn"]
    listSecondWord = ["","nn","tsu","ku","ltsu","chi","ki","-"]
    listLParticle = ["",",","ni","no","de","to","wo","ka"]
    listRParticle = ["",",","ha","ga","mo","ha,","ga,","mo,"]

    助詞in = ["ha,","ga,","mo,","ha","ga","mo","ha,","ga,","mo,","niga","niga,","dega","dega,","kaga","kaga,","woga","woga,"]
    助詞out = [".",",","-","ha,","ga,","mo,","!","?","nn","noni","noni,","node","node,","noka","noka,","nowo","nowo,"]
    
    if not Asterisk and LeftParticle and (resultL or resultR):
        print("zyoshi")
        resultL += listSecondWord[listParticle.index(LeftParticle)]
        print(resultL)

    if not Asterisk and RightParticle and (resultR or resultL and LeftParticle):
        resultR += listSecondWord[listParticle.index(RightParticle)]
        print(resultR)

    if (resultL or resultR) and not LeftParticle and RightParticle == "n" and not Hyphen and not Asterisk:
        print("suuji")
        result = ""
        if LeftY: result += "1"
        if "K" in LeftConsonant: result += "2"
        if "S" in LeftConsonant: result += "3"
        if "I" in LeftVowel: result += "4"
        if "U" in LeftVowel: result += "5"
        if "U" in RightVowel: result += "6"
        if "I" in RightVowel: result += "7"
        if "S" in RightConsonant: result += "8"
        if "K" in RightConsonant: result += "9"
        if RightY: result += "0"

    if not resultL and not resultR:
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