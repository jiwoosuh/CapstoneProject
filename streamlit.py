import streamlit as st
import os
import csv
import pandas as pd
from streamlit.components.v1 import components
from source_code.word2csv import get_file_locations, extract_info_from_docx, convert_table_to_csv_file
from source_code.data_cleaning import clean_date_format, fix_year_format, clean_mem_status, clean_transaction_amount

def main():
    st.title("Project Presentation")

    # Sidebar navigation
    page = st.sidebar.selectbox("Select a page", ["Project Overview", "Data Preprocessing", "Analysis", "Conclusion"])

    # Page content
    if page == "Project Overview":
        project_overview()
    elif page == "Data Preprocessing":
        data_preprocessing()
    elif page == "Analysis":
        analysis()
    elif page == "Conclusion":
        conclusion()

def project_overview():
    st.header("Project Overview")
    # Add content for Project Overview page

def data_preprocessing():
    st.header("Data Preprocessing")

    # Data extraction
    folder = 'Data'

    file_locations = get_file_locations(folder)
    csv_file_header = ['FD_Name', 'State', 'Region', 'Member_Status', 'File_Name', 'Respondent ID', 'Date', 'Week', 'Transaction_Nature', 'Transaction_Type', 'Transaction_Name', 'Transaction_Amount', 'Transaction_Comment']

    combined_csv_data = []
    for docx_file in file_locations:
        st.write(f'Processing file: {docx_file}')
        csv_data = convert_table_to_csv_file(docx_file, csv_file_header)
        combined_csv_data.extend(csv_data)

    combined_output_csv = 'combined_output.csv'
    with open(combined_output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(csv_file_header)  # Write the header
        writer.writerows(combined_csv_data)  # Write the data

    st.write(f'Combined data saved to {combined_output_csv}')

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

    df.to_csv('Financial_Diaries.csv', index=False)
    st.success('Data cleaning complete. Financial_Diaries.csv saved.')
    # Display processed data
    if os.path.exists('Financial_Diaries.csv'):
        st.subheader("Processed Data")
        df = pd.read_csv('Financial_Diaries.csv')
        st.dataframe(df)




def analysis():
    st.header("Analysis")
    st.subheader("Tableau Dashboard")
    tableau_url = "https://your-tableau-dashboard-url"
    components.iframe(tableau_url, height=800, scrolling=True)

def conclusion():
    st.header("Conclusion")
    # Add content for Conclusion page

if __name__ == "__main__":
    main()