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

data3 = {
    'semana': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
    'hrs': [106, 224, 284, 369, 351, 268, 460, 385, 450, 397, 314, 229, 157, 199, 136, 184, 164, 139, 144, 129, 138, 227]
}
no_hrs = pd.DataFrame(data3)

destajo_des = pd.DataFrame(data2)

st.title('_Control_ :red[Vori Vost] :sunglasses:') # titulo de la página

dest_button = st.button('Destajo') # creando botón para ver destajos

if dest_button:
    st.line_chart(total_dest, x='semana', y='suma', color="#FF0000")
    st.dataframe(total_dest, hide_index=True)

hrs_extra = st.button('Horas Extras') # creando botón para ver horas extras

if hrs_extra:
    st.line_chart(no_hrs, x='semana', y='hrs', color="#FF0000")
    st.dataframe(no_hrs, hide_index=True)
