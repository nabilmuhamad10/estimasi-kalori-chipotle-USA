import pickle
import streamlit as st

model = pickle.load(open('estimasi_calChipotle.sav', 'rb'))

st.title('Estimasi')
st.subheader('Jumlah Kalori Makanan di Chipotle USA')


TotalFats = st.number_input('Input Total Fats(g)')
Cholesterol = st.number_input('Input Cholesterol(mg)')
Sodium = st.number_input('Input Sodium(g)')
Carbohydrates = st.number_input('Input Carbohydrates(g)')
DietaryFiber = st.number_input('Input DietaryFiber(g)')
Sugar = st.number_input('Input Sugar(g)')
Protein = st.number_input('Input Protein(g)')


predict = ''

if st.button('Cek Jumlah Kalori'):
    predict = model.predict(
        [[TotalFats,Cholesterol,Sodium,Carbohydrates,DietaryFiber,Sugar,Protein]]
    )
    st.write ('Estimasi jumlah kalori makanan di Chipotle USA (kCal) : ', predict)