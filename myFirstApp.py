import streamlit as st
from joblib import load
import numpy as np
def frist():
    st.title("降水预测系统")
    st.write("你好请输入以下数据")
    Tem_values = st.slider('温度', min_value=-20.0, max_value=40.0, value=(0.0, 20.0), step=0.1)
    st.write('最高温度为：', Tem_values[1])
    st.write('最低温度为：', Tem_values[0])
    T_min = Tem_values[0]
    T_max = Tem_values[1]
    T_ave = (T_max+T_min)/2
    st.write('平均温度为：', T_ave)
    Press = st.slider('海平面大气压', min_value=900.0, max_value=1100.0, value=1000.0, step=0.1)
    st.write('海平面大气压为：', Press)
    Wind_dir = st.slider('风向', min_value=0, max_value=360, value=180)
    st.write('风向为：', Wind_dir)
    Wind_sp = st.slider('风速', min_value=0.00, max_value=20.00, value=10.00, step=0.01)
    st.write('风速为：', Wind_sp)
    Cloud_c = st.slider('云层', min_value=0.000, max_value=1.000, value=0.500, step=0.125)
    st.write('云层为：', Cloud_c)
    st.write('点击下列按钮得出降水预测')
    if st.button('按钮'):
        file_path = 'estimator.pickle'
        estimator_new = load(filename="estimator.pickle")
        X = np.array([T_ave, T_max, T_min, Press, Wind_dir, Wind_sp, Cloud_c])
        X = X.reshape(1, -1)
        # 将Series转化为二维数组
        # print(X)
        pre_y = estimator_new.predict(X)
        st.write('预测降水量为：', pre_y[0], 'mm')
if __name__ == '__main__':
    frist()
