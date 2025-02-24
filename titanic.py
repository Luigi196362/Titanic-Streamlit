import pandas as pd
import streamlit as st
import numpy as np
import datetime
import matplotlib.pyplot as plt
titanic_link = './titanic.csv'
titanic_data = pd.read_csv(titanic_link)
# Create the title for the web app
st.title("Streamlit Avanzado")

sidebar = st.sidebar

sidebar.title("Luis Enrique Romero Pérez")

sidebar.write("Matricula: zs21004524.")
sidebar.write("zs21004524@estudiantes.uv.mx")

sidebar.image("https://firebasestorage.googleapis.com/v0/b/paradigmas-luigi196362.appspot.com/o/javascript%2Fimages%2Fcredencial.jpg?alt=media&token=ffba3513-0c65-4540-8bdf-140a9ba8f468")

# Give user the current date
today = datetime.date.today()
today_date = st.date_input('Current date', today)
st.success('Current date: `%s`' % (today_date))
# Display the content of the dataset if checkbox is true
st.header("Dataset")
agree = st.checkbox("show DataSet Overview ? ")
if agree:
    st.dataframe(titanic_data)
    

# Select the embark town of the passanger and then display the dataset with this selection
selected_town = st.radio("Select Embark Town",
titanic_data['embark_town'].unique())
st.write("Selected Embark Town:", selected_town)
st.write(titanic_data.query(f"""embark_town==@selected_town"""))
st.markdown("___")
# Select a range of the fare and then display the dataset with this selection
optionals = st.expander("Optional Configurations", True)
fare_min = optionals.slider(
    "Minimum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
fare_max = optionals.slider(
    "Maximum Fare",
    min_value=float(titanic_data['fare'].min()),
    max_value=float(titanic_data['fare'].max())
)
subset_fare = titanic_data[(titanic_data['fare'] <= fare_max) & (fare_min <= titanic_data['fare'])]
st.write(f"Number of Records With Fare Between {fare_min} and {fare_max}: {subset_fare.shape[0]}")
# Display of the dataset
st.dataframe(subset_fare)

#Graficas

fig, ax = plt.subplots()
ax.hist(titanic_data.fare)
st.header("Histograma del Titanic")
st.pyplot(fig)
st.markdown("___")
fig2, ax2 = plt.subplots()
y_pos = titanic_data['class']
x_pos = titanic_data['fare']
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title('¿Cuanto pagaron las clases del Titanic')
st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)
st.markdown("___")
fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.age, titanic_data.fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Grafica de Dispersión del Titanic")
st.pyplot(fig3)

#Mapa San Francisco

map_data = pd.DataFrame(
 np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
 columns=['lat', 'lon'])

st.map(map_data)
#Mapa NYC

st.title('Uber pickups in NYC')
DATE_COLUMN = 'date/time'
DATA_URL = ('./uber_dataset.csv')
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("Done! (using st.cache)")
# Some number in the range 0-23
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader('Map of all pickups at %s:00' % hour_to_filter)
st.map(filtered_data)