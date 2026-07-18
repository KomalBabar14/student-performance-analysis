# 📊 Student Performance Analysis

A Python-based data analysis project that processes student academic records using **Pandas** and visualizes insights with **Matplotlib**.

## 🚀 Features

- Load student data from a CSV file
- Calculate average marks automatically
- Assign grades based on performance
- Identify the overall top performer
- Find subject-wise toppers
- Calculate class average
- Generate pass/fail statistics
- Export processed data to a CSV report
- Create professional data visualizations

## 📂 Project Structure

```
student-performance-analysis/
│
├── data/
│   └── students.csv
│
├── charts/
│   ├── average_scores.png
│   ├── grade_distribution.png
│   └── subject_distribution.png
│
├── analysis.py
├── students_report.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## 📈 Generated Visualizations

- Average Marks by Student
- Grade Distribution
- Subject-wise Average Scores

## 🛠 Technologies

- Python 3
- Pandas
- Matplotlib

## ▶️ How to Run

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/student-performance-analysis.git
```

Navigate into the project:

```bash
cd student-performance-analysis
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the analysis:

```bash
python analysis.py
```

## 📊 Sample Output

```
=============================================
      STUDENT PERFORMANCE REPORT
=============================================

Total Students : 10
Class Average  : 82.93

Top Performer  : Ayesha (95.00)
Lowest Average : Bilal (65.67)

Subject Toppers
- Math: Ayesha
- Science: Ayesha
- English: Zain

Pass Percentage: 100%
```

## 📄 Output Files

Running the script generates:

- Processed CSV report
- Student performance summary
- Average score chart
- Grade distribution chart
- Subject average chart

## 📜 License

This project is available for educational and portfolio purposes.