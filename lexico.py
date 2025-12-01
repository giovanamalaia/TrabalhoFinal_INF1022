from sly import Lexer

class ObsActLexer(Lexer):
    tokens = {
        ID, NUM, STRING, 
        DISPOSITIVOS, FIMDISPOSITIVOS, 
        DEF, QUANDO, SENAO, EXECUTE, 
        LIGAR, DESLIGAR, ALERTA, PARA, EM, DIFUNDIR,
        AND, BOOL_VAL, OPLOGIC, SETA
    }
    
    ignore = ' \t' # espaço e tabulação ignore
    literals = { ':', ';', ',', '[', ']', '=', '(', ')' }
    SETA = r'->'
    OPLOGIC = r'(>=|<=|==|!=|>|<)'
    STRING  = r'\".*?\"'
    ID = r'[a-zA-Z][a-zA-Z0-9]*'

    ID['dispositivos'] = DISPOSITIVOS
    ID['fimdispositivos'] = FIMDISPOSITIVOS
    ID['def'] = DEF
    ID['quando'] = QUANDO
    ID['senao'] = SENAO
    ID['execute'] = EXECUTE
    ID['alerta'] = ALERTA
    ID['para'] = PARA
    ID['em'] = EM
    ID['difundir'] = DIFUNDIR
    ID['ligar'] = LIGAR
    ID['desligar'] = DESLIGAR
    ID['AND'] = AND
    
    # para aceitar tanto 'True' quanto 'TRUE'
    ID['True'] = BOOL_VAL
    ID['TRUE'] = BOOL_VAL
    ID['False'] = BOOL_VAL
    ID['FALSE'] = BOOL_VAL

    @_(r'\d+')
    def NUM(self, t):
        t.value = int(t.value)
        return t

    @_(r'\n+')
    def ignore_newline(self, t):
        self.lineno += len(t.value)

    def error(self, t):
        print(f"Caractere ilegal: {t.value[0]!r} na linha {self.lineno}")
        self.index += 1