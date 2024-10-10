import numpy as np
import streamlit as st 
from tslearn.neighbors import KNeighborsTimeSeriesClassifier
import pickle

# load arrays
x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")

# load model
clf = KNeighborsTimeSeriesClassifier.from_pickle("nn3_valve_model.pkl")
clf.fit(x_train, y=y_train)

# define labels
labels = {0: "not optimal (73%)", 
          1: "not optimal (80%)", 
          2: "not optimal (90%)", 
          3: "optimal (100%)"}
  
def main(): 
    st.title("Valve Condition Predictor")
    html_temp = """
    <div style="background:blue ;padding:10px">
    <h2 style="color:white;text-align:center;">Valve Condition Prediction App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html = True)
    
    fs1 = st.text_input("FS1: Volume flow (600 values separated with a comma)", '') 
    ps2 = st.text_input("PS2: Pressure (6000 values separated with a comma)", '') 
    
    # launch prediction after click on the predict button
    if st.button("Predict"): 
        try:
            fs1_arr = np.array([float(x) for x in fs1.split(",")])
            ps2_arr = np.array([float(x) for x in ps2.split(",")])
            if len(fs1_arr) != 600 or len(ps2_arr) != 6000:
                st.warning('Wrong input size, may produce inaccurate prediction!', icon="⚠️")
            arr = np.concatenate([fs1_arr[::10], ps2_arr[::100]])
            arr = (arr - np.mean(arr))/np.std(arr)
            
            # predict
            clf_pred = clf.predict(arr)[0]
            valve_value = labels[clf_pred]

            st.success(f'The predicted valve condition for this cycle is {valve_value}.')
            
        except:
            st.error("Wrong input format\n", icon="🚨")        

if __name__=='__main__': 
    main() 