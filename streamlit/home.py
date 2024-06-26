import streamlit as st
import os
import csv
import sys
from pathlib import Path
import pandas as pd
from streamlit.components.v1 import components
# sourcecode_path = Path(os.getcwd()).parent / 'source_code'
sourcecode_path = Path(os.getcwd()).parent
sys.path.append(sourcecode_path)
# from word2csv import get_file_locations, extract_info_from_docx, convert_table_to_csv_file
# from data_cleaning import clean_date_format, fix_year_format, clean_mem_status, clean_transaction_amount
# from pdf2csv_easyOCR import ocr_result
# from source_code.word2csv import get_file_locations, extract_info_from_docx, convert_table_to_csv_file
# from source_code.geo_viz import init_map, create_point_map, plot_from_df, load_df, load_map_region, load_map_state, main_region, main_state, plots
# from source_code.data_cleaning import clean_date_format, fix_year_format, clean_mem_status, clean_transaction_amount
# from source_code.pdf2csv_easyOCR import ocr_result

# st.title('Welcome!')
st.set_page_config(
    page_title="Introduction",
    page_icon="👋"
)

st.title('Welcome to 🪄:blue[Docx2Dashboard]')
st.subheader('Introducing Our Solution for Digital Transformation', divider='grey')
# st.subheader("💁‍♀️ Empowering unbanked Nigerian women through Digital Transformation.")
# st.subheader("📑 Convert paper-based financial records into CSV files effortlessly.")
# st.subheader("📊 Access dynamic visual dashboards for comprehensive financial management.")

# introduction = '''
# 💁‍♀️ Empowering **unbanked women** in Nigeria through :blue[Digital Transformation].
# 📑 Convert paper-based financial records into **CSV files** effortlessly.
# 📊 Access dynamic *visual dashboards* for comprehensive financial management.
# '''
# st.markdown(introduction)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        '<div style="text-align: center; background-color: lightsteelblue; padding: 10px; height:250px; border-radius:10px;"><h1>💁‍♀</h1><p>Empowering <strong>unbanked women</strong> in Nigeria through Digital Transformation</p></div>',
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        '<div style="text-align: center;background-color: lightsteelblue; padding: 10px; height:250px; border-radius:10px;"><h1>📑</h1><p>Convert paper-based financial records into <strong>CSV files</strong> effortlessly.</p></div>',
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        '<div style="text-align: center;background-color: lightsteelblue; padding: 10px; height:250px; border-radius:10px;margin-bottom:20px;"><h1>📊</h1><p>Access dynamic <em>visual dashboards</em> for comprehensive financial management.</p></div>',
        unsafe_allow_html=True
    )


st.image('Welcome_image.png', caption='How Docx2Dashboard works')
st.text("This App is developed in the GWU Data Science Capstone Project")
st.text("With World Bank Social Sustainability and Inclusion unit")
st.text("Team Member: Brooklyn Chen, Jiwoo Suh, Sanjana Godolkar")
