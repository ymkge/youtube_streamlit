import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit入門')

st.write('Display Image')

# img = Image.open('./sora.png')
# st.image(img, caption='toro', use_column_width=True)

col1, col2, col3 = st.beta_columns(3)

with col1:
    st.header("toro")
    st.image("./toro.png")
with col2:
    st.header("kuro")
    st.image("./kuro.png")
with col3:
    st.header("sora")
    st.image("./sora.png")


option = st.selectbox(
    '好きな数字教えて',
    list(range(1, 11))
)
'あなたの好きな数字は,', option, 'です。'

text = st.text_input('あなたの趣味を教えてください。')
'あなたの趣味：', text

condition = st.slider('あなたの今の調子は？', 0, 100, 50)
'コンディション:',condition

df = pd.DataFrame(
    np.random.rand(31, 4)*[8000, 5000, 4000, 1000] +[15000, 12000, 7000, 5000],
    columns=['1_High学習層', '2_Middle学習層', '3_Low学習層', '4_休眠層']
)
if st.checkbox('Show Chart'):
    # st.line_chart(df)
    # st.area_chart(df)
    st.bar_chart(df)

if st.checkbox('Show Image'):
    img = Image.open('./toro.png')
    st.image(img, caption='toro', use_column_width=True)


left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラムです')
else:
    right_column.write('注目')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


st.write('プログレスバーの表示')
'Start!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!'

# df = pd.DataFrame(
#     np.random.rand(100, 2)/[50, 50] +[35.69, 139.70],
#     columns=['lat', 'lon']  ## 緯度と経度
# )

# st.map(df)

# st.dataframe(df.style.highlight_max(axis=0))
# st.table(df.style.highlight_max(axis=0))

# """
# # 章
# ## 節
# ### 項

# ```python
# import streamlit as st
# import numpy as np
# import pandas as pd
# ```
# """