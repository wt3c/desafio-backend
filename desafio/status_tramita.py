from .models import Documento
from .trata_tjrj import trata_tjrj

""" Modulo responsavél por juntar várias informações para serem comparadas
"""


def get_status_banco():
    """Considerando que a documentos tem um campo que contém a informação de status do processo, gero uma lista
        com todos resultado.
    """
    data = Documento.objetos.filter(status != 'FINALIZADO')
    return data


def get_user_log(id_documento):
    """Retorna lista de usuários do arquivo de log que o status seja diferente de 'FINALIAZDO. """
    pass


def envia_email(user, id_banco):
    """Envio por email informações de alterações a todo usuário envolvido no processo do documento"""
    pass


def check_status():
    # Recebo lista com os processos
    proc_pedentes = get_status_banco()

    for procdb in proc_pedentes:
        # Envio informções do banco que tratadas e retornandas em formatos de dict
        for tjrj in trata_tjrj(procdb):
            # Faço as comparações entre os dois bancos de informações
            if (tjrj.id == procdb.id) and (tjrj.status != procdb.status):
                user = get_user_log(procdb.id)
                envia_email(user, procdb.id)
