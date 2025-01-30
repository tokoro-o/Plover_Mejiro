KEYS = (
'*-', 'Y-', 'T-', 'H-', 'K-', 'S-', 'A-', 'I-', 'O-', 'X-', 't-', 'k-', 'n-',
'#',
'-*', '-Y', '-T', '-H', '-K', '-S', '-A', '-I', '-O', '-X', '-t', '-k', '-n',
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
        '*-' : ('b','q'),
        'Y-' : 'a',
        'T-' : 's',
        'H-' : 'w',
        'K-' : 'd',
        'S-' : 'e',
        'A-' : 'f',
        'I-' : 'r',
        'O-' : 'g',
        'X-' : 't',
        't-' : 'x',
        'k-' : 'v',
        'n-' : 'c',
        '#'  : '\'',
        '-*' : 'p',
        '-Y' : ';',
        '-T' : 'l',
        '-H' : 'o',
        '-K' : 'k',
        '-S' : 'i',
        '-A' : 'j',
        '-I' : 'u',
        '-O' : 'h',
        '-X' : 'y',
        '-t' : ',',
        '-k' : 'n',
        '-n' : 'm',
        'arpeggiate' : 'space'
        }
}


DICTIONARIES_ROOT = 'asset:plover_Sokutaipu_EX:dictionaries'
DEFAULT_DICTIONARIES = ('Plover_Sokutaipu_EX_.py','abbreviation_for_Sokutaipu_EX.json','commands_for_Sokutaipu_EX.json')
