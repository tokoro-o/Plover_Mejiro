KEYS = (
'*-', 'Y-', 'T-', 'K-', 'N-', 'S-', 'A-', 'I-', 'O-', 'U-', 't-', 'k-', 'n-',
'#',
'-*', '-Y', '-T', '-K', '-N', '-S', '-A', '-I', '-O', '-U', '-t', '-k', '-n',
'-1','-2','-3','-4','-5',
'-6','-7','-8','-9','-0',
)

IMPLICIT_HYPHEN_KEYS = ('#')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = ('-O')

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
        'Keyboard': {
        '*-' : 'q',
        'Y-' : 'a',
        'T-' : 's',
        'K-' : 'w',
        'N-' : 'd',
        'S-' : 'e',
        'A-' : 'f',
        'I-' : 'r',
        'O-' : 'g',
        'U-' : 't',
        't-' : 'c',
        'k-' : 'v',
        'n-' : 'space',
        '#'  : 'b',
        '-*' : ('p','[',']'),
        '-Y' : ';',
        '-T' : 'l',
        '-K' : 'o',
        '-N' : 'k',
        '-S' : 'i',
        '-A' : 'j',
        '-I' : 'u',
        '-O' : 'h',
        '-U' : 'y',
        '-t' : 'm',
        '-k' : 'n',
        '-n' : 'Return',
        '-1' : '1',
        '-2' : '2',
        '-3' : '3',
        '-4' : '4',
        '-5' : '5',
        '-6' : '6',
        '-7' : '7',
        '-8' : '8',
        '-9' : '9',
        '-0' : '0',
        'arpeggiate' : (',','.','z','x'),
        'no-op' : '\''
        }
}


DICTIONARIES_ROOT = 'asset:Sokutaipu_EX:dictionaries'
DEFAULT_DICTIONARIES = ('Sokutaipu_EX_Commands.json','Sokutaipu_EX_Verbs.json','Sokutaipu_EX_Kana.py')
