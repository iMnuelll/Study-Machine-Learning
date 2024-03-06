# import streamlit as st
# st.write(
#     """
#     # My first app
#     Hello, Ini penggunaan streamlit pertama kamu!
#     """
# )
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
 
x = np.random.normal(15, 5, 250)
 
fig, ax = plt.subplots()
ax.hist(x=x, bins=15)
st.pyplot(fig)