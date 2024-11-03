Para instalar as bibliotecas
pip install -r requirements.txt

Para rodar o aplicativo
python main.py

Quando o aplicativo rodar, será perguntado no terminal se quer fazer o download dos arquivos, tratar os dados,
processar os dados e rodar o app localmente. responda com 'sim' ou 'nao'.
Após fazer o git pull a primeira vez é necessário fazer o download, tratar os dados e processar os dados para
conseguir rodar o app, nas proximas vezes, não é necessário, respondendo 'sim' apenas para rodar o app localmente.

Essa versão do código esta com o número de nós da malha viária reduzido, o que faz com que as rotas calculadas
fiquem com linhas mais retas e não sigam inteiramente as vias, mas os pontos inicial e final continuam
corretos.
Para alterar isso comente a linha numero 55 (G = ox.graph_from_polygon(polygon, network_type='all'))
e descomente a linha 54 (#G = ox.graph_from_polygon(polygon, network_type='all', simplify=False)).