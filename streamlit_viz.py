import streamlit as st
import os
import csv
import pandas as pd
from pathlib import Path
from streamlit.components.v1 import components
from source_code.word2csv import get_file_locations, extract_info_from_docx, convert_table_to_csv_file
from source_code.data_cleaning import clean_date_format, fix_year_format, clean_mem_status, clean_transaction_amount
# from source_code.pdf2csv import pdf_to_images,ocr_handwritten_text, get_list_of_files
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.title("🇳🇬 Nigeria For Women Program Scale-up Project")
    st.subheader("GWU Data Science Capstone Project - 2024 Spring")
    st.write("With World Bank 🌐 Social Sustainability and Inclusion")
    st.write("👩‍💻👩‍💻👩‍💻: Brooklyn Chen, Jiwoo Suh, Sanjana Godolkar")
    st.write("Instructor: Abdi Awl")
    st.write("[Trello Board](https://trello.com/b/ytzd5Ve7/dats6501-brooklyn-chen-sanjana-godolkar)")

    # Sidebar navigation
    page = st.sidebar.selectbox("Select a page",
                                ["Project Overview", "Main Tasks", "Methodology",
                                 "Data Preprocessing", "OCR Handwritten PDF", "Transaction Analysis",
                                 "Visual Analysis", "Challenges","Conclusion", "Further Tasks"])

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
        pdf_ocr()
    elif page == "Transaction Analysis":
        transaction_analysis()
    elif page == "Visual Analysis":
        visualization()
    elif page == "Challenges":
        challenges()
    elif page == "Conclusion":
        conclusion()
    elif page == "Further Tasks":
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

    ### Data Preprocessing - Docx2CSV, RegEx
    - **Description:** This task involves preparing the raw data for analysis. Two methods are employed - using the `Docx2CSV` utility and employing Regular Expressions (RegEx).
    - **Objective:** To convert data from Word documents (docx) into a more structured format (CSV) using `Docx2CSV` and perform additional preprocessing using RegEx for tasks like changing date formats.
    - **Significance:** This step is crucial for transforming unstructured data into a format suitable for analysis, ensuring uniformity and cleanliness in the dataset.

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

    ### Data Preprocessing - Docx2CSV
    - **Description:** The `Docx2CSV` custome function is utilized for converting Word documents to CSV format.
    - **Components:**
        - **Docx package:** Utilized for reading and extracting text and table data from Word documents.
    - **Significance:** This method facilitates the extraction of tabular data from Word documents and prepares it for further analysis.

    ### Data Preprocessing - RegEx
    - **Description:** Regular Expressions are employed to manipulate and clean data, specifically for changing date formats.
    - **Components:**
        - **Changing date format:** RegEx is used to modify the date formats present in the dataset.
    - **Significance:** RegEx provides a powerful tool for pattern-matching and manipulation, crucial for ensuring consistency in date representations.

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

def pdf_ocr():
    st.header("OCR Handwritten PDF")
    data_folder = Path(os.getcwd()) / 'Data'
    pdf_files = get_list_of_files(data_folder, '**/*.pdf', '.pdf')

    for pdf_file in pdf_files:
        st.write(f"Processing PDF: {pdf_file}")
        images = pdf_to_images(pdf_file)

        for idx, image in enumerate(images):
            # Display each page of the PDF
            st.image(image, caption=f"Page {idx + 1}", use_column_width=True)

            # Perform OCR on the image
            text = ocr_handwritten_text(image)

            # Display OCR results
            st.write(f"Page {idx + 1} OCR Result:\n{text}\n")


def data_preprocessing():
    st.header("Data Preprocessing")

    # Data extraction
    folder = 'Data'

    file_locations = get_file_locations(folder)
    csv_file_header = ['FD_Name', 'State', 'Region', 'Member_Status', 'File_Name', 'Respondent ID', 'Date', 'Week', 'Transaction_Nature', 'Transaction_Type', 'Transaction_Name', 'Transaction_Amount', 'Transaction_Comment']

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

    # Remove the 'Date' column
    df.drop(columns=['Date'], inplace=True)

    df.to_csv('Financial_Diaries.csv', index=False)
    st.success('Data cleaning is completed. Financial_Diaries.csv saved.')
    # Display processed data
    if os.path.exists('Financial_Diaries.csv'):
        st.subheader("Processed Data")
        df = pd.read_csv('Financial_Diaries.csv')
        st.dataframe(df)


def transaction_analysis():
    st.header("Transactions NLP Analysis")

def visualization():
    import streamlit as st
    import numpy as np
    import pandas as pd
    from wordcloud import WordCloud
    import matplotlib.pyplot as plt
    import seaborn as sns
    from scipy import stats
    from scipy.stats import shapiro, probplot

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

    # # Display first 6 unique values for each column
    # st.subheader("Data Structure")
    # info_df = pd.DataFrame(columns=["Column Name", "Data Type", "Non-Null Count", "Unique Values"])
    # for column in df.columns:
    #     info_series = df[column].describe()
    #     data_type = df[column].dtype
    #     unique_values = df[column].unique()[:6]
    #     info_df = info_df.append({"Column Name": column,
    #                               "Data Type": data_type,
    #                               "Non-Null Count": info_series["count"],
    #                               "Unique Values": ", ".join(map(str, unique_values))},
    #                              ignore_index=True)
    # st.write(info_df)
    #
    # st.divider()
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

    # # append wasn't working for me(Jiwoo)
    # st.subheader("Data Structure")
    # info_data = {"Column Name": [], "Data Type": [], "Non-Null Count": [], "Unique Values": []}
    #
    # for column in df.columns:
    #     info_series = df[column].describe()
    #     data_type = df[column].dtype
    #     unique_values = df[column].unique()[:5]
    #
    #     info_data["Column Name"].append(column)
    #     info_data["Data Type"].append(data_type)
    #     info_data["Non-Null Count"].append(info_series["count"])
    #     info_data["Unique Values"].append(", ".join(map(str, unique_values)))
    #
    # info_df = pd.concat([pd.DataFrame(info_data)], ignore_index=True)
    # st.write(info_df)

    st.divider()


    # Plot
    st.header('Data Analytics and Visualization')
    option = st.sidebar.selectbox(
        'Income or Expenditure',
        ('All', 'Income', 'Expenditure'))
    if option == 'All':
        df_filtered = df
    elif option == 'Income':
        df_filtered = df[df['Transaction_Type'] == 'Income']
    elif option == 'Expenditure':
        df_filtered = df[df['Transaction_Type'] == 'Expenditure']

    # Plot histogram and density plot
    mean_val = df_filtered["Transaction_Amount"].mean()
    median_val = df_filtered["Transaction_Amount"].median()
    # mode_val = stats.mode(df_filtered["Transaction_Amount"])[0][0]
    mode_val = stats.mode(df_filtered["Transaction_Amount"],keepdims=True)[0][0]

    st.subheader('Distribution of Transaction Amount')
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

    st.write("Due to the right-skewed nature of the Transaction_Amount data, we employ log transformation to achieve a more symmetrical distribution. This transformation mitigates the impact of large values on the distribution, compresses the range of values, and stabilizes variance. Additionally, it promotes linearity in the relationship between variables, a desirable trait in statistical modeling and analysis.")

    df_filtered['Transaction_Amount_log'] = np.log(df_filtered['Transaction_Amount'])

    # Plot histogram and density plot after log
    mean_val = df_filtered["Transaction_Amount_log"].mean()
    median_val = df_filtered["Transaction_Amount_log"].median()
    #mode_val = stats.mode(df_filtered["Transaction_Amount_log"])[0][0]
    mode_val = stats.mode(df_filtered["Transaction_Amount_log"],keepdims=True)[0][0]

    st.subheader('Distribution of Log-transformed Transaction Amount')
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
    st.image(wordcloud.to_array(), use_column_width=True)

    grouped_data = df_filtered.groupby(['Week', 'Category_Name'])['Transaction_Amount'].sum().reset_index()

    # Pivot the grouped data for easier plotting
    pivot_table = grouped_data.pivot('Week', 'Category_Name', 'Transaction_Amount').fillna(0)


    # Categories
    unique_categories = df_filtered['Category_Name'].unique()

    # Define a dictionary to map each category to a color from the "Set2" palette
    category_colors = dict(zip(unique_categories, sns.color_palette("Set3", len(unique_categories))))

    # Distribution of Transaction Categories
    st.subheader('Distribution of Transaction Categories')
    plt.figure(figsize=(12, 6))
    sns.countplot(x='Category_Name', data=df_filtered, palette=category_colors)
    plt.xticks(rotation=45)
    plt.title('Distribution of Transaction Categories')
    st.pyplot()

    # Proportion of Each Category
    st.subheader('Proportion of Each Category')
    category_proportions = df_filtered['Category_Name'].value_counts(normalize=True)
    plt.figure(figsize=(10, 8))
    category_proportions.plot(kind='pie', autopct='%1.1f%%',
                              colors=[category_colors.get(x) for x in category_proportions.index])
    plt.title('Proportion of Each Category')
    plt.ylabel('')  # Hide the y-label
    st.pyplot()

    # # Clustered Bar Chart
    # st.subheader('Weekly Transaction Amounts by Category')
    # pivot_table = df_filtered.pivot_table(index='Week', columns='Category_Name', values='Transaction_Amount',
    #                                       aggfunc='sum', fill_value=0)
    # pivot_table.plot(kind='bar', figsize=(14, 7), color=[category_colors.get(x) for x in pivot_table.columns])
    # plt.title('Weekly Transaction Amounts by Category')
    # plt.xlabel('Week Number')
    # plt.ylabel('Total Transaction Amount')
    # plt.legend(title='Category Name')
    # st.pyplot()

    # Stacked Bar Chart
    st.subheader('Weekly Transaction Amounts by Category')
    pivot_table = df_filtered.pivot_table(index='Week', columns='Category_Name', values='Transaction_Amount',
                                          aggfunc='sum', fill_value=0)
    pivot_table.plot(kind='bar', stacked=True, figsize=(14, 7),
                     color=[category_colors.get(x) for x in pivot_table.columns])
    plt.title('Weekly Transaction Amounts by Category')
    plt.xlabel('Week Number')
    plt.ylabel('Total Transaction Amount')
    plt.legend(title='Category Name')
    st.pyplot()


    # Split violin plot
    st.subheader("Distribution of log(Transaction Amount) by Member Status")
    plt.figure(figsize=(10, 6))
    palette_colors = {'NON WAG': 'lightblue', 'WAG': 'lightpink'}
    sns.violinplot(x='Transaction_Nature', y='Transaction_Amount_log', hue='Member_Status', data=df_filtered, split=True,
                   palette=palette_colors, inner="quart")

    plt.xlabel('Transaction_Nature', fontweight='bold')
    plt.ylabel('Transaction Amount (log)', fontweight='bold')
    plt.title('Split Violin Plot of log(Transaction Amount) by Transaction Nature and Member Status')

    plt.xticks(rotation=45)
    plt.legend(title='Member Status', loc='lower left')
    st.pyplot(plt)


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

    # # Pivot
    # st.subheader("Average Tlog(ransaction Amount) by State and Member Status")
    # pivot_df = df_filtered.pivot_table(index='State', columns='Member_Status', values='Transaction_Amount_log', aggfunc='mean')
    #
    # plt.figure(figsize=(12, 8))
    # sns.heatmap(pivot_df, cmap='Greens', annot=True, fmt=".1f", linewidths=.5)
    # # plt.title('Average log(Transaction Amount) by State and Member Status')
    # plt.xlabel('Member Status', fontweight='bold')
    # plt.ylabel('State', fontweight='bold')
    # plt.xticks(rotation=45)
    # plt.tight_layout()
    #
    # # Display the plot in Streamlit
    # st.pyplot()


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

    # Shapiro-Wilk test for normality
    # shapiro_stat_in_group, shapiro_p_in_group = shapiro(wag_transaction_amount_log)
    # shapiro_stat_not_in_group, shapiro_p_not_in_group = shapiro(non_wag_transaction_amount_log)
    # st.write("Shapiro-Wilk test for normality:")
    # st.write("In Group - Statistic:", shapiro_stat_in_group, " p-value:", "{:.4f}".format(shapiro_p_in_group))
    # st.write("Not In Group - Statistic:", shapiro_stat_not_in_group, " p-value:", "{:.4f}".format(shapiro_p_not_in_group))

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

    # # Fixed transaction amount
    # st.markdown("- If there is a significant difference in :blue[**the mean fixed transaction amount**] between WAG and NON WAG?")
    # fixed_wag = np.log(
    #     df_filtered[(df_filtered['Member_Status'] == 'WAG') & (df_filtered['Transaction_Nature'] == 'Fixed')][
    #         'Transaction_Amount'])
    # fixed_non_wag = np.log(
    #     df_filtered[(df_filtered['Member_Status'] == 'NON WAG') & (df_filtered['Transaction_Nature'] == 'Fixed')][
    #         'Transaction_Amount'])
    #
    # t_stat, p_value = stats.ttest_ind(fixed_wag, fixed_non_wag)
    #
    # alpha = 0.05
    # if p_value < alpha:
    #     st.write("**Reject the null hypothesis**, there is a significant difference in the mean fixed transaction amount between the two groups.")
    # else:
    #     st.write("**Fail to reject the null hypothesis**,"
    #              "there is no significant difference in the mean fixed transaction amount between the two groups.")
    # st.divider()
    #
    # # Variable transaction amount
    # st.markdown("- If there is a significant difference in :blue[**the mean variable transaction amount**] between WAG and NON WAG?")
    # var_wag = np.log(
    #     df_filtered[(df_filtered['Member_Status'] == 'WAG') & (df_filtered['Transaction_Nature'] == 'Variable')][
    #         'Transaction_Amount'])
    # var_non_wag = np.log(
    #     df_filtered[(df_filtered['Member_Status'] == 'NON WAG') & (df_filtered['Transaction_Nature'] == 'Variable')][
    #         'Transaction_Amount'])
    #
    # t_stat, p_value = stats.ttest_ind(var_wag, var_non_wag)
    #
    # alpha = 0.05
    # if p_value < alpha:
    #     st.write("**Reject the null hypothesis**, there is a significant difference in the mean variable transaction amount between the two groups.")
    # else:
    #     st.write("**Fail to reject the null hypothesis**, there is no significant difference in the mean variable transaction amount between the two groups.")


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


def challenges():
    st.header("Challenge")

    challenge_info = """

    ### Communication with WB
    - **Description:** This challenge involves effective communication with the World Bank to shape and align the project with their expectations and requirements.
    - **Significance:** Ensuring clear communication helps in understanding and meeting the objectives set by the World Bank, leading to a successful collaboration.

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
    st.header("further_analysis")

if __name__ == "__main__":
    main()