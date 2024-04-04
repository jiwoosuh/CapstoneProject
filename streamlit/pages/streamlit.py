import streamlit as st
import os
import csv
import sys
from pathlib import Path
import pandas as pd
from pathlib import Path
from streamlit.components.v1 import components
st.set_option('deprecation.showPyplotGlobalUse', False)
sys.path.append(Path(os.getcwd()).parent)
from source_code.word2csv import get_file_locations, extract_info_from_docx, convert_table_to_csv_file
# from source_code.geo_viz import init_map, create_point_map, plot_from_df, load_df, load_map_region, load_map_state, main_region, main_state, plots
from source_code.data_cleaning import clean_date_format, fix_year_format, clean_mem_status, clean_transaction_amount
from source_code.pdf2csv import pdf_to_images,ocr_handwritten_text, get_list_of_files


def main():
    st.set_page_config(layout='wide')

    st.title("🇳🇬 Nigeria For Women Program Scale-up Project")
    st.subheader("GWU Data Science Capstone Project - 2024 Spring")
    st.write("With World Bank 🌐 Social Sustainability and Inclusion")
    st.write("👩‍💻👩‍💻👩‍💻: Brooklyn Chen, Jiwoo Suh, Sanjana Godolkar")
    st.write("Instructor: Abdi Awl")
    st.write("[Trello Board](https://trello.com/b/ytzd5Ve7/dats6501-brooklyn-chen-sanjana-godolkar)")

    # Sidebar navigation
    # page = st.sidebar.selectbox("Select a page",
    #                             ["Project Overview", "Main Tasks", "Methodology",
    #                              "Data Preprocessing", "OCR Handwritten PDF", "Transaction Analysis",
    #                              "Visual Analysis", "Geovisualization", "Challenges", "Conclusion", "Project Impact & Application"])

    page = st.sidebar.selectbox("Select a page",
                                ["Project Overview", "Main Tasks", "Methodology",
                                 "Data Preprocessing", "OCR Handwritten PDF", "Update Data Manually", "Transaction Analysis",
                                 "Visual Analysis", "Challenges", "Conclusion", "Project Impact & Application"])

    # Page content
    if page == "Project Overview":
        project_overview()
    elif page == "Main Tasks":
        tasks()
    elif page == "Methodology":
        methodology()
    elif page == "Data Preprocessing":
        data_preprocessing()
    elif page == "OCR Handwritten PDF":
        # pdf_ocr()
        ocr_result()
    elif page == "Update Data Manually":
        manual_update()
    elif page == "Transaction Analysis":
        transaction_analysis()
    elif page == "Visual Analysis":
        visualization()
    # elif page == "Geovisualization":
    #     geo_visualization()
    elif page == "Challenges":
        challenges()
    elif page == "Conclusion":
        conclusion()
    elif page == "Project Impact & Application":
        further_analysis()

def project_overview():
    st.header("Project Overview")
    ## 1. Introduction
    st.subheader("1. Introduction")
    st.markdown("""
    This capstone seeks to digitize the financial processes of the Women Affinity
    Groups (WAGs) under the Nigeria for Women Program Scale Up (NFWP-SU)
    project. By structuring digitized financial transaction data, this will improve the efficiency for WAGs to
    harness technology for savings, credit access, and overall economic empowerment
    in order to help low-income women.
    """)

    ## 2. Background and Context
    st.subheader("2. Background and Context")
    st.markdown("""
    WAGs have been pivotal in fostering women's financial and social capital in
    Nigeria. They provide a platform for savings, mutual lending, and skill
    development. Despite their success, these groups face challenges in manual
    financial transactions, which are time-consuming and prone to errors. The
    digitization of these groups promises to streamline operations and expand their
    impact.
    """)

    ## 3. Problem Description
    st.subheader("3. Problem Description")
    st.markdown("""
    The project addresses the need for an efficient, transparent, and scalable solution to
    manage the financial activities of WAGs. By digitizing financial process, the
    project aims to automate savings, loan repayments, and other financial
    transactions, thereby enhancing the operational efficiency and financial
    empowerment of the groups.
    """)

    ## 4. Objectives and Goals
    st.subheader("4. Objectives and Goals")
    st.markdown("""
    - Digitize unstructured raw data into analyzable data.
    - Develop a dashboard to visualize financial transactions for further insights.
    - Measure the impact of digitization on the efficiency of WAGs and the economic
      empowerment of its members.
    """)

def tasks():
    st.header("Main Tasks")

    tasks_info = """

    ### Data Preprocessing
    - **Description:** Extracting data from a hierarchical structure of 178 Word files distributed across multiple directories using `Docx` and `RegEx` for preprocessing.
    - **Objective:** Convert Word document data into a clean, structured format (CSV), ensuring data quality and consistency.
    - **Significance:** This step plays a critical role in preparing the dataset for analysis. By converting unstructured data into a structured format and applying preprocessing techniques, we ensure the dataset's readiness for analysis, enhancing its usability and reliability for analytical tasks.

    ### OCR Handwritten PDF
    - **Description:** Optical Character Recognition (OCR) is applied to extract text from handwritten PDF documents.
    - **Objectives:**
        - Implement basic OCR techniques for extracting text from images.
        - Utilize unstructured I/O for partitioning PDFs.
        - Use the `pdf2image` library combined with transformers for advanced OCR on PDFs.
    - **Significance:** OCR on handwritten PDFs helps convert non-digital information into a format suitable for analysis, contributing to a comprehensive dataset.

    ### Transaction NLP Data Analysis
    - **Description:** Natural Language Processing (NLP) techniques are applied to analyze transaction data.
    - **Objectives:**
        - Apply traditional methods like TF-IDF (Term Frequency-Inverse Document Frequency) and Naive Bayes (NB) for analysis.
        - Implement zero-shot classification using transformer models.
    - **Significance:** Extracting insights from transactional data involves advanced NLP techniques, providing a deeper understanding of the context and sentiment associated with transactions.
    """

    st.markdown(tasks_info)


def methodology():
    st.header("Methodology")

    methodology_info = """

    ### Python-docx
    - **Description:** The python-docx package is a Python library used for creating, reading, and modifying Microsoft Word (.docx) files. It provides a convenient API for interacting with Word documents programmatically.
    - **Components:**        
        - **Reading and Writing:** It reads existing Word documents and extracts text, tables, images, and other elements.
        - **Document Structure:** It provides classes and methods for navigating through the document structure and accessing different parts of the document
        - **Table Manipulation:** It allows you to work with tables, including creating new tables, adding rows and columns, and modifying cell content and formatting.
    - **Significance:** This method facilitates the extraction of tabular data from Word documents and prepares it for further analysis.

    ### Regular Expressions (RegEx)
    - **Description:** RegEx is a formal language for describing text patterns
    - **Components:** 
        - **Data extraction:** used it for precise extraction of desired text and information from Word files
        - **Changing date format:** used to modify the date formats present in the dataset.
    - **Significance:** RegEx provides a powerful tool for pattern-matching and manipulation, crucial for dat extraction and ensuring consistency in date representations.

    ### OCR Handwritten PDF
    - **Description:** OCR on handwritten PDFs involves several stages, including basic OCR, unstructured I/O for partitioning, and advanced OCR using `pdf2image` and transformers.
    - **Components:**
        - **Basic OCR:** Initial extraction of text from images.
        - **Unstructured I/O:** Partitioning PDFs into manageable sections.
        - **pdf2image + transformers:** Utilizing a combination of libraries for advanced OCR.
    - **Significance:** This multi-step approach ensures accurate extraction of text from handwritten PDFs, overcoming challenges associated with unstructured data.

    ### Transaction NLP Analysis
    - **Description:** Transactional data is subjected to NLP analysis using both traditional methods and transformer-based models.
    - **Components:**
        - **Traditional method:** TF-IDF and Naive Bayes for baseline analysis.
        - **Zero-shot classification:** Leveraging transformer models for advanced NLP analysis.
    - **Significance:** The combination of traditional and modern NLP techniques provides a comprehensive understanding of the textual information in transaction data.

    ### Data Analytics and Visualization + Web App
    - **Description:** Visualization tools like Matplotlib, Seaborn and Streamlit are employed for creating interactive data visualizations and web applications.
    - **Components:**
        - **Python(Matplotlib/Seaborn):** Used for creating visually appealing and informative dashboards.
        - **Hypothesis Testing:** Used independent sample t-test to determine whether there is a significant difference between the means of two independent groups
        - **Chi-squared Test:** Used test of independence to determine whether there is a significant association between two categorical variables
        - **Streamlit:** Utilized for building interactive web applications for data exploration.
    - **Significance:** Visualization enhances the interpretability of the data, while web apps provide an accessible interface for users to interact with the findings.
    """

    st.markdown(methodology_info)

# def pdf_ocr():
#     st.header("OCR Handwritten PDF")
#     data_folder = Path(os.getcwd()) / 'Data'
#     pdf_files = get_list_of_files(data_folder, '**/*.pdf', '.pdf')
#     # user_input = st.text_input("Enter text from PDF:")
#
#     for pdf_file in pdf_files:
#         st.write(f"Processing PDF: {pdf_file}")
#         images = pdf_to_images(pdf_file)
#
#         for idx, image in enumerate(images):
#             # Display each page of the PDF
#             st.image(image, caption=f"Page {idx + 1}", use_column_width=True)
#
#             # Perform OCR on the image
#             text = ocr_handwritten_text(image)
#             # user_input = st.text_area("Enter your handwritten text:", "")
#
#             # Display OCR results
#             st.write(f"Page {idx + 1} OCR Result:\n{text}\n")
#             # st.write(f"Page {idx + 1} User Input:\n{user_input}\n")

# def pdf_ocr():
#     st.header("OCR Handwritten PDF")
#     data_folder = Path(os.getcwd()) / 'Data'
#     pdf_files = get_list_of_files(data_folder, '**/*.pdf', '.pdf')
#     # user_input = st.text_input("Enter text from PDF:")
#
#     for pdf_file in pdf_files:
#         st.write(f"Processing PDF: {pdf_file}")
#         images = pdf_to_images(pdf_file)
#
#         for idx, image in enumerate(images):
#             # Display each page of the PDF
#             st.image(image, caption=f"Page {idx + 1}", use_column_width=True)
#
#             # Perform OCR on the image
#             text = ocr_handwritten_text(image)
#             # user_input = st.text_area("Enter your handwritten text:", "")
#
#             # Display OCR results
#             st.write(f"Page {idx + 1} OCR Result:\n{text}\n")
#             # st.write(f"Page {idx + 1} User Input:\n{user_input}\n")
#
#             # Define an empty DataFrame
#             df = pd.DataFrame(
#                 columns=['FD_Name', 'State', 'Region', 'Member_Status', 'File_Name', 'Respondent_ID', 'Date', 'Week',
#                          'Transaction_Nature', 'Transaction_Type', 'Transaction_Category', 'Category_Name',
#                          'Transaction_Name', 'Transaction_Amount', 'Transaction_Comment', 'Formatted_Date'])
#
#             # Define column configurations
#             config = {
#                 'FD_Name': st.column_config.TextColumn('FD Name'),
#                 'State': st.column_config.TextColumn('State'),
#                 'Region': st.column_config.TextColumn('Region'),
#                 'Member_Status': st.column_config.TextColumn('Member Status'),
#                 'File_Name': st.column_config.TextColumn('File Name'),
#                 'Respondent_ID': st.column_config.TextColumn('Respondent ID'),
#                 'Date': st.column_config.DateColumn('Date'),
#                 'Week': st.column_config.NumberColumn('Week'),
#                 'Transaction_Nature': st.column_config.TextColumn('Transaction Nature'),
#                 'Transaction_Type': st.column_config.TextColumn('Transaction Type'),
#                 'Transaction_Category': st.column_config.TextColumn('Transaction Category'),
#                 'Category_Name': st.column_config.TextColumn('Category Name'),
#                 'Transaction_Name': st.column_config.TextColumn('Transaction Name'),
#                 'Transaction_Amount': st.column_config.NumberColumn('Transaction Amount'),
#                 'Transaction_Comment': st.column_config.TextColumn('Transaction Comment'),
#                 'Formatted_Date': st.column_config.TextColumn('Formatted Date')
#             }
#
#             # Generate a unique key based on PDF file name and page index for the data editor
#             editor_key = f"{pdf_file}_{idx}_editor"
#             # Generate a unique key based on PDF file name and page index for the button
#             button_key = f"{pdf_file}_{idx}_button"
#
#             # Display the data editor and get user input
#             result = st.data_editor(df, column_config=config, num_rows='dynamic', key=editor_key)
#
#             # Button to get the results
#             if st.button('Get results', key=button_key):
#                 st.write(result)

import os
from pathlib import Path
import streamlit as st
import pandas as pd
import cv2
import numpy as np
import easyocr
from pdf2image import convert_from_path

def ocr_result():
    st.header("OCR Handwritten PDF")
    data_folder = Path(os.getcwd()) / 'Data'
    pdf_files = get_list_of_files(data_folder, '**/*.pdf', '.pdf')
    # user_input = st.text_input("Enter text from PDF:")


    for pdf_file in pdf_files:
        st.write(f"Processing PDF: {pdf_file}")
        pages = convert_from_path(pdf_file)
        reader = easyocr.Reader(['en'], gpu=True)

        # Loop through each page
        for idx, page in enumerate(pages):
            # Convert PIL image to OpenCV format
            image = cv2.cvtColor(np.array(page), cv2.COLOR_RGB2BGR)

            # Sharpen the image
            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            sharpen_kernel = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
            sharpen = cv2.filter2D(gray, -1, sharpen_kernel)

            # Thresholding
            thresh = cv2.threshold(sharpen, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

            # Perform OCR
            ocr_results = reader.readtext(thresh, detail=0)

            # Display OCR results
            st.image(image, caption=f"Page {idx + 1}", use_column_width=True)
            st.write(f"Page {idx + 1} OCR Result:\n{ocr_results}\n")

            # Define an empty DataFrame
            df = pd.DataFrame(
                columns=['FD_Name', 'State', 'Region', 'Member_Status', 'File_Name', 'Respondent_ID', 'Date', 'Week',
                         'Transaction_Nature', 'Transaction_Type', 'Transaction_Category', 'Category_Name',
                         'Transaction_Name', 'Transaction_Amount', 'Transaction_Comment', 'Formatted_Date'])

            # Define column configurations
            config = {
                'FD_Name': st.column_config.TextColumn('FD Name'),
                'State': st.column_config.TextColumn('State'),
                'Region': st.column_config.TextColumn('Region'),
                'Member_Status': st.column_config.TextColumn('Member Status'),
                'File_Name': st.column_config.TextColumn('File Name'),
                'Respondent_ID': st.column_config.TextColumn('Respondent ID'),
                'Date': st.column_config.DateColumn('Date'),
                'Week': st.column_config.NumberColumn('Week'),
                'Transaction_Nature': st.column_config.TextColumn('Transaction Nature'),
                'Transaction_Type': st.column_config.TextColumn('Transaction Type'),
                'Transaction_Category': st.column_config.TextColumn('Transaction Category'),
                'Category_Name': st.column_config.TextColumn('Category Name'),
                'Transaction_Name': st.column_config.TextColumn('Transaction Name'),
                'Transaction_Amount': st.column_config.NumberColumn('Transaction Amount'),
                'Transaction_Comment': st.column_config.TextColumn('Transaction Comment'),
                'Formatted_Date': st.column_config.TextColumn('Formatted Date')
            }

            # Generate a unique key based on PDF file name and page index for the data editor
            editor_key = f"{pdf_file}_{idx}_editor"
            # Generate a unique key based on PDF file name and page index for the button
            button_key = f"{pdf_file}_{idx}_button"

            # Display the data editor and get user input
            result = st.data_editor(df, column_config=config, num_rows='dynamic', key=editor_key)

            # Button to get the results
            if st.button('Get results', key=button_key):
                st.write(result)

def manual_update():
    st.header("Update Tabular Data Manually")

    def manual_update(old_data):
        # st.header("Update Tabular Data Manually")
        # Load old data
        if old_data is not None:
            df = pd.read_csv(old_data)
            unique_values = get_unique_values(df)

            # Create select boxes for input variables based on unique values
            st.subheader("Enter Variable Values:")
            fd_name = st.text_input("FD_Name:")
            state = st.selectbox("State:", unique_values['State'])
            region = st.selectbox("Region:", unique_values['Region'])
            member_status = st.selectbox("Member_Status:", unique_values['Member_Status'])
            file_name = st.text_input("File_Name:")
            respondent_id = st.text_input("Respondent ID:")
            date = st.text_input("Date(DD/MM/YYYY):")
            week = st.number_input("Week:", min_value = 1,max_value=5)
            transaction_nature = st.selectbox("Transaction_Nature:", unique_values['Transaction_Nature'])
            transaction_type = st.selectbox("Transaction_Type:", unique_values['Transaction_Type'])
            transaction_category = st.selectbox("Transaction_Category:", unique_values['Transaction_Category'])
            category_name = st.selectbox("Category_Name:", unique_values['Category_Name'])
            transaction_name = st.text_input("Transaction_Name:")
            transaction_amount = st.number_input("Transaction_Amount:")
            transaction_comment = st.text_input("Transaction_Comment:")
            formatted_date = clean_date_format(date)

            if st.button("Update Row"):
                # Call functions to update tabular data
                updated_row_data = [fd_name, state, region, member_status, file_name, respondent_id, date, week,
                                    transaction_nature, transaction_type, transaction_category, category_name,
                                    transaction_name, transaction_amount, transaction_comment,formatted_date]
                # Update tabular data with the new row data
                updated_data = update_tabular_data(df, updated_row_data)
                st.success("Row Updated Successfully!")
                st.dataframe(updated_data.tail())

                updated_data_csv = updated_data.to_csv(index=False, encoding='utf-8')
                # new_file_name = st.text_input("Type New File Name:")


                st.download_button(
                    label="Download data as CSV",
                    data=updated_data_csv,
                    file_name="Updated_data.csv",
                    mime='text/csv',
                )

    def update_tabular_data(old_data, updated_row_data):
        # if not old_data.endswith('.csv'):
        #     raise ValueError("The provided old_data is not a CSV file.")
        # old_data = pd.read_csv(old_data)
        new_row = pd.DataFrame([updated_row_data], columns=old_data.columns)
        updated_data = pd.concat([old_data, new_row], ignore_index=True)
        # updated_data = old_data.append(new_row, ignore_index=True)
        return updated_data



    # User input for the old data file
    old_data = st.file_uploader("Choose a CSV file to update")

    # Call the function to update tabular data manually
    if old_data is not None:
        manual_update(old_data)




def data_preprocessing():
    import streamlit as st
    import zipfile
    import os
    import shutil
    import plotly.express as px
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from wordcloud import WordCloud
    from plotly.subplots import make_subplots
    import matplotlib.pyplot as plt
    import seaborn as sns

    def extract_folder_name(zip_file):
        extract_path = os.getcwd()

        with zipfile.ZipFile(zip_file, 'r') as zip_ref:
            zip_ref.extractall(extract_path)

        macosx_folder = os.path.join(extract_path, "__MACOSX")
        if os.path.exists(macosx_folder):
            shutil.rmtree(macosx_folder)

    def data_extraction(folder):
        file_locations = get_file_locations(folder)
        csv_file_header = ['FD_Name', 'State', 'Region', 'Member_Status', 'File_Name', 'Respondent_ID', 'Date', 'Week', 'Transaction_Nature', 'Transaction_Type', 'Transaction_Name', 'Transaction_Amount', 'Transaction_Comment']

        combined_csv_data = []
        for docx_file in file_locations:
            # st.write(f'Processing file: {docx_file}')
            csv_data = convert_table_to_csv_file(docx_file, csv_file_header)
            combined_csv_data.extend(csv_data)

        combined_output_csv = 'combined_output.csv'
        with open(combined_output_csv, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(csv_file_header)  # Write the header
            writer.writerows(combined_csv_data)  # Write the data

        # Data cleaning
        os.getcwd()
        df = pd.read_csv('combined_output.csv')

        df['Formatted_Date'] = df['Date'].apply(clean_date_format)
        df['Transaction_Amount'] = df['Transaction_Amount'].apply(clean_transaction_amount)
        df['Member_Status'] = df['Member_Status'].apply(clean_mem_status)
        df['State'] = df['State'].str.lower()
        df['State'] = df['State'].replace({'abia baseline': 'abia'})
        df['Region'] = df['Region'].str.lower()
        df['Transaction_Name'] = df['Transaction_Name'].str.replace('₦', '')

        # Convert columns to appropriate data types
        df['FD_Name'] = df['FD_Name'].astype('category')
        df['Member_Status'] = df['Member_Status'].astype('category')
        df['Week'] = df['Week'].astype('category')
        df['Transaction_Nature'] = df['Transaction_Nature'].astype('category')
        df['Transaction_Type'] = df['Transaction_Type'].astype('category')
        df['Formatted_Date'] = pd.to_datetime(df['Formatted_Date'], format='%d/%m/%Y', errors='coerce')

        # Remove 'zero Transaction_Amount' and 'Date' column
        df = df[df['Transaction_Amount'] != 0]
        df.drop(columns=['Date'], inplace=True)

        df.to_csv('Financial_Diaries.csv', index=False)

        st.success('Data is cleaned and saved as \'Financial_Diaries.csv\'')

        # Display processed data
        if os.path.exists('Financial_Diaries_Modified.csv'):
            st.subheader("Processed Data")
            df = pd.read_csv('Financial_Diaries_Modified.csv')
            st.dataframe(df)

        # Dataset Information
        st.subheader("Data Structure")

        info_data = []
        for column in df.columns:
            data_type = df[column].dtype
            non_null_count = df[column].count()
            unique_values = df[column].unique()[:6]
            info_data.append({"Column Name": column,
                              "Data Type": data_type,
                              "Non-Null Count": non_null_count,
                              "Unique Values": ", ".join(map(str, unique_values))})
        info_df = pd.DataFrame(info_data)

        with st.expander("Expand to view"):
            st.write(f"Number of Transactions: {df.shape[0]}")
            st.write(f"Number of Variables: {df.shape[1]}")
            st.dataframe(info_df)

        # st.divider()

        st.subheader("Overview")
        df['Formatted_Date'] = pd.to_datetime(df['Formatted_Date'])
        df['Year'] = df['Formatted_Date'].dt.year

        count_r = df['Respondent ID'].nunique()
        count_wag = df[df["Member_Status"] == "WAG"]['Respondent ID'].nunique()
        count_nwag = df[df["Member_Status"] == "NON WAG"]['Respondent ID'].nunique()
        total_income = df[df["Transaction_Type"] == "Income"]
        income_per = (total_income["Transaction_Amount"].sum()/df["Transaction_Amount"].sum())*100
        total_expence = df[df["Transaction_Type"] == "Expenditure"]
        expence_per = (total_expence["Transaction_Amount"].sum()/df["Transaction_Amount"].sum())*100
        total_fixed = df[df["Transaction_Nature"] == "Fixed"]
        fixed_per = (total_fixed["Transaction_Amount"].sum()/df["Transaction_Amount"].sum())*100
        total_var = df[df["Transaction_Nature"] == "Variable"]
        var_per = (total_var["Transaction_Amount"].sum()/df["Transaction_Amount"].sum())*100

        st.markdown(f"""
        <div style='background-color: #CCE5FF; padding: 10px; border-radius: 10px;'>
            <div style='text-align: center; display: flex; font-size: 18px;'>
                <div>
                    <div style='display: flex; align-items: center;'>
                        <div style='margin: 15px;'>
                            <p style='margin-bottom: 10px; font-weight: bold; font-size: 20px;'>Respondent</p>
                            <div style='display: flex; justify-content: space-between; width: 500px; height:100px; background-color: white; padding: 20px; border-radius: 10px;'>
                                <div style='margin: 0 5% 0 10%;'>Total<br>{count_r}</div>
                                <div style='margin: 0 5% 0 5%;'>WAG<br>{count_wag}</div>
                                <div style='margin: 0 10% 0 5%;'>NWAG<br>{count_nwag}</div>
                            </div>
                        </div>
                        <div style='margin: 15px;'>
                            <p style='margin-bottom: 10px;font-weight: bold; font-size: 20px;'>Transaction Type</p>
                            <div style='display: flex; justify-content: space-between; width: 340px; height:100px; background-color: white; padding: 20px; border-radius: 10px;'>
                                <div style='margin: 0 3% 0 10%;'>Income<br>{income_per.round(1)}%</div>
                                <div style='margin: 0 8% 0 3%;'>Expenditure<br>{expence_per.round(1)}%</div>
                            </div>
                        </div>
                        <div style='margin: 10px;'>
                            <p style='margin-bottom: 10px;font-weight: bold; font-size: 20px;'>Transaction Nature</p>
                            <div style='display: flex; justify-content: space-between; width: 340px; height:100px; background-color: white; padding: 20px; border-radius: 10px;'>
                                <div style='margin: 0 3% 0 10%;'>Fixed<br>{fixed_per.round(1)}%</div>
                                <div style='margin: 0 8% 0 3%;'>Variable<br>{var_per.round(1)}%</div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

        # main_state()
        # plots('State')
        #
        # st.divider()
        #
        # main_region()
        # plots('Region')

        # Plot 1
        wag_transaction_amount_log = np.log(df[df['Member_Status'] == 'WAG']['Transaction_Amount'])
        non_wag_transaction_amount_log = np.log(df[df['Member_Status'] == 'NON WAG']['Transaction_Amount'])

        # Create histogram traces
        trace1 = go.Histogram(x=wag_transaction_amount_log, marker=dict(color='navy'), name='WAG')
        trace2 = go.Histogram(x=non_wag_transaction_amount_log, opacity=0.7, marker=dict(color='skyblue'), name='NON WAG')

        layout = go.Layout(
            title='Distribution of Transaction Amount (log)',
            xaxis=dict(title='Transaction Amount (log)'),
            yaxis=dict(title='Frequency'),
            barmode='overlay',
        )
        fig1 = go.Figure(data=[trace1, trace2], layout=layout)
        fig1.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        # Plot 2
        fig2 = px.bar(df, x='Transaction_Type', y='Transaction_Amount', color='Transaction_Nature',
                      title='Transaction Amount by Type and Nature')
        fig2.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))

        # Plot 3
        fig3 = px.bar(df, x='Week', y='Transaction_Amount', color='Transaction_Type',
                      title='Transaction Amount by Week')
        fig3.update_layout(legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ))
        # Plot 4
        fig4 = make_subplots(rows=1, cols=2, shared_yaxes=True)
        fig4.add_trace(
            go.Bar(x=total_income['Year'], y=total_income['Transaction_Amount']),
            row=1, col=1
        )

        fig4.add_trace(
            go.Bar(x=total_expence['Year'], y=total_expence['Transaction_Amount']),
            row=1, col=2
        )

        fig4.update_traces(showlegend=False)

        # Add subtitles
        fig4.update_layout(
            title_text="Transaction Amount by Year",
            annotations=[
                dict(
                    text="Income", x=0.220, y=-0.15, showarrow=False, xref="paper", yref="paper", font=dict(size=14)
                ),
                dict(
                    text="Expense", x=0.780, y=-0.15, showarrow=False, xref="paper", yref="paper", font=dict(size=14)
                )
            ]
        )
        fig4.update_layout(height=450, width=800, title_text="Transaction Amount by Year")

        # Plot 5
        custom_stopwords = ["the", "and", "to", "of", "in", "for", "on", "with", "by", "from", "at", "is", "are", "was",
                            "were", "it", "that", "this", "an", "as", "or", "be", "have", "has", "not", "no", "can",
                            "could", "but", "so", "if", "when", "where", "how", "why", "which", "cost", "income",
                            "weekly"]

        # Preprocess transaction names
        transaction_names = df['Transaction_Name'].str.lower().str.split()
        transaction_names = [[word for word in words if word not in custom_stopwords] for words in transaction_names]
        transaction_names_str = ' '.join([' '.join(words) for words in transaction_names])

        # Generate Word Cloud
        wordcloud = WordCloud(background_color='white', colormap='Blues_r', height=600, width=1850,
                              min_font_size=10).generate(transaction_names_str)

        # Convert Word Cloud to Plotly image
        img_rgb = wordcloud.to_array()
        fig5 = go.Figure(data=go.Image(z=img_rgb))
        fig5.update_layout(title='Word Cloud for Transaction Name',
                           xaxis_visible=False,
                           yaxis_visible=False)


        # Plot 7
        fig7 = px.bar(df, x='Week', y='Transaction_Amount', color='Transaction_Category1', barmode='group',
                      title='Transaction Category by Week')

        col2, col3, col4 = st.columns(3)
        col1, col5 = st.columns([1, 2])

        with col1:
            st.plotly_chart(fig1, use_container_width=True)

        with col2:
            st.plotly_chart(fig2, use_container_width=True)

        with col3:
            st.plotly_chart(fig3, use_container_width=True)

        with col4:
            st.plotly_chart(fig4, use_container_width=True)

        with col5:
            st.plotly_chart(fig5, use_container_width=True)

        st.plotly_chart(fig7, use_container_width=True)

    st.subheader("Data Preprocessing")
    folder_upload = st.file_uploader("Upload a zip file", type=["zip"])
    if folder_upload is not None:
        if folder_upload.type == 'application/zip':
            extract_folder_name(folder_upload)
            folder = folder_upload.name[:-4]
            data_extraction(folder)
        else:
            st.error("Please upload a zip file.")





def transaction_analysis():
    st.header("Transaction NLP Analysis")

    st.markdown("""
    ### Classification of Transactions into Categories
    We categorized transactions into 11 distinct categories for precise analysis:

    - **0- Business and Trade:** Non-agricultural income/expenditure.
    - **1- Agriculture:** Agriculture-related transactions.
    - **2- Travel and Transport:** Includes fuel/gas.
    - **3- Gifts:** Financial gifts from relatives or friends.
    - **4- Household:** Related to household items, like firewood, repairs, etc.
    - **5- Consumables:** Food, water, etc.
    - **6- Financial Management:** Loan repayment, interest, etc.
    - **7- Health Care:** Hospital and healthcare finances.
    - **8- WAG:** Transactions related to WAG savings.
    - **9- Personal:** Purchases like hair braiding, clothes, shoes, etc.
    - **10- Miscellaneous:** Other transactions, like church offerings, Christmas expenses, etc.

    **Initial Approach for Categorization**
    Initial attempts using LDA and clustering failed due to the sentence-like structure of transactions.

    ### Using TF-IDF + NB Classification
    **Data Preparation**
    To create a balanced training dataset, we manually handpicked 10 rows from each category.

    **Model Training and Application**
    We developed a text processing pipeline incorporating TF-IDF Vectorization and Multinomial Naive Bayes. This approach was applied to the curated dataset, yielding precise classification.

    **Outcome**
    This method achieved higher accuracy than previous attempts, successfully labeling all transactions into appropriate categories.

    ### Exploring Advanced Methods
    Subsequently, we experimented with a pre-trained model for zero-shot classification using Hugging Face's `facebook/bart-large-mnli`.

    **Outcome**
    This method also showed similar results in the classification process. 

    ### Comparing Methods
    We are currently comparing the results of the TF-IDF Vectorization with Naive Bayes approach and the zero-shot classification method to determine the best fit for our project needs.
    """)


def visualization():
    import streamlit as st
    import zipfile
    import os
    import shutil
    import plotly.express as px
    import numpy as np
    import pandas as pd
    import plotly.graph_objects as go
    from wordcloud import WordCloud
    from plotly.subplots import make_subplots

    st.header("Dataset Information")
    # st.subheader("Tableau Dashboard")
    # tableau_url = "https://your-tableau-dashboard-url"
    # components.iframe(tableau_url, height=800, scrolling=True)

    # Load the dataset
    df = pd.read_csv("Financial_Diaries.csv", na_values={'transaction_comment': ''},
                     usecols=lambda column: column != 'Date', keep_default_na=False)
    df = df[df['Transaction_Amount'] != 0]

    # Convert columns to appropriate data types
    df['FD_Name'] = df['FD_Name'].astype('category')
    df['Member_Status'] = df['Member_Status'].astype('category')
    df['Week'] = df['Week'].astype('category')
    df['Transaction_Nature'] = df['Transaction_Nature'].astype('category')
    df['Transaction_Type'] = df['Transaction_Type'].astype('category')
    df['Formatted_Date'] = pd.to_datetime(df['Formatted_Date'], format='%d/%m/%Y', errors='coerce')
    df['Formatted_Date'] = df['Formatted_Date'].dt.date

    # Dataset Information
    # st.subheader("Dataset Information")
    st.write(f"Number of Rows: {df.shape[0]}")
    st.write(f"Number of Columns: {df.shape[1]}")

    st.subheader("Data Structure")
    info_data = []
    for column in df.columns:
        data_type = df[column].dtype
        non_null_count = df[column].count()
        unique_values = df[column].unique()[:6]
        info_data.append({"Column Name": column,
                          "Data Type": data_type,
                          "Non-Null Count": non_null_count,
                          "Unique Values": ", ".join(map(str, unique_values))})
    info_df = pd.DataFrame(info_data)
    st.write(info_df)

    st.divider()


    # Plot

    # Plot histogram and density plot
    # Assuming 'st' is imported from Streamlit
    st.header('Data Analytics and Visualization')
    option = st.sidebar.selectbox(
        'Income or Expenditure',
        ('All', 'Income', 'Expenditure'))

    if option == 'All':
        df_filtered = df
    elif option == 'Income':
        df_filtered = df[df['Transaction_Type'] == 'Income']
    else:
        df_filtered = df[df['Transaction_Type'] == 'Expenditure']

    # Plot histogram and density plot
    mean_val = df_filtered["Transaction_Amount"].mean()
    median_val = df_filtered["Transaction_Amount"].median()
    # mode_val = stats.mode(df_filtered["Transaction_Amount"]).mode[0]
    # mode_val = stats.mode(df_filtered["Transaction_Amount"])[0][0]
    mode_val = stats.mode(df_filtered["Transaction_Amount"]).mode.item()

    plt.figure(figsize=(10, 6))
    sns.histplot(df_filtered["Transaction_Amount"], kde=True, color='skyblue')
    plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=1, label='Mean: {:.2f}'.format(mean_val))
    plt.axvline(median_val, color='green', linestyle='dashed', linewidth=1, label='Median: {:.2f}'.format(median_val))
    plt.axvline(mode_val, color='orange', linestyle='dashed', linewidth=1, label='Mode: {:.2f}'.format(mode_val))
    plt.title('Histogram and Density Plot of {}'.format("Transaction_Amount"))
    plt.xlabel('Transaction Amount')
    plt.ylabel('Frequency / Density')
    plt.legend()
    combined_fig = plt.gcf()
    st.pyplot(combined_fig)

    st.write(
        "Due to the right-skewed nature of the Transaction_Amount data, we employ log transformation to achieve a more symmetrical distribution. This transformation mitigates the impact of large values on the distribution, compresses the range of values, and stabilizes variance. Additionally, it promotes linearity in the relationship between variables, a desirable trait in statistical modeling and analysis.")

    df_filtered['Transaction_Amount_log'] = np.log(df_filtered['Transaction_Amount'])

    # Plot histogram and density plot after log
    mean_val = df_filtered["Transaction_Amount_log"].mean()
    median_val = df_filtered["Transaction_Amount_log"].median()
    mode_val = stats.mode(df_filtered["Transaction_Amount_log"]).mode.item()

    plt.figure(figsize=(10, 6))
    sns.histplot(df_filtered["Transaction_Amount_log"], kde=True, color='skyblue')
    plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=1, label='Mean: {:.2f}'.format(mean_val))
    plt.axvline(median_val, color='green', linestyle='dashed', linewidth=1, label='Median: {:.2f}'.format(median_val))
    plt.axvline(mode_val, color='orange', linestyle='dashed', linewidth=1, label='Mode: {:.2f}'.format(mode_val))
    plt.title('Histogram and Density Plot of {}'.format("log(Transaction Amount)"))
    plt.xlabel('log(Transaction Amount)')
    plt.ylabel('Frequency / Density')
    plt.legend()
    combined_fig = plt.gcf()
    st.pyplot(combined_fig)

    # Word Cloud
    st.subheader("Word Cloud for Transaction Name")
    custom_stopwords = ["the", "and", "to", "of", "in", "for", "on", "with", "by", "from", "at", "is", "are", "was",
                        "were", "it", "that", "this", "an", "as", "or", "be", "have", "has", "not", "no", "can",
                        "could", "but", "so", "if", "when", "where", "how", "why", "which", "cost", "income", "weekly"]

    transaction_names = df_filtered['Transaction_Name'].str.lower().str.split()
    transaction_names = [[word for word in words if word not in custom_stopwords] for words in transaction_names]
    transaction_names_str = ' '.join([' '.join(words) for words in transaction_names])

    wordcloud = WordCloud(width=800, height=800,
                          background_color='white',
                          min_font_size=10).generate(transaction_names_str)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.legend('')
    st.pyplot(use_container_width=True)


    # Categories
    unique_categories = df_filtered['Category_Name'].unique()

    # Define a dictionary to map each category to a color from the "Set2" palette
    category_colors = dict(zip(unique_categories, sns.color_palette("Set3", len(unique_categories))))

    # Distribution of Transaction Categories
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Category_Name', data=df_filtered, palette=category_colors)
    plt.xticks(rotation=45)
    plt.title('Distribution of Transaction Categories')
    plt.tight_layout()
    st.pyplot()

    # Stacked Bar Chart
    grouped_data = df_filtered.groupby(['Week', 'Category_Name'])['Transaction_Amount'].sum().reset_index()
    pivot_table = grouped_data.pivot(index='Week', columns='Category_Name', values='Transaction_Amount').fillna(0)

    # Stacked Bar Chart
    fig, ax = plt.subplots(figsize=(14, 7))
    pivot_table.plot(kind='bar', stacked=True, ax=ax,
                     color=[category_colors.get(x) for x in pivot_table.columns])
    ax.set_title('Weekly Transaction Amounts by Category')
    ax.set_xlabel('Week Number')
    ax.set_ylabel('Total Transaction Amount')
    ax.legend(title='Category Name')
    plt.tight_layout()
    st.pyplot()

    # Split violin plot
    st.subheader("Distribution of log(Transaction Amount) by Member Status")
    plt.figure(figsize=(10, 6))
    palette_colors = {'NON WAG': 'lightblue', 'WAG': 'lightpink'}
    sns.violinplot(x='Transaction_Nature', y='Transaction_Amount_log', hue='Member_Status', data=df_filtered,
                   split=True,
                   palette=palette_colors, inner="quart")

    plt.xlabel('Transaction_Nature', fontweight='bold')
    plt.ylabel('Transaction Amount (log)', fontweight='bold')
    plt.title('Split Violin Plot of log(Transaction Amount) by Transaction Nature and Member Status')

    plt.xticks(rotation=45)
    plt.legend(title='Member Status', loc='lower left')
    st.pyplot()


    # Pivot
    st.subheader("Average Transaction Amount by Member Status")
    pivot_df = df_filtered.pivot_table(index='Transaction_Nature', columns='Member_Status', values='Transaction_Amount', aggfunc='mean')

    plt.figure(figsize=(12, 8))
    sns.heatmap(pivot_df, cmap='Blues', annot=True, fmt=".1f", linewidths=.5)
    plt.title('Average Transaction Amount by Transaction Nature and Member Status')
    plt.xlabel('Member Status', fontweight='bold')
    plt.ylabel('Transaction Nature', fontweight='bold')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Display the plot in Streamlit
    st.pyplot()


    # Mirror chart
    st.subheader("Average Transaction Amounts between 2023 and 2021")
    df_filtered['Formatted_Date'] = pd.to_datetime(df_filtered['Formatted_Date'])

    df_wag = df_filtered[df_filtered['Member_Status'] == 'WAG']
    df_nwag = df_filtered[df_filtered['Member_Status'] == 'NON WAG']

    df_2021_n = df_nwag[df_nwag['Formatted_Date'].dt.year == 2021].groupby('Transaction_Nature')['Transaction_Amount'].mean().reset_index()
    df_2021_w = df_wag[df_wag['Formatted_Date'].dt.year == 2021].groupby('Transaction_Nature')['Transaction_Amount'].mean().reset_index()
    df_2023_n = df_nwag[df_nwag['Formatted_Date'].dt.year == 2023].groupby('Transaction_Nature')['Transaction_Amount'].mean().reset_index()
    df_2023_w = df_wag[df_wag['Formatted_Date'].dt.year == 2023].groupby('Transaction_Nature')['Transaction_Amount'].mean().reset_index()

    fig, ax = plt.subplots(figsize=(10, 6))

    bar_width = 0.35
    bar_positions_2021_n = range(len(df_2021_n))
    bar_positions_2021_w = [pos + bar_width for pos in bar_positions_2021_n]
    bar_positions_2023_n = range(len(df_2023_n))
    bar_positions_2023_w = [pos + bar_width for pos in bar_positions_2023_n]

    bars_2021_n = ax.barh(bar_positions_2021_n, -df_2021_n['Transaction_Amount'], bar_width, color='steelblue',
                          label='2021 NON WAG')
    bars_2021_w = ax.barh(bar_positions_2021_w, -df_2021_w['Transaction_Amount'], bar_width, color='lightcoral',
                          label='2021 WAG')
    bars_2023_n = ax.barh(bar_positions_2023_n, df_2023_n['Transaction_Amount'], bar_width, color='lightblue',
                          label='2023 NON WAG')
    bars_2023_w = ax.barh(bar_positions_2023_w, df_2023_w['Transaction_Amount'], bar_width, color='lightpink',
                          label='2023 WAG')

    ax.set_yticks([pos + bar_width / 2 for pos in bar_positions_2021_n])
    ax.set_yticklabels(df_2021_n['Transaction_Nature'])

    ax.set_xlabel('Average Transaction Amount', fontweight='bold')
    ax.set_ylabel('Transaction Nature', fontweight='bold')
    ax.set_title('Mirror Chart of Average Transaction Amounts by Transaction Nature and Member Status')

    for bars in [bars_2021_n, bars_2021_w, bars_2023_n, bars_2023_w]:
        for bar in bars:
            value = bar.get_width()
            ha = 'right' if value < 0 else 'left'
            ax.text(value, bar.get_y() + bar.get_height() / 2,
                    f'{abs(value):.2f}', ha=ha, va='center', color='black', fontsize=9)

    ax.set_xticklabels([f'{abs(x)}' for x in ax.get_xticks()])
    ax.legend(loc='center right')
    plt.tight_layout()
    st.pyplot(fig)

    st.divider()


    # Hypothesis test
    st.header("Hypothesis Test")
    st.write('Hypothesis testing is a statistical method used to determine whether a hypothesis is statistically significant.'
             ' We used an independent sample t-test to compare the means of two groups (WAG and NON WAG) and determine if there is a significant difference.')

    # All Transaction amount
    wag_transaction_amount_log = np.log(df_filtered[df_filtered['Member_Status'] == 'WAG']['Transaction_Amount'])
    non_wag_transaction_amount_log = np.log(df_filtered[df_filtered['Member_Status'] == 'NON WAG']['Transaction_Amount'])

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.hist(wag_transaction_amount_log, bins=20, alpha=0.5, color='red', label='WAG')
    ax.hist(non_wag_transaction_amount_log, bins=20, alpha=0.5, color='blue', label='NON WAG')
    ax.set_xlabel('Transaction Amount (log)')
    ax.set_ylabel('Frequency')
    ax.set_title('Distribution of Transaction Amount (log)')
    ax.legend()
    st.pyplot(fig)


    st.markdown("- If there is a significant difference in :blue[**the mean transaction amount**] between WAG and NON WAG?")

    t_stat, p_value = stats.ttest_ind(wag_transaction_amount_log, non_wag_transaction_amount_log)

    alpha = 0.05
    if p_value < alpha:
        st.write("**Reject the null hypothesis**, there is a significant difference in the mean transaction amount between the two groups.")
    else:
        st.write("**Fail to reject the null hypothesis**, there is no significant difference in the mean transaction amount between the two groups.")
    st.divider()

    # Chi-square test
    st.header("Chi-square Test")
    st.write("Test of Independence is used in this analysis to determine whether there is a significant association between two categorical variables")
    from scipy.stats import chi2_contingency
    st.markdown("- If there is a significant relationship between :blue[**Member Status and Transaction Type**]?")

    contingency_table = pd.crosstab(df_filtered['Member_Status'], df_filtered['Transaction_Type'])
    chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)

    alpha = 0.05
    if p_val < alpha:
        st.write("**Reject the null hypothesis**, there is a significant relationship between Member Status(NON WAG, WAG) and Transaction Type(Income, Expenditure).")
    else:
        st.write("**Fail to reject the null hypothesis**, there is no significant relationship between Member Status(NON WAG, WAG) and Transaction Type(Income, Expenditure).")


    st.markdown("- If there is a significant relationship between :blue[**Member Status and Transaction Nature**]?")

    contingency_table = pd.crosstab(df_filtered['Member_Status'], df_filtered['Transaction_Nature'])
    chi2_stat, p_val, dof, expected = chi2_contingency(contingency_table)

    alpha = 0.05
    if p_val < alpha:
        st.write("**Reject the null hypothesis**, there is a significant relationship between Member Status(NON WAG, WAG) and Transaction Nature(Fixed, Variable).")
    else:
        st.write("**Fail to reject the null hypothesis**, there is no significant relationship between Member Status(NON WAG, WAG) and Transaction Nature(Fixed, Variable).")
# def geo_visualization():
#     main_state()
#     plots('State')
#
#     st.divider()
#
#     main_region()
#     plots('Region')

def challenges():
    st.header("Challenge")

    challenge_info = """

    ### Unstructured Data
    - **Description:** The project deals with unstructured data in the form of MS Word docx files and handwritten PDF files.
    - **Challenges:**
        - **MS Word docx files:** Extraction of relevant information from unstructured Word documents.
        - **Handwritten PDF files:** OCR and extraction of text from handwritten PDFs.
    - **Significance:** Overcoming challenges related to unstructured data is crucial for obtaining valuable insights and ensuring data accuracy.

    ### Analysis & Deriving Insights
    - **Description:** The challenge involves the analysis of data and deriving meaningful insights from the processed information.
    - **Significance:** Analyzing the data and extracting insights contribute to the project's goals, providing valuable information for decision-making.

    """

    st.markdown(challenge_info)

def conclusion():
    st.header("Conclusion")
    # Add content for Conclusion page
    st.markdown("""
    ### Data Analytics and Visualization
    - The most occurred transaction names are "gift", "business", and "sale"
    - Distribution of log(Transaction Amount) by Member Status is similar
    - WAG members' average transaction amount was higher than Non WAG members'
    - Average transaction amount in 2023 was higher than average transaction amount in 2021
    - There is no significant difference in the mean transaction amount between WAG and NON WAG
    - There is no significant relationship between Member Status(NON WAG, WAG) and Transaction Type(Income, Expenditure)
    - There is no significant relationship between Member Status(NON WAG, WAG) and Transaction Nature(Fixed, Variable)
    """)

def further_analysis():
    st.header("Project Impact & Application")
    markdown_text = """

### Automation on Data Preprocessing
- We successfully completed the **automation of data preprocessing** for MS Word Docx files, converting them into newly structured CSV files.
- Through automated data cleaning and NLP text classification, the CSV files became more **analyzable and structured** for further analysis.
- 🔄 This part is :green[**reusable**] with any new MS Word Docx files if they are written in the same template. Once new Docx files are added, the data preprocessing part will automatically update the CSV files.

### Data Visualization & Hypothesis Testing
- With the structured CSV files, we performed data visualization and conducted statistical hypothesis testing.
- Visualizations provided valuable insights into patterns and trends within the transaction data, such as the distribution of transaction amounts, popular categories, and differences between WAG and non-WAG members.
- Hypothesis tests allowed us to statistically examine potential relationships, such as whether there were significant differences in mean transaction amounts between the two member groups.
- 💡 Overall, **restructuring the raw data** enabled comprehensive analysis through visualizations and statistical methods, unlocking **deeper insights**.
"""
    st.markdown(markdown_text)

if __name__ == "__main__":
    main()