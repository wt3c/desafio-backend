import traceback
import xmltodict


def trata_tjrj(documento):
    doc_soap_xml = lib_soap("endpoit_soap/info_de_autenticação/{idtram}".format(idtram=documento.id_tjrj))
    data_xml = doc_soap_xml.read()

    data_dict = None
    try:
        data_dict = xmltodict.parse(data_xml)
    except:
        print("Erro no parse do XML para DICT. "
              "{ERRO} ".format(ERRO=traceback.format_exc()))

    return data_dict
