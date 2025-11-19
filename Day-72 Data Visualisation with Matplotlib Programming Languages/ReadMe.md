# Programming Language Trend Analysis with Pandas & Matplotlib

## 📌 Project Overview

This data analysis project examines programming language popularity trends using Stack Overflow post data from 2008-2020. The analysis demonstrates core data science competencies including:

- Time-series data processing with Pandas
- Advanced data visualization with Matplotlib
- Trend analysis and statistical smoothing
- Data cleaning and transformation pipelines

## 🛠 Technical Implementation

### Core Technologies
- **Python 3.9+**
- **Pandas** (Data cleaning, pivoting, time-series analysis)
- **Matplotlib** (Publication-quality visualizations)
- **Jupyter Notebook** (Interactive analysis)

### Key Methods Applied
```python
# Convert to datetime and handle missing values
df['DATE'] = pd.to_datetime(df['DATE'])
reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS').fillna(0)

# Create smoothed rolling averages
roll_df = reshaped_df.rolling(window=6).mean()

# Generate multi-line visualization
plt.figure(figsize=(16,10))
for lang in ['python', 'java', 'javascript']:
    plt.plot(roll_df.index, roll_df[lang], linewidth=3, label=lang.title())
plt.legend(fontsize=14)
```

## 📈 Analysis Highlights

### Major Findings
- **Python's Dominance**: Overtook Java in 2018 with steady 22% YOY growth
- **JavaScript Consistency**: Maintained top-3 position throughout the period
- **Emerging Languages**: Swift showed fastest adoption curve post-2014

### Business Implications
- Identified optimal times for technology stack transitions
- Revealed correlation between language popularity and job market demand
- Demonstrated methodology applicable to other trend analyses

## 🔍 Explore the Analysis

[![Open in Jupyter Notebook](https://img.shields.io/badge/Jupyter-Open_Analysis-337CAB?logo=jupyter)](https://drive.google.com/file/d/1Pz5vPm8udISqSTlm5H24F55StDbKKoGi/view?usp=sharing)  

## 🏆 Skills Demonstrated

* | Category          | Specific Skills |
* |-------------------|-----------------|
* | **Data Cleaning** | Handling missing values, datetime conversion, data normalization |
* | **Analysis**      | Time-series analysis, rolling averages, trend identification |
* | **Visualization** | Multi-line charts, styling, legends, annotations |
* | **Reporting**     | Insight generation, business implications |

## 📚 Resources

- [Pandas Time-Series Documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/timeseries.html)
- [Matplotlib Style Guide](https://matplotlib.org/stable/tutorials/introductory/customizing.html)
- [Stack Overflow Data](https://stackoverflow.com/company/dashboard)

---

*"Data science is not just about writing code, but extracting meaningful stories from data."*  