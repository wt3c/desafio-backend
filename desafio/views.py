from django.http import Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView

from .models import Documento
from .trata_tjrj import trata_tjrj
from .gerar_log import Gera_log

@login_required(login_url='/login/')
def homepage(request):
    return render(request, 'desafio/index.html')


@login_required(login_url='/login/')
class objDocumento(APIView):
    # pk é pasado como parametro pela url
    def get(self, request, pk):

        try:
            documento = Documento.objects.get(pk=pk)
        except Documento.DoesNotExist:
            raise Http404("Documento Não encontrado...")

        # SOAP
        data_dict = trata_tjrj(documento)

        # Inviar informações para o modulo que gerar os logs.
        user = request.GET['USER']
        log = Gera_log(user, data_dict, pk)
        log.gera_log()

        return render(request, 'desafio/desafioForm.html', {'form': data_dict})
