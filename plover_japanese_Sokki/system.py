KEYS = (
'*-', 'N-', 'T-', 'S-', 'K-', 'Y-', 'A-', 'I-', 'O-', 'o-', 't-', 'k-', 'n-',
'#',
'-*', '-N', '-T', '-S', '-K', '-Y', '-A', '-I', '-O', '-o', '-t', '-k', '-n',
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
        'N-' : 'w',
        'T-' : 's',
        'S-' : 'e',
        'K-' : 'd',
        'Y-' : 'a',
        'A-' : 'f',
        'I-' : 'r',
        'O-' : 'g',
        'o-' : 't',
        't-' : 'x',
        'k-' : 'v',
        'n-' : 'c',
        '#'  : ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '='),
        '-*' : 'p',
        '-N' : 'o',
        '-T' : 'l',
        '-S' : 'i',
        '-K' : 'k',
        '-Y' : ';',
        '-A' : 'j',
        '-I' : 'u',
        '-O' : 'h',
        '-o' : 'y',
        '-t' : 'm',
        '-k' : 'b',
        '-n' : 'n',
        'arpeggiate': 'space',
        }
}


DICTIONARIES_ROOT = 'asset:plover_japanese_Sokki:dictionaries'
DEFAULT_DICTIONARIES = ('Plover_Japanese_Sokki.py','abbreviation_for_Sokki.json','commands_for_Sokki.json')
