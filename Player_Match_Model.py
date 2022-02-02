import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import RendererAgg
from matplotlib.figure import Figure
import seaborn as sns
import statsmodels
from statsmodels.nonparametric.smoothers_lowess import lowess
import streamlit as st

st.set_page_config(page_title='Recruit Dashboard',
                   page_icon='https://upload.wikimedia.org/wikipedia/commons/thumb/f/f5/Notre_Dame_Fighting_Irish_logo.svg/1200px-Notre_Dame_Fighting_Irish_logo.svg.png',
                   layout="wide")

# READ DATA --------------------------------------------------------------------
@st.cache(allow_output_mutation=True)
def get_pbp():

    data_ = pd.read_excel('Consolidated_UC_Data+NDwnew.')
    return data_

data = get_pbp()

# ROW 1 ------------------------------------------------------------------------

row1_spacer1, row1_1, row1_spacer2, row1_2, row1_spacer3 = st.beta_columns(
    (.1, 2, 1.5, 1, .1)
    )

row1_1.title('Recruit Dashboard')

with row1_2:
    st.write('')
    row1_2.subheader(
    'Created by [Charlie Pallett](https://twitter.com/ChazPalz)')
 

# ROW 2 ------------------------------------------------------------------------

row2_spacer1, row2_1, row2_spacer2, row2_2, row2_spacer3 = st.beta_columns(
    (.1, 1.6, .1, 1.6, .1)
    )

with row2_1:

    options_p = df.groupby(['receiver','posteam'])[['play_id']].count().reset_index()
    options_p = options_p.loc[options_p.play_id>29]
    player_list = options_p['receiver'].to_list()

    player_data['pbp_name'] = [item[0] + '.'+ ''.join(item.split()[1:]) for item in player_data['full_name']]
    pd_filt = player_data.loc[(player_data['pbp_name'].isin(player_list)) &
                          ((player_data['position'] == 'WR') |
                          (player_data['position'] == 'TE'))]

    pd_filt = pd_filt.loc[~pd_filt.full_name.isin(remove)]
    player_list = pd_filt['pbp_name'].to_list()
    pd_filt = pd_filt.filter(
                ['full_name','pbp_name','team']
                    ).dropna().reset_index(drop=True).sort_values('full_name')
    records = pd_filt.to_dict('records')
    selected_data = st.selectbox('Select a Player', options=records,
        format_func=lambda record: f'{record["full_name"]}')

    player = selected_data.get('pbp_name')
    team = selected_data.get('team')


with row2_2:
    start_week, stop_week = st.select_slider(
    'Select A Range of Weeks',
    options=list(range(1,22)),
    value=(1,21))
    
    
# ROW 1 ------------------------------------------------------------------------

st.write('')
row1_space1, row1_1, row1_space2, row1_2, row1_space3, row1_3, row1_space4 = st.beta_columns(
    (.15, 1, .3, 1, .00000001, 3, 0.15))

with row1_1, _lock:

    player_filter = player_data.loc[(player_data['pbp_name'] == player) &
                                    (player_data['team'] == team)]
    url = player_filter['headshot_url'].dropna().iloc[-1]
    st.subheader('Player Info')
    st.image(url, width=300)



with row1_2, _lock:
    st.subheader(' ')
    st.text(' ')
    st.text(
        f"Name: {player_filter['full_name'].to_string(index=False).lstrip()}"
        )
    st.text(
        f"College: {player_filter['college'].to_string(index=False).lstrip()}"
        )
    st.text(
        f"Position: {player_filter['position'].to_string(index=False).lstrip()}"
        )
    st.text(
        f"Birthday: {player_filter['birth_date'].to_string(index=False).lstrip()}"
        )
    st.text(
        f"Height: {player_filter['height'].to_string(index=False).lstrip()}"
        )
    st.text(
        f"Weight: {player_filter['weight'].astype(int).to_string(index=False).lstrip()}"
        )

    
# Radar chart 
radar_chart_fig = radar_chart(runs)
st.plotly_chart(radar_chart_fig)