import json
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql+psycopg2://parsersmc:xE5CzwD3EdK@127.0.0.1/parsers_main_controller_db')
with open('countries_w_d.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# countries = data['countries']
# for country in countries:
#     country['vk_id'] = country.pop('id')
#     country['name'] = country.pop('title')

cities = data['cities']
new_cities = []
city_id = []
for city in cities:
    if 'country_id' not in city.keys():
        continue
    if city['id'] not in city_id:
        city_id.append(city['id'])
        new_cities.append({'city_vk_id': city['id'],'city_name': city['title'] + ' ' + city.get('region', ''), 'vk': city['country_id']})
    
# country_df = pd.DataFrame(countries)
cities_df = pd.DataFrame(new_cities)

# country_df.to_sql("countryvk", engine, schema='public', if_exists='append', index=False)
cities_df.to_sql("cityvk", engine, schema='public', if_exists='append', index=False)
