import pandas as pd
import googlemaps


gmaps = googlemaps.Client(key='AIzaSyDrAKbe_yqbOor3PXwCptz6KDSbyfr_UOQ')

search_results = gmaps.places(query='temakeria em Praia Grande')

dados = []

for result in search_results['results']:
    place_id = result['place_id']
    place_details = gmaps.place(place_id=place_id)['result']
    
    nome = place_details.get('name', 'Não disponível')
    endereco = place_details.get('formatted_address', 'Não disponível')
    telefone = place_details.get('formatted_phone_number', 'Não disponível')
    site = place_details.get('website', 'Não disponível')
    
    dados.append([nome, endereco, telefone, site])

df = pd.DataFrame(dados, columns=['Nome', 'Endereço', 'Telefone', 'Site'])

df.to_excel('temakerias_pg.xlsx', index=False)

print("Dados salvos com sucesso em 'temakerias_pg.xlsx'.")
