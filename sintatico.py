from sly import Parser
from lexico import ObsActLexer

class ObsActParser(Parser):
    tokens = ObsActLexer.tokens

    def __init__(self):
        self.code = []
        # conjunto para memorizar os sensores encontrados
        self.sensores_encontrados = set()

    @_('dev_section cmd_section')
    def program(self, p):
        header = "from funcoes import *\n\n"
        
        # para cada sensor encontrado, é inicializado com 0
        inicializacao = ""
        for sensor in self.sensores_encontrados:
            inicializacao += f"{sensor} = 0 # Inicialização automática\n"
        return header + p.dev_section + "\n" + inicializacao + "\n" + p.cmd_section

    # DEV SEC -> dispositivos : DEV LIST fimdispositivos
    @_('DISPOSITIVOS ":" dev_list FIMDISPOSITIVOS')
    def dev_section(self, p):
        return "# Dispositivos declarados:\n" + p.dev_list

    # DEV LIST -> DEVICE DEV LIST | DEVICE
    @_('device dev_list')
    def dev_list(self, p):
        return p.device + "\n" + p.dev_list

    @_('device')
    def dev_list(self, p):
        return p.device

    # DEVICE -> ID DEVICE
    @_('ID')
    def device(self, p):
        return f"# Dev: {p.ID}"
    
    # DEVICE -> ID DEVICE [ID OBS]
    @_('ID "[" ID "]"')
    def device(self, p):
        self.sensores_encontrados.add(p.ID1)
        return f"# Dev: {p.ID0} (sensor: {p.ID1})"

    # CMD LIST -> CMD; CMD LIST | CMD;
    @_('cmd ";" cmd_section')
    def cmd_section(self, p):
        return p.cmd + "\n" + p.cmd_section

    @_('cmd ";"')
    def cmd_section(self, p):
        return p.cmd

    # CMD -> ATTRIB | OBSACT | ACT
    @_('attrib', 'obsact', 'act')
    def cmd(self, p):
        return p[0]

    # ATTRIB -> def ID OBS = VAL
    @_('DEF ID "=" val')
    def attrib(self, p):
        return f"{p.ID} = {p.val}"

    # --- Condicionais (OBSACT) ---
    # OBSACT -> quando OBS : ACT
    @_('QUANDO obs ":" act')
    def obsact(self, p):
        return f"if {p.obs}:\n    {p.act}"

    # OBSACT -> quando OBS : ACT senao ACT
    @_('QUANDO obs ":" act SENAO act')
    def obsact(self, p):
        return f"if {p.obs}:\n    {p.act0}\nelse:\n    {p.act1}"

    # --- Expressões Lógicas (OBS) ---
    # OBS -> ID OBS OP LOGIC V AL
    @_('ID OPLOGIC val')
    def obs(self, p):
        return f"{p.ID} {p.OPLOGIC} {p.val}"
    
    # OBS -> ID OBS OP LOGIC V AL AN D OBS
    @_('ID OPLOGIC val AND obs')
    def obs(self, p):
        return f"{p.ID} {p.OPLOGIC} {p.val} and {p.obs}"

    # --- Valores (VAL) ---
    # V AL -> N U M | BOOL
    # @_('NUM', 'BOOL_VAL')
    # def val(self, p):
    #     return str(p[0])

    @_('NUM', 'BOOL_VAL')
    def val(self, p):
        valor = str(p[0])
        # Tradução: ObsAct (TRUE) -> Python (True)
        if valor == 'TRUE':
            return 'True'
        elif valor == 'FALSE':
            return 'False'
        return valor

    # --- Ações (ACT) ---
    # ACT -> execute ACT ION em ID DEV ICE
    @_('EXECUTE action EM ID')
    def act(self, p):
        return f'{p.action}("{p.ID}")'

    # ACT -> alerta para ID DEV ICE : M SG
    @_('ALERTA PARA ID ":" STRING')
    def act(self, p):
        return f'alerta("{p.ID}", {p.STRING})'
        
    # ACT -> alerta para ID DEV ICE : M SG , ID OBS
    @_('ALERTA PARA ID ":" STRING "," ID')
    def act(self, p):
        return f'alerta("{p.ID0}", {p.STRING}, {p.ID1})'

    # --- Ações de Difundir (ACT - Difundir) ---
    # Regra Auxiliar: DEV LIST N -> ID | ID , DEV LIST N
    @_('ID')
    def dev_list_n(self, p):
        return [p.ID] 

    @_('ID "," dev_list_n')
    def dev_list_n(self, p):
        return [p.ID] + p.dev_list_n

    # ACT -> dif undir : M SG -> [DEV LIST N]
    @_('DIFUNDIR ":" STRING SETA "[" dev_list_n "]"')
    def act(self, p):
        return f'difundir({p.dev_list_n}, {p.STRING})'

    # ACT -> dif undir : M SG ID OBS -> [DEV LIST N]
    @_('DIFUNDIR ":" STRING ID SETA "[" dev_list_n "]"')
    def act(self, p):
        return f'difundir({p.dev_list_n}, {p.STRING}, {p.ID})'

    # --- Ações Primitivas (ACTION) ---
    # ACT ION -> ligar | desligar
    @_('LIGAR', 'DESLIGAR')
    def action(self, p):
        return p[0]

    def error(self, p):
        if p:
            print(f"Erro de sintaxe no token '{p.type}' valor '{p.value}' na linha {p.lineno}")
        else:
            print("Erro de sintaxe no final do arquivo")