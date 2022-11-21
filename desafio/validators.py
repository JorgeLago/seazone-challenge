from desafio.models import Reserva

def check_in_valido(check_in, check_out):
    return check_in < check_out