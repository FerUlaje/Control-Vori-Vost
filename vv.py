import pandas as pd
import streamlit as st
import plotly.express as px

data = {
    'semana': [16, 17, 18, 19, 20, 21, 22],
    'suma': [272, 287, 207, 205, 214, 221, 221]
}

total_dest = pd.DataFrame(data)

data2 = {
    'semana': [16, 17, 18, 19, 20, 21, 22],
    'ML': [215, 194, 137, 135, 165, 159, 169],
    'pzas': [43, 83, 55, 54, 36, 50, 40],
    'dia': [15, 10, 15, 16, 12, 12, 13]
}

destajo_des = pd.DataFrame(data2)

st.title('_Control_ :red[Vori Vost] :sunglasses:')