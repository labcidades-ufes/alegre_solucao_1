from coleta.download_dados import *
from tratamento.tratamento import *
from processamento.processamento import *
from exibicao.exibicao import rodar_app

def ask_for_download():
    while True:
        answer = input("Deseja fazer o download dos dados? (sim/nao): ").lower()
        if answer in ['sim', 'nao']:
            if(answer == 'sim'):
                return True
            else:
                return False
        else:
            print("Por favor, responda com 'sim' ou 'não'.")


def ask_for_tratamento():
    while True:
        answer = input("Deseja fazer o tratamento dos dados? (sim/nao): ").lower()
        if answer in ['sim', 'nao']:
            if(answer == 'sim'):
                return True
            else:
                return False
        else:
            print("Por favor, responda com 'sim' ou 'não'.")


def ask_for_process():
    while True:
        answer = input("Deseja fazer o processamento dos dados? (sim/nao): ").lower()
        if answer in ['sim', 'nao']:
            if(answer == 'sim'):
                return True
            else:
                return False
        else:
            print("Por favor, responda com 'sim' ou 'não'.")


def ask_for_running_app():
    while True:
        answer = input("Deseja rodar o app localmente? (sim/nao): ").lower()
        if answer in ['sim', 'nao']:
            if(answer == 'sim'):
                return True
            else:
                return False
        else:
            print("Por favor, responda com 'sim' ou 'não'.")


def main():
    print("Iniciando...")

    if ask_for_download():
        print("Iniciando downloads...")
        
        download_limites_municipios()
        download_unidades_saude_ES()
        download_population_alegre()
    else:
        print("Download ignorado.")

    if ask_for_tratamento():
        print("Iniciando tratamento dos dados...")

        obter_limite_municipio_alegre()
        obter_hexagonos_alegre()
        obter_unidades_saude_alegre()
    else:
        print("Tratamento dos dados ignorado.")

    if ask_for_process():
        print("Iniciando processamento dos dados...")

        obter_centroides()        
        obter_dados_viarios_expandido()
        obter_rotas_centroide_para_saude()
        obter_gdf_peso_hexagonos()
    else:
        print("Processamento ignorado.")

    if ask_for_running_app():
        print("Iniciando aplicação shiny...")

        #App
        rodar_app()
    else:
        print("Encerrando!")
    


# Bloco principal
if __name__ == "__main__":
    main()