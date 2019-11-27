from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

error_messages = {
    'placa_error': _('A placa deve possuir o formato AAA-9999.'),
    'saiupagou!': _('Não pode haver saída sem pagamento.')
}

def placa_validator(value):
    tamanho_hifen = False
    letras = False
    numeros = True
    try:
        if str(value)[3] == '-' and len(str(value)) == 8:
            tamanho_hifen = True
    except:
        tamanho_hifen = False
    try:
        teste = int(str(value)[0])
    except:
        try:
            teste = int(str(value)[1])
        except:
            try:
                teste = int(str(value)[2])
            except:
                letras = True
    try:
        teste = int(str(value)[4:])
    except:
        numeros = False
    if tamanho_hifen and letras and numeros:
        pass
    else:
        raise ValidationError(
            error_messages['placa_error']
        )
    