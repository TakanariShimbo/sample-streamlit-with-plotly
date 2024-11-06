import numpy as np
import plotly.figure_factory as ff
import streamlit as st


x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

hist_data = [x1, x2, x3]
group_labels = ["Group 1", "Group 2", "Group 3"]

fig = ff.create_distplot(hist_data=hist_data, group_labels=group_labels, bin_size=[0.1, 0.25, 0.5])

st.plotly_chart(figure_or_data=fig, use_container_width=True)
