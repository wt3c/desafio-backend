from collections import namedtuple


class Gera_log:
    """ Modulo será responsável pelo gerenciamento da criação do arquivo de log que será gravado em CSV"""
    def __init__(self, user, data_tjrj, pk):
        self.user = user

        # Converto o dict data_tjrj para uma namedtuple
        # Assim posso usar algo como 'data'.'doc'
        self.data = namedtuple('tjrj', data_tjrj.key())(**data_tjrj)
        self.pk = pk

    def gera_log(self):
        file = 'log.log'
        # restante do codigo...
