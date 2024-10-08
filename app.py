import numpy as np
import streamlit as st 
from tslearn.neighbors import KNeighborsTimeSeriesClassifier

# load arrays
x_train = np.load("x_train.npy")
y_train = np.load("y_train.npy")

# recreate model
clf = KNeighborsTimeSeriesClassifier(n_neighbors=5, 
                                     metric="dtw", 
                                     weights="distance",
                                     verbose=1)
clf.fit(x_train, y=y_train)

# define labels
labels = {0: 73, 1: 80, 2: 90, 3: 100}
  
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
            fs1_arr = np.array([float(x) for x in fs1.split(",")][::10])
            ps2_arr = np.array([float(x) for x in ps2.split(",")][::100])
            arr = np.concatenate([fs1_arr, ps2_arr])
            
            # predict
            clf_pred = clf.predict(arr)[0]
            valve_value = labels[clf_pred]

            st.success(f'The valve condition for this cycle is {valve_value}')
            
        except:
            st.error("Wrong input format\n", icon="🚨")        

if __name__=='__main__': 
    main() 