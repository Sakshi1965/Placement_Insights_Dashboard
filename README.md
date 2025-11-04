# 🎓 Placement Insights Dashboard

An interactive data analytics dashboard built using **Streamlit**, providing deep insights into student placement trends, salary distributions, and performance factors.

---

## 📌 Overview
This project analyzes and visualizes placement data to help understand how factors like **gender**, **degree type**, **academic performance**, and **work experience** influence placement outcomes and salaries.

The dashboard allows users (teachers, analysts, or recruiters) to:
- Filter data by gender, work experience, or degree type
- View placement rates and salary distributions
- Analyze correlations between academic performance and salary
- Download filtered datasets as CSV

---

## 🧠 Key Features
✅ Interactive filters (gender, degree type, work experience)  
✅ Real-time metrics — Total Students, Placement Rate, Average Salary  
✅ Beautiful visualizations (Seaborn + Matplotlib)  
✅ Download filtered dataset  
✅ Tabs for Overview, Insights, and Salary Analysis  
✅ Built using clean, modular Python code

---

## 🛠️ Tech Stack
| Component | Technology Used |
|------------|-----------------|
| **Frontend** | Streamlit |
| **Data Analysis** | Pandas, NumPy |
| **Visualization** | Seaborn, Matplotlib |
| **Backend** | Python |
| **Dataset** | CSV (Cleaned Placement Data) |

---

## 📂 Project Structure

Placement_Insights_Dashboard/
│
├── app/
│ └── placement_dashboards.py
│
├── data/
│ ├── cleaned_data.csv
│ └── raw_placement_data.csv
│
├── notebooks/
│ └── placement_analysis_day4.ipynb
|
│__project_overview.txt
├── requirements.txt
└── README.md


---

## ⚙️ Installation & Setup
### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/Placement_Insights_Dashboard.git
cd Placement_Insights_Dashboard

 ## Create a Virtual Enviornment
python -m venv venv
venv\Scripts\activate

## Install dependencies

pip install -r requirements.txt

## Run the Streamlit App

streamlit run app/placement_dashboards.py

## Sample Insights

Students with work experience have higher placement rates and salaries.

Degree performance (CGPA) strongly correlates with placement success.

Marketing & HR specializations show competitive placement results.

##📦 Future Enhancements

Integration with Power BI or Plotly for advanced visuals

Predictive modeling for salary or placement probability

Dark mode UI for better user experience

## ------ Author -------

Sakshi Shinde
Data Analyst Enthusiast | Python | Power BI | SQL | Streamlit

##---- License ----

This project is open-source and free to use for educational purposes.


---

💡 **Next step for you:**  
1. Copy the above markdown.  
2. Paste it inside your `README.md` file using:
   ```bash
   notepad README.md