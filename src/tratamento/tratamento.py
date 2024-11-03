import os
import geopandas as gpd

def obter_limite_municipio_alegre():
    # Definir o caminho relativo
    caminho_municipios = os.path.join("..", "dados", "dados_baixados", "limites_municipios_ES.geojson")
    
    # Carregar os dados
    gdf_municipios = gpd.read_file(caminho_municipios)
    
    # Filtra o limite da cidade de Alegre
    gdf_municipio_alegre = gdf_municipios[gdf_municipios['nome'] == 'Alegre']
    
    #salvar
    gdf_municipio_alegre.to_file(os.path.join("..", "dados", "dados_tratados", "limite_municipio_alegre.geojson"), driver='GeoJSON')
    print("Limite de municipio de Alegre criado.")


# Função para realizar a interseção e filtrar por Alegre
def obter_hexagonos_alegre():
    # Definir o caminho relativo
    caminho_municipios = os.path.join("..", "dados", "dados_tratados", "limite_municipio_alegre.geojson")
    caminho_population = os.path.join("..", "dados", "dados_baixados", "kontur_population_BR_20231101.gpkg")
    
    # Carregar os dados
    municipio_alegre = gpd.read_file(caminho_municipios)
    population = gpd.read_file(caminho_population)

    #ajusta o crs
    municipio_alegre = municipio_alegre.to_crs(epsg=31984)
    population = population.to_crs(epsg=31984)
    
    #recorta o geodataframe de população pelo limite da cidade de Alegre
    intersected = gpd.overlay(population, municipio_alegre, how='intersection')
    
    if intersected.empty:
        print("Nenhuma interseção encontrada para o município de Alegre.")
    
    #salva o arquivo
    intersected.to_file(os.path.join("..", "dados", "dados_tratados", "population_alegre.geojson"), driver='GeoJSON')
    print("População de Alegre criada.")


def obter_unidades_saude_alegre():
    # Definir o caminho relativo
    caminho_geojson_unidades_saude_ES = os.path.join("..", "dados", "dados_baixados", "unidades_saude_ES.geojson")
    
    # Carregar os dados
    gdf_unidades_saude_ES = gpd.read_file(caminho_geojson_unidades_saude_ES)

    # Filtrar as unidades de saúde pela cidade de Alegre
    gdf_unidades_saude_alegre = gdf_unidades_saude_ES.loc[gdf_unidades_saude_ES['MUNICIPIO'] == 'Alegre']

    #Filtrar as unidades de saude por informações passadas pelo staff de Alegre
    gdf_unidades_saude_alegre = gdf_unidades_saude_alegre.loc[
        (gdf_unidades_saude_alegre['NOME'].str.contains('Estratégia de Sáude', na=False, case=False)
        | gdf_unidades_saude_alegre['NOME'].str.contains('US de Araraí', na=False, case=False)
        | (gdf_unidades_saude_alegre['NOME'].str.contains('US de Boa Vista', na=False, case=False))
        | (gdf_unidades_saude_alegre['NOME'].str.contains('US de Santa Angélica', na=False, case=False))
        | (gdf_unidades_saude_alegre['NOME'].str.contains('US de Floresta', na=False, case=False))
        | (gdf_unidades_saude_alegre['NOME'].str.contains('US de Roseira', na=False, case=False)))
        & (~gdf_unidades_saude_alegre['NOME'].str.contains('Estratégia de Sáude da FamílIa III - Rua 13 de Maio', na=False, case=False))
    ]

    #salva o arquivo
    gdf_unidades_saude_alegre.to_file(os.path.join("..", "dados", "dados_tratados", "unidades_saude_alegre.geojson"), driver='GeoJSON')
    print("Unidades de saude de Alegre criadas.")

    #unidades de saude de apoio de Alegre
    gdf_unidades_saude_apoio = gdf_unidades_saude_alegre.loc[
        (gdf_unidades_saude_alegre['NOME'].str.contains('US de Boa Vista', na=False, case=False))
        | (gdf_unidades_saude_alegre['NOME'].str.contains('US de Santa Angélica', na=False, case=False))
        | (gdf_unidades_saude_alegre['NOME'].str.contains('US de Floresta', na=False, case=False))
        | (gdf_unidades_saude_alegre['NOME'].str.contains('US de Roseira', na=False, case=False))]

    #salva o arquivo
    gdf_unidades_saude_apoio.to_file(os.path.join("..", "dados", "dados_tratados", "unidades_saude_apoio_alegre.geojson"), driver='GeoJSON')
    print("Unidades de saude de apoio de Alegre criadas.")