import streamlit as st
import pandas as pd
import numpy as np
import shap
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestRegressor

st.set_option('deprecation.showPyplotGlobalUse', False)

st.write("""
         # Boston House Price Prediction App
         """)

expander_bar = st.beta_expander("About")
expander_bar.markdown("""
    * **Python libraries:** pandas, streamlit, shap, matplotlib, sklearn
    * **Description:** This app predicts the **Boston House Price**!
    * **Data:** obtained from the (https://www.kaggle.com/c/boston-housing)
""")

# Loads Dataset
boston = datasets.load_boston()
X = pd.DataFrame(boston.data, columns=boston.feature_names)
Y = pd.DataFrame(boston.target, columns=['MEDV'])

st.sidebar.header('Specific Input Parameters')


def user_input_features():
    CRIM = st.sidebar.slider('CRIM', float(X.CRIM.min()), float(X.CRIM.max()), float(X.CRIM.mean()))
    ZN = st.sidebar.slider('ZN', float(X.ZN.min()), float(X.ZN.max()), float(X.ZN.mean()))
    INDUS = st.sidebar.slider('INDUS', float(X.INDUS.min()), float(X.INDUS.max()), float(X.INDUS.mean()))
    CHAS = st.sidebar.slider('CHAS', float(X.CHAS.min()), float(X.CHAS.max()), float(X.CHAS.mean()))
    NOX = st.sidebar.slider('NOX', float(X.NOX.min()), float(X.NOX.max()), float(X.NOX.mean()))
    RM = st.sidebar.slider('RM', float(X.RM.min()), float(X.RM.max()), float(X.RM.mean()))
    AGE = st.sidebar.slider('AGE', float(X.AGE.min()), float(X.AGE.max()), float(X.AGE.mean()))
    DIS = st.sidebar.slider('DIS', float(X.DIS.min()), float(X.DIS.max()), float(X.DIS.mean()))
    RAD = st.sidebar.slider('RAD', float(X.RAD.min()), float(X.RAD.max()), float(X.RAD.mean()))
    TAX = st.sidebar.slider('TAX', float(X.TAX.min()), float(X.TAX.max()), float(X.TAX.mean()))
    PTRATIO = st.sidebar.slider('PTRATIO', float(X.PTRATIO.min()), float(X.PTRATIO.max()), float(X.PTRATIO.mean()))
    B = st.sidebar.slider('B', float(X.B.min()), float(X.B.max()), float(X.B.mean()))
    LSTAT = st.sidebar.slider('LSTAT', float(X.LSTAT.min()), float(X.LSTAT.max()), float(X.LSTAT.mean()))
    data = {
        'CRIM': float(CRIM),
        'ZN': float(ZN),
        'INDUS': float(INDUS),
        'CHAS': float(CHAS),
        'NOX': float(NOX),
        'RM': float(RM),
        'AGE': float(AGE),
        'DIS': float(DIS),
        'RAD': float(RAD),
        'TAX': float(TAX),
        'PTRATIO': float(PTRATIO),
        'B': float(B),
        'LSTAT': float(LSTAT)  
    }
    return data

df = user_input_features()

st.write('### Specific Input Parameters')
st.write(df)
st.write('----')

# Build Reg Model
model = RandomForestRegressor()
model.fit(X,Y.values.ravel())

temp = np.ndarray(shape=(1,13))
np.append(temp, df.values())
    

# Apply model to make Prediction
prediction = model.predict(temp)


st.header('Prediction of MEDV')
st.write(prediction)
st.write('---')

# Explaining the models prediction using SHAP values
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

st.header('Feature Importance')
plt.title('Feature importance based on SHAP values')
shap.summary_plot(shap_values, X)
st.pyplot(bbox_inches='tight')
st.write('---')

plt.title('Feature improtance based on SHAP values (Bar)')
shap.summary_plot(shap_values, X, plot_type="bar")
st.pyplot(bbox_inches='tight')