

import pandas as pd
import numpy as np
import re

pd.set_option('display.max_columns', None)  # es para enseñar todas las columnas del df
pd.set_option('display.max_rows', None)     # es para enseñar todas las filas del df

import warnings
warnings.simplefilter('ignore')   # es para quitar warnings


# para pintar
import matplotlib as plt
import seaborn as sns

# para que salga el gráfico
# get_ipython().run_line_magic('matplotlib', 'inline')


# Importando csv


games = pd.read_csv('../data/data_games/games.csv')
games_detail = pd.read_csv('../data/data_games/games_details.csv')
teams = pd.read_csv('../data/data_games/teams.csv')

cities = pd.read_csv('../data/data_scraping/cities.csv')
player_size= pd.read_csv('../data/data_scraping/player_dim.csv')


# GAMES


games.columns=[c.lower() for c in games.columns]

games.game_date_est = games.game_date_est.astype('datetime64[ns]')

# Elimino duplicados de game_id

games.drop_duplicates(subset=['game_id'], inplace=True)

# Sustituir valores nulos por ceros

games.fillna(0, inplace=True)

games.info()


# Elimino duplicados de game_id

games.drop_duplicates(subset=['game_id'], inplace=True)


# ### Games detail

# In[32]:


games_detail.columns=[c.lower() for c in games_detail.columns]

games_detail.rename(columns={'to': 'turn'}, inplace=True)


# In[33]:


games_detail[games_detail.fgm.isna()]


# In[39]:


games_detail.drop(['nickname', 'start_position', 'comment'], axis=1, inplace=True)


# In[40]:


# Creo una coluna game_details_id

games_detail['games_detail_id'] = [i for i in range(1, len(games_detail)+1)]


# In[41]:


# Hago regex para eleminar caracters raros al final, sustituyo nulos y cambio a int64

games_detail['min'] = games_detail['min'].str.replace(r"[:]+\d+", "", regex=True)

# games_detail['min'].fillna(0, inplace=True)

games_detail['min'] = games_detail['min'].astype('float64')


# In[42]:


games_detail.info()


# In[45]:


games_detail[games_detail.fgm.isna()].head()


# In[13]:


# Sustituir valores nulos por ceros

games_detail.fillna(0, inplace=True)


# In[14]:


# Elimino duplicados de game_detail_id

games_detail.drop_duplicates(subset=['games_detail_id'], inplace=True)


# ### Teams

# In[15]:


teams.columns=[c.lower() for c in teams.columns]


# In[16]:


teams.city[teams.city=='Utah'] = 'Salt Lake City'
teams.city[teams.city=='Brooklyn'] = 'New York'
teams.city[teams.city=='Golden State'] = 'San Francisco'
teams.city[teams.city=='Minnesota'] = 'Minneapolis'
teams.city[teams.city=='Indiana'] = 'Indianapolis'


# ### Cities 

# In[17]:


cities.columns=[c.lower() for c in cities.columns]
cities.columns=[c.replace('\n', ' ') for c in cities.columns]
cities.columns=[c.replace(' ', '_') for c in cities.columns]
cities.columns=[c.replace('[c]', '') for c in cities.columns]


# In[18]:


# Hago regex para eleminar caracters raros al final 

cities.city = cities.city.str.replace(r"[[]+[\w]+[]]", "", regex=True)


# In[19]:


cities.drop(['2010_census', 'change', '2020_land_area', '2020_population_density'], axis=1, inplace=True)


# In[20]:



# Para añadir datos 

df2 = pd.DataFrame({'city': ['Toronto'],
                    'state' : ['Ontario'], '2020_census': ['7,853,815'], 'location': ['43.40°N 79.23°O']})

cities = pd.concat([cities, df2], ignore_index = True, axis = 0)


# In[21]:


# Creo una coluna city_id

cities['city_id'] = [i for i in range(1, len(cities)+1)]


# In[22]:


# Elimino duplicados de city_id

cities.drop_duplicates(subset=['city_id'], inplace=True)


# In[23]:


# Elimino duplicados de city_id

cities.drop_duplicates(subset=['city_id'], inplace=True)


# ### Modificio tabla teams

# In[24]:


# Hago un left join a teams por city para 

teams = teams.set_index('city').join(cities[["city", "city_id"]].set_index('city'), how='left')

teams.reset_index(inplace=True)


# In[25]:


# Sustituir valores nulos por ceros

teams.fillna(0, inplace=True)


# ### Players size

# In[26]:


player_size.columns=[c.lower() for c in player_size.columns]


# In[27]:


# Creo una columna y concateno first name y last name

player_size['player_name'] = player_size['first_name'] + ' ' + player_size['last_name']


# In[28]:


player_size.drop(['team', 'first_name', 'last_name'], axis=1, inplace=True)


# In[29]:


# Me quedo con las filas que no tengan nulos en esos campos

player_size = player_size[player_size[['height_feet', 'height_inches', 'weight_pounds']].notnull().any(axis=1)]


# In[30]:


# Elimino los valores nulos en player name

player_size = player_size[player_size.player_name.notna()]


# In[31]:


# Relleno la columna position con el 'unk'

player_size.position.fillna('unk', inplace=True)


# In[32]:


# Creo una columna con el peso y altura en SI

player_size['weight_kg'] = round(player_size.weight_pounds * 0.453592, 2)

player_size['height_cm'] = round((player_size.height_inches * 2.54) + (player_size.height_feet * 30.48))


# In[33]:


# Elimino las columnas que no quiero

player_size.drop(['height_feet','height_inches', 'weight_pounds'], axis=1, inplace=True)


# ### Modifico tabla games_detail

# In[34]:


### Modifico players para añadirle altura, peso y posición


games_detail = games_detail.set_index('player_name').join(player_size[["player_name", "position",'height_cm', 'weight_kg']].set_index('player_name'), how='left')

games_detail.reset_index(inplace=True)

games_detail.position.fillna('unk', inplace=True)

games_detail.fillna(0, inplace=True)


# ### Exporto los dataframe a csv

# In[35]:


games.to_csv('../data/data_sql/games.csv', sep=',', index=False)
games_detail.to_csv('../data/data_sql/games_detail.csv', sep=',', index=False)
teams.to_csv('../data/data_sql/teams.csv', sep=',', index=False)
cities.to_csv('../data/data_sql/cities.csv', sep=',', index=False)


# In[ ]:





# In[ ]:




