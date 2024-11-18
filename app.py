import pandas as pd 
import streamlit as st
import streamlit_shadcn_ui as ui
from datetime import datetime
# Sample data
st.header("My Fitness Log")
df = pd.DataFrame(columns=['Date', 'Exercise Name', 'Sets', 'Reps', 'Weight', 'Notes'])
Notes = ['Hard', 'EZ', 'Medium']
# Column configuration for st.data_editor
config = {
    'Date': st.column_config.DatetimeColumn(
            "Date", min_value=datetime(2024, 1, 1), max_value=datetime(2024, 12, 31),
            format="D MMM YYYY, h:mm a", step=60),
    'Exercise Name': st.column_config.TextColumn('Exercise name (required)', width='large', required=True),
    'Sets': st.column_config.NumberColumn('Sets (number of set)', min_value=0, max_value=1000),
    'Reps': st.column_config.NumberColumn('Reps (number of Repetition)', min_value=0, max_value=200),
    'Weight': st.column_config.NumberColumn('Weight (now)', min_value=0, max_value=200),
    'Notes': st.column_config.SelectboxColumn('Difficulty', options=Notes)
}
result = st.data_editor(df, column_config = config, num_rows='dynamic')
ui.table(result, maxHeight=300)