import pandas as pd
import streamlit as st
from streamlit_metrics import metric_row
import seaborn as sns
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
    page_title= "Airways conditions viz",
    page_icon= "📊",
    layout= 'wide'

)

st.markdown("<h1 style='text-align: center'>FLight Data Visualization</h1>", unsafe_allow_html=True)

sns.set_style('dark')
sns.set(rc={
    'axes.facecolor' :"#27a102",
    'figure.facecolor' : "#000000"
})
df = pd.read_csv('shipment_data.csv')


Average_Velocity = df["Velocity"].mean()
Average_Barometric_Altitude= df['Barometric_Altitude'].mean()
Average_Geoometric_Altitude = df['Geometric_Altitude'].mean()

left_column, middle_column, right_column = st.columns(3)
with left_column:
    st.subheader("Average Velocity")
    st.subheader(f"{Average_Velocity:.2f}")

with middle_column:
    st.subheader("Average Barometric Altitude")
    st.subheader(f"{Average_Barometric_Altitude:.2f}")

with right_column:
    st.subheader("Average Geoometric Altitude")
    st.subheader(f"{Average_Geoometric_Altitude:.2f}")

st.markdown("""---""")    

st.markdown("<h2 style='text-align: center'>Visualization</h2>", unsafe_allow_html=True)

fig, axs = plt.subplots(1, 3, figsize=(18, 6))


axs[0].scatter(df['Velocity'], df['Geometric_Altitude'], c='#ffbf00')
axs[0].set_xlabel('Velocity', color='white')
axs[0].set_ylabel('Geometric Altitude', color='white')
axs[0].tick_params(axis='x', colors='white')
axs[0].tick_params(axis='y', colors='white')

axs[1].scatter(df['Velocity'], df['Barometric_Altitude'], c='#ffbf00')
axs[1].set_xlabel('Velocity', color='white')
axs[1].set_ylabel('Barometric Altitude', color='white')
axs[1].tick_params(axis='x', colors='white')
axs[1].tick_params(axis='y', colors='white')

axs[2].scatter(df['Barometric_Altitude'], df['Geometric_Altitude'], c='#ffbf00')
axs[2].set_xlabel('Barometric Altitude', color='white')
axs[2].set_ylabel('Geometric Altitude', color='white')
axs[2].tick_params(axis='x', colors='white')
axs[2].tick_params(axis='y', colors='white')

st.pyplot(fig )

plt.show()


