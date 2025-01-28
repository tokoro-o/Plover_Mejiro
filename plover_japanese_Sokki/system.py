KEYS = (
'*-', 'T-', 'K-', 'N-', 'S-', 'Y-', 'O-', 'I-', 'E-', 'e-', 't-', 'k-', 'n-',
'#',
'-*', '-T', '-K', '-N', '-S', '-Y', '-O', '-I', '-E', '-e', '-t', '-k', '-n',
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
        'T-' : 'w',
        'K-' : 's',
        'N-' : 'd',
        'S-' : 'e',
        'Y-' : 'a',
        'O-' : 'f',
        'I-' : 'r',
        'E-' : 'g',
        'e-' : 't',
        't-' : 'x',
        'k-' : 'v',
        'n-' : 'c',
        '#'  : '\'',
        '-*' : 'p',
        '-T' : 'o',
        '-K' : 'l',
        '-N' : 'k',
        '-S' : 'i',
        '-Y' : ';',
        '-O' : 'j',
        '-I' : 'u',
        '-E' : 'h',
        '-e' : 'y',
        '-t' : ',',
        '-k' : 'n',
        '-n' : 'm',
        'arpeggiate' : 'space'
        }
}


DICTIONARIES_ROOT = 'asset:plover_japanese_Sokki:dictionaries'
DEFAULT_DICTIONARIES = ('Plover_Japanese_Sokki.py','abbreviation_for_Sokki.json','commands_for_Sokki.json')
