KEYS = (
'*-', 'Y-', 'T-', 'H-', 'K-', 'S-', 'A-', 'I-', 'O-', 'X-', 't-', 'k-', 'n-',
'#',
'-*', '-Y', '-T', '-H', '-K', '-S', '-A', '-I', '-O', '-X', '-t', '-k', '-n',
'-1','-2','-3','-4','-5',
'-6','-7','-8','-9','-0',
)

IMPLICIT_HYPHEN_KEYS = ('#')

SUFFIX_KEYS = ()

NUMBER_KEY = None

NUMBERS = {}

UNDO_STROKE_STENO = ('*-')

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
        'Keyboard': {
        '*-' : 'q',
        'Y-' : 'a',
        'T-' : 's',
        'H-' : 'w',
        'K-' : 'd',
        'S-' : 'e',
        'A-' : 'f',
        'I-' : 'r',
        'O-' : 'g',
        'X-' : 't',
        't-' : 'v',
        'k-' : 'b',
        'n-' : 'space',
        '#'  : 'c',
        '-*' : ('p','[',']'),
        '-Y' : ';',
        '-T' : 'l',
        '-H' : 'o',
        '-K' : 'k',
        '-S' : 'i',
        '-A' : 'j',
        '-I' : 'u',
        '-O' : 'h',
        '-X' : 'y',
        '-t' : 'm',
        '-k' : 'n',
        '-n' : 'return',
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
        'arpeggiate' : (',','.'),
        'no-op' : '\''
        }
}


DICTIONARIES_ROOT = 'asset:plover_Sokutaipu_EX:dictionaries'
DEFAULT_DICTIONARIES = ('Plover_Sokutaipu_EX_kana.py','abbreviation_for_Sokutaipu_EX.json','commands_for_Sokutaipu_EX.json')
