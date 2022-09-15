import streamlit as st
import pandas as pd
import numpy as np

mean = 3
n_rows = 10
md_results = f"The mean is **{mean:.2f}** and there are **{n_rows:,}**."
st.markdown(md_results)
st.latex(r''' e^{i\pi} + 1 = 0 ''')

df = pd.DataFrame({
    'scores': [0.6863609552383423, 0.5861597061157227],
})

st.bar_chart(df)


def visualize_confidence_level(prediction_proba):
    """
    this function uses matplotlib to create inference bar chart rendered with streamlit in real-time
    return type : matplotlib bar chart
    """
    st.set_option('deprecation.showPyplotGlobalUse', False)
    data = (prediction_proba[0] * 100).round(2)
    grad_percentage = pd.DataFrame(data=data, columns=['Percentage'], index=['Low', 'High'])
    ax = grad_percentage.plot(kind='barh', figsize=(7, 4), color='#285ed6', zorder=10, width=0.5)
    ax.legend().set_visible(False)
    ax.set_xlim(xmin=0, xmax=100)

    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)

    ax.tick_params(axis="both", which="both", bottom="off", top="off", labelbottom="on", left="off", right="off",
                   labelleft="on")

    vals = ax.get_xticks()
    for tick in vals:
        ax.axvline(x=tick, linestyle='dashed', alpha=0.4, color='#eeeeee', zorder=1)

    ax.set_xlabel(" Percentage(%) Confidence Level", labelpad=2, weight='bold', size=12)
    ax.set_ylabel("Wine Quality", labelpad=10, weight='bold', size=12)
    ax.set_title('Prediction Confidence Level ', fontdict=None, loc='center', pad=None, weight='bold')

    st.pyplot()
    return


visualize_confidence_level(np.array([[0.6863609552383423, 0.5861597061157227]], dtype=np.float32))
