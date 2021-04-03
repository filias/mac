import random

from mac.exposicoes.models import Exposicao
from mac.geral.models import Tela

TELAS = list(Tela.objects.all())
TELAS = random.sample(TELAS, 10)
DEFAULT_DICT = {"telas": TELAS}

EXPOSICOES = Exposicao.objects.all()
