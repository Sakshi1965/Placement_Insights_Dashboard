# Placement Insights Dashboard 🎓
# Author: Sakshi Shinde
# Description: A Streamlit dashboard that visualizes student placement data with filters and insights.

import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme(style="whitegrid", palette="mako")

st.set_page_config(
    page_title="Placement Insights Dashboard 🎓",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
        body {
            background-color: #F7F9FB;
        }
        [data-testid="stMetricValue"] {
            color: #4CAF50;
            font-weight: bold;
        }
        h1, h2, h3 {
            color: #2E4053;
        }
    </style>
""", unsafe_allow_html=True)

df = pd.read_csv('data/cleaned_data.csv')
st.title('Placement Insights Dashboard')
st.sidebar.header("🎛️ Filter Options")

# ---------------- Sidebar Filters ----------------
selected_gender = st.sidebar.selectbox(
    "Select Gender",
    ["All"] + list(df["gender"].unique()),
    key="gender_filter"
)
if selected_gender != "All":
    df = df[df["gender"] == selected_gender]

selected_workex = st.sidebar.selectbox(
    "Select Work Experience",
    ["All"] + list(df["workex"].unique()),
    key="workex_filter"
)
if selected_workex != "All":
    df = df[df["workex"] == selected_workex]

selected_degree_t = st.sidebar.selectbox(
    "Select Degree Type",
    ["All"] + list(df["degree_t"].unique()),
    key="degree_filter"
)
if selected_degree_t != "All":
    df = df[df["degree_t"] == selected_degree_t]

# Reset button
if st.sidebar.button("🔄 Reset Filters"):
    st.session_state.clear()
    st.session_state.gender_filter = "All"
    st.session_state.workex_filter = "All"
    st.session_state.degree_filter = "All"
    st.rerun()

# ---------------- Basic Calculations ----------------
df['placed_flag'] = df['status'].map({'Placed': 1, 'Not Placed': 0})

total_students = len(df)
placed_students = len(df[df['status'] == 'Placed'])
placement_rate = round((placed_students / total_students) * 100, 2)
average_salary = round(df[df['status'] == 'Placed']['salary'].mean(), 2)

# ---------------- Metrics ----------------
col1, col2, col3, col4 = st.columns(4)
col1.metric('Total Students', total_students)
col2.metric('Placed Students', placed_students)
col3.metric('Placement Rate', placement_rate)
col4.metric('Average Salary (LPA)', f"{average_salary:.2f}")

# Download filtered data
st.markdown("### ⬇️ Download Filtered Data")
st.download_button(
    label="Download CSV",
    data=df.to_csv(index=False),
    file_name="filtered_placement_data.csv",
    mime="text/csv"
)

st.divider()

# ---------------- Tabs ----------------
tab1, tab2, tab3 = st.tabs(["📊 Overview", "🎓 Placement Insights", "💰 Salary & Performance"])

# ============ TAB 1: OVERVIEW ============
with tab1:
    st.subheader("🎓 Dataset Preview")
    st.dataframe(df.head())

    # Pie Chart - Overall Placement Ratio
    status_counts = df['status'].value_counts()
    fig, ax = plt.subplots()
    ax.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
    ax.set_title('Overall Placement Ratio')
    st.pyplot(fig)
    st.write("✅ **Insight:** Around 65% of students were placed, indicating a decent placement rate overall.")

    # Correlation Heatmap
    st.subheader("📊 Correlation Heatmap")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    fig, ax = plt.subplots()
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    ax.set_title('Feature Correlation Heatmap')
    st.pyplot(fig)
    st.write("💡 **Insight:** Higher CGPA may correlate with better placement chances or higher salaries.")

# ============ TAB 2: PLACEMENT INSIGHTS ============
with tab2:
    st.subheader("📈 Placement Insights Visuals")
    st.write("Explore how different factors influence placements.")

    # Gender-wise placement
    fig, ax = plt.subplots()
    sns.countplot(x='gender', hue='status', data=df, palette='plasma', ax=ax)
    ax.set_title('Placement by Gender')
    st.pyplot(fig)
    st.write("🔹 **Insight:** Male students appear to have a slightly higher placement rate than female students.")

    # Degree type placement
    fig, ax = plt.subplots()
    sns.countplot(x='degree_t', hue='status', data=df, palette='plasma', ax=ax)
    ax.set_title('Placement By Degree Type')
    st.pyplot(fig)

    # Work experience placement
    fig, ax = plt.subplots()
    sns.countplot(x='workex', hue='status', data=df, palette='plasma', ax=ax)
    ax.set_title('Placement By Work Experience')
    st.pyplot(fig)

    # Placement Rate by Degree
    st.subheader("🎓 Placement Rate by Specialization")
    placement_rate = (
        df.groupby("degree_t")["status"]
        .apply(lambda x: (x == "Placed").mean() * 100)
        .sort_values(ascending=False)
    )
    fig, ax = plt.subplots()
    sns.barplot(x=placement_rate.index, y=placement_rate.values, palette="viridis", ax=ax)
    ax.set_title("Placement Rate by Degree Type")
    ax.set_ylabel("Placement Rate (%)")
    st.pyplot(fig)
    st.write("💡 **Insight:** Compare which degree types or streams perform best in placements.")

# ============ TAB 3: SALARY & PERFORMANCE ============
with tab3:
    # Salary Histogram
    st.subheader("💰 Salary Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df[df['status'] == 'Placed']['salary'], bins=10, kde=True, color='purple', ax=ax)
    ax.set_title('Salary Distribution of Placed Students')
    ax.set_xlabel('Salary')
    ax.set_ylabel('Count')
    st.pyplot(fig)
    st.write("💰 **Insight:** Most placed students have salaries between 2–3 LPA, with some outliers above 5 LPA.")

    # Scatterplot: CGPA vs Salary
    st.subheader("📉 CGPA vs Salary (Placed Students Only)")
    placed_df = df[df['status'] == 'Placed']
    fig, ax = plt.subplots()
    sns.scatterplot(data=placed_df, x="degree_p", y="salary", hue="gender", style="workex", ax=ax)
    ax.set_title("CGPA vs Salary by Gender and Work Experience")
    ax.set_xlabel("Degree Percentage (CGPA)")
    ax.set_ylabel("Salary (LPA)")
    st.pyplot(fig)
    st.write("💡 **Insight:** Academic performance and work experience both influence salary outcomes.")

    # Average Salary by Degree & WorkEx
    st.subheader("💰 Average Salary by Work Experience and Degree Type")
    avg_salary_by_group = (
        df[df["status"] == "Placed"]
        .groupby(["workex", "degree_t"])["salary"]
        .mean()
        .reset_index()
    )
    fig, ax = plt.subplots()
    sns.barplot(x="degree_t", y="salary", hue="workex", data=avg_salary_by_group, ax=ax)
    ax.set_title("Average Salary by Work Experience and Degree Type")
    ax.set_ylabel("Average Salary (LPA)")
    st.pyplot(fig)

    if st.checkbox("Show Average Salary Insights"):
        st.dataframe(avg_salary_by_group)

# ---------------- Summary Section ----------------
st.divider()
st.header("🧠 Key Observations Summary")
st.write("- Students with work experience generally have higher average salaries.")
st.write("- Degree performance positively correlates with placement chances.")
st.write("- Marketing & HR specialization shows slightly higher placement rate.")

st.caption("Developed by Sakshi Shinde | Data Analyst Portfolio Project")
