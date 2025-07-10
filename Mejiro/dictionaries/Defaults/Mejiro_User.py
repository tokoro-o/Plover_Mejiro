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

    def process_map_output_wrapping(text):
        """
        asterisk_map からの出力が単一のアルファベット文字であれば、
        小文字に変換し、先頭に{MODE:SET_SPACE:}を付け、{#shift(F1)} で囲みます。
        （Google 日本語入力で"Shift + F1"を「半角英数切り替え」と設定しています）
        """
        if text and len(text) == 1 and text.isalpha():
            return "{MODE:SET_SPACE:}{#shift(F1)}" + text.lower() + "{#shift(F1)}"
        return text

    def add_set_space_if_alphabet(text):
        """
        テキストが単一のアルファベット文字であれば、先頭に {MODE:SET_SPACE:} を追加します。
        """
        if text and len(text) == 1 and text.isalpha():
            return "{MODE:SET_SPACE:}" + text
        return text

    if Asterisk == "*":
        asterisk_map = {
            'a': 'I', 'i': '1', 'u': 'という', 'e': 'A', 'o': 'O',
            'ka': 'かわ', 'ki': 'X', 'ku': '9', 'ke': 'K', 'ko': 'こと',
            'kya': 'から', 'kyu': 'Q', 'kyo': 'これ',
            'ga': 'がわ', 'gi': 'とき', 'gu': 'くり', 'ge': 'わけ', 'go': '5',
            'gya': 'がら', 'gyu': 'グラム', 'gyo': 'この',
            'sa': '3', 'shi': 'C', 'su': 'S', 'se': '', 'so': 'として',
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
            'wa': 'Y', 'wi': '', 'nn': '.', 'wo': ',',
            'ヲ': ',', 'ヮ': 'わり', 'ッ': 'について', 'ヴ': 'において'
        }

        resultL = Make(LeftY, LeftConsonant, LeftVowel)
        resultR = Make(RightY, RightConsonant, RightVowel)
        
        corrected_L = 修正(resultL)
        corrected_R = 修正(resultR)

        combined_key = corrected_L + corrected_R
        
        output_to_wrap = ""

        if combined_key and combined_key in asterisk_map:
            original_map_value = asterisk_map[combined_key]
            processed_from_map = process_map_output_wrapping(original_map_value)
            if len(original_map_value) == 1 and original_map_value.isalpha():
                output_to_wrap = add_set_space_if_alphabet(processed_from_map)
            else:
                output_to_wrap = processed_from_map

        #elif LeftParticle == "tkn" and RightParticle == "tkn":
        #   output_to_wrap = "EE"
        #elif LeftParticle == "tkn" or RightParticle == "tkn":
        #    output_to_wrap = add_set_space_if_alphabet("E")
        elif RightParticle == "tkn":
           output_to_wrap = "{MODE:SET_SPACE:}{#shift(F1)}e{#shift(F1)}"
        #elif LeftParticle == "tkn" or RightParticle == "tkn":
        #    output_to_wrap = add_set_space_if_alphabet("E")
        
        else:
            processed_L = ""
            if corrected_L:
                mapped_L = asterisk_map.get(corrected_L, "")
                wrapped_L = process_map_output_wrapping(mapped_L)
                if len(mapped_L) == 1 and mapped_L.isalpha():
                    processed_L = add_set_space_if_alphabet(wrapped_L)
                else:
                    processed_L = wrapped_L
            
            processed_R = ""
            if corrected_R:
                mapped_R = asterisk_map.get(corrected_R, "")
                wrapped_R = process_map_output_wrapping(mapped_R)
                if len(mapped_R) == 1 and mapped_R.isalpha():
                    processed_R = add_set_space_if_alphabet(wrapped_R)
                else:
                    processed_R = wrapped_R
            
            output_to_wrap = processed_L + processed_R

        if output_to_wrap:
            if "{MODE:SET_SPACE:}" in output_to_wrap:
                return output_to_wrap
            else:
                return "{^" + output_to_wrap + "^}"
        else:
            raise KeyError

    