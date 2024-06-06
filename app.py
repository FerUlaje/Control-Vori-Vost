import pandas as pd
import plotly.express as px
import streamlit as st

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

data4 = {
    'semana': [ 16, 17, 18, 19, 20, 21, 22],
    'costo': [132512, 119821, 105022, 109721, 118776, 122447, 110546]
}

costo_dest = pd.DataFrame(data4)

data5 = {
    'semana': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22],
    'costo': [9647, 18356, 23674, 28734, 29373, 25025, 40250, 35745, 40886, 34522, 28398, 20454, 14373, 20002, 13682, 16385, 14094, 11896, 12404, 11645, 12010, 18991]
}

costo_hrs = pd.DataFrame(data5)

st.title('_Control_ :red[Vori Vost] :pinched_fingers:') # titulo de la página

dest_button = st.button('Destajo') # creando botón para ver destajos


if dest_button:
    st.subheader('Destajos', divider='red')
    st.subheader('ML, Piezas y Días')
    fig1 = st.line_chart(total_dest, x='semana', y='suma', color="#FF0000")
    fig2 = st.dataframe(total_dest, hide_index=True)
    st.subheader('Costo')
    fig3 = st.line_chart(costo_dest, x='semana', y='costo', color="#FF0000")
    fig4 = st.dataframe(costo_dest, column_config={
        "semana":"Semana",
        "costo": st.column_config.NumberColumn("Costo", format="$%d"),
    }, hide_index=True)


hrs_extra = st.button('Horas Extras') # creando botón para ver horas extras

if hrs_extra:
    st.subheader('N° y Costo de Horas Extras', divider='rainbow')
    st.subheader('N° de Horas Extras')
    st.line_chart(no_hrs, x='semana', y='hrs', color="#FF0000")
    st.dataframe(no_hrs, hide_index=True)
    st.subheader('Costo de Horas Extras')
    st.line_chart(costo_hrs, x='semana', y='costo')
    st.dataframe(costo_hrs.style.highlight_max(axis=0), hide_index=True)

