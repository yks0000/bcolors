"""

Library to help color Foreground color of text using print function.
Ref: blender build scripts
"""

OK = '\033[92m'
WARN = '\033[93m'
ERR = '\033[31m'
UNDERLINE = '\033[4m'
ITALIC = '\x1B[3m'
BOLD = '\033[1m'
BLUE = '\033[94m'
ENDC = '\033[0m'

HEADER = '\033[95m' + BOLD
PASS = OK + BOLD
FAIL = ERR + BOLD

OKMSG = BOLD + OK + u'\u2705' + "  "
ERRMSG = BOLD + FAIL + u"\u274C" + "  "
WAITMSG = BOLD + WARN + u'\u231b' + "  "

HELP = WARN
BITALIC = BOLD + ITALIC
BLUEIC = BITALIC + OK
END = ENDC
