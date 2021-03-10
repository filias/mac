import random

from mac.geral.models import Tela
from mac.exposicoes.models import Exposicao

#TELAS = random.shuffle(list(Tela.objects.all()))
TELAS = list(Tela.objects.all())
TELAS = random.sample(TELAS, 10)
DEFAULT_DICT = {'telas': TELAS}
#DEFAULT_DICT = {}

EXPOSICOES = Exposicao.objects.all()
    
