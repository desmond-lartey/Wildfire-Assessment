#!/usr/bin/env python
# coding: utf-8

# In[4]:


# Importing necessary libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the merged and categorized dataset
def load_data():
    return pd.read_excel("Updated_Merged_Categorized_South_Africa_Wildland_Fire_Survey2.xlsx")

merged_data_df = load_data()

# Side Bar
st.sidebar.title("User Selection")

# Select category
categories = merged_data_df["Category"].unique().tolist()
selected_category = st.sidebar.selectbox("Select a category:", categories)

# List questions based on selected category
questions = merged_data_df[merged_data_df["Category"] == selected_category]["Question"].unique().tolist()
selected_question_1 = st.sidebar.selectbox("Select the first question:", questions)

analysis_type = st.sidebar.radio("Choose the type of analysis:", ("correlation", "comparative"))

# If correlation, allow the selection of a second question
if analysis_type == "correlation":
    selected_question_2 = st.sidebar.selectbox("Select the second question:", [q for q in questions if q != selected_question_1])
else:
    selected_question_2 = None

# Choose demographic and chart type
demographics = ["Race", "Gender", "Province", "Occupation"]
selected_demo = st.sidebar.selectbox("Choose a demographic:", demographics)

chart_types = ["heatmap", "bar", "pie", "line"]
selected_chart_type = st.sidebar.selectbox("Choose a chart type:", chart_types)

# Function to plot correlation or comparative analysis
def plot_analysis(question1, question2, demo, chart_type, analysis_type):
    # Filtering data based on the selected questions and demographic
    q1_data = merged_data_df[merged_data_df["Question"] == question1]
    
    if analysis_type == "correlation":
        q2_data = merged_data_df[merged_data_df["Question"] == question2]
        # Merging the two questions on Respondent ID
        merged_q_data = pd.merge(q1_data, q2_data, on="Respondent ID", how="inner", suffixes=('_q1', '_q2'))
        crosstab_data = pd.crosstab(merged_q_data["Response_q1"], merged_q_data["Response_q2"])
        
        # Plotting heatmap for correlation
        if chart_type == "heatmap":
            fig, ax = plt.subplots(figsize=(15, 10))
            sns.heatmap(crosstab_data, annot=True, cmap="YlGnBu", cbar=True, ax=ax, annot_kws={"size": 12})
            ax.set_title(f"Correlation between '{question1}' and '{question2}' by {demo}", fontsize=16)
            ax.set_ylabel("Responses to " + question1, fontsize=14)
            ax.set_xlabel("Responses to " + question2, fontsize=14)
            ax.tick_params(axis='both', which='major', labelsize=12)
            plt.tight_layout()
            st.pyplot(fig)
    
    elif analysis_type == "comparative":
        # Comparative analysis for a single question across the chosen demographic
        response_counts = q1_data.groupby(demo)["Response"].value_counts().unstack().fillna(0)
        
        # Stacked bar chart for comparative analysis
        if chart_type == "bar":
            fig, ax = plt.subplots(figsize=(20, 12))
            response_counts.plot(kind="bar", stacked=True, colormap="viridis", ax=ax)
            ax.set_title(f"Comparative Analysis of '{question1}' by {demo}", fontsize=20)
            ax.set_ylabel("Number of Respondents", fontsize=25)
            ax.set_xlabel(demo, fontsize=14)
            ax.legend(title="Responses", bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=18)
            ax.tick_params(axis='both', which='major', labelsize=16)
            plt.tight_layout()
            st.pyplot(fig)
        
        # Pie chart for comparative analysis
        elif chart_type == "pie":
            for demo_value, group in q1_data.groupby(demo):
                fig, ax = plt.subplots(figsize=(12, 10))
                group["Response"].value_counts().plot(kind="pie", autopct='%1.1f%%', startangle=140, ax=ax)
                ax.set_title(f"Responses for '{question1}' in {demo} = {demo_value}", fontsize=16)
                ax.set_ylabel("")
                plt.tight_layout()
                st.pyplot(fig)
        
        # Line chart for comparative analysis
        elif chart_type == "line":
            fig, ax = plt.subplots(figsize=(15, 10))
            response_counts.T.plot(ax=ax)
            ax.set_title(f"Comparative Analysis of '{question1}' by {demo}", fontsize=16)
            ax.set_ylabel("Number of Respondents", fontsize=14)
            ax.set_xlabel("Responses", fontsize=14)
            ax.legend(title=demo, fontsize=12)
            ax.tick_params(axis='both', which='major', labelsize=12)
            plt.tight_layout()
            st.pyplot(fig)

# Main Content
st.title("South Africa Wildland Fire Survey Analysis")
if st.sidebar.button("Plot"):
    plot_analysis(selected_question_1, selected_question_2, selected_demo, selected_chart_type, analysis_type)

