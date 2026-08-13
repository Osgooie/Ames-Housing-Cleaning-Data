# 🏠 Ames Housing Price Prediction

[![Python](https://img.shields.io/badge/Python-3.14.5-blue.svg)](https://www.python.org/)
[![Pandas](https://img.shields.io/badge/Pandas-3.0.3-green.svg)](https://pandas.pydata.org/)
[![NumPy](https://img.shields.io/badge/NumPy-2.4.6-orange.svg)](https://numpy.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.11.1-red.svg)](https://matplotlib.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-1.9.0-yellow.svg)](https://scikit-learn.org/)
## 📊 **Project Overview**

This project focuses on **data cleaning and preprocessing** of the famous Ames Housing dataset. 
The dataset contains **79 features** describing residential homes, but it suffers from numerous missing values, inconsistent categorical variables, and outliers.

### 🎯 **Project Objectives**

- **Deep Data Cleaning**: Handle missing values across 80+ columns using appropriate strategies (filling with `None`, `0`, `Median`, or `Mode`).
- **Feature Engineering**: Create new meaningful features (e.g., `Has_Bsmt`, `House_Age`, `Total_Baths`) to extract more value from raw data.
- **Data Transformation**: Convert categorical variables into numerical formats using `Label Encoding` to make the data ready for machine learning models.
- **Exploratory Data Analysis (EDA)**: Visualize distributions and correlations to understand the key drivers of house prices.

### 🗑️ **Data Cleaning Summary**

| Action | Details |
| :--- | :--- |
| **Removed Columns** | Dropped columns with >70% missing values (e.g., `Alley`, `Pool QC`, `Fence`, `Misc Feature`). |
| **Missing Values** | Handled systematically: Categorical → `'None'` / `'Unknown'`, Numerical → `0` or `Median`. |
| **Feature Engineering** | Created `Has_Bsmt`, `Has_Garage`, `Has_Fireplace` binary features, and total area features. |
| **Data Type Conversion** | Converted all categorical/text columns to numerical using `LabelEncoder`. |
| **Final Dataset** | A clean, numerical dataset with **0 missing values**, ready for any machine learning pipeline. |

> **Note**: This project currently covers the complete **data preprocessing** phase. The cleaned dataset is saved and ready for future modeling (e.g., Linear Regression, Random Forest, XGBoost).

---

### 🎯 **Key Highlights**

- **Dataset**: 2,930 rows, 79 features + 1 target (`SalePrice`)
- **Missing Data**: Handled thousands of missing values across 20+ columns
- **Feature Engineering**: Added new features like `Has_Bsmt`, `House_Age`, `Total_Baths`
- **Output**: A clean, fully numerical dataset with **0 missing values**
- **Next Step**: Ready for machine learning model training

## 🧹 **Data Cleaning Process**

### 1️⃣ **Handling Missing Values**
- **Categorical Columns**: Replaced with `'None'` (meaning "does not have") or `'Unknown'` (meaning "not recorded").
- **Numerical Columns**: Replaced with `0` for features like basement area, garage area, and bathroom counts.

### 2️⃣ **Feature Engineering**
- **`Has_Bsmt`**: Binary flag for houses with a basement.
- **`Has_Garage`**: Binary flag for houses with a garage.
- **`House_Age`**: Calculated from `Yr Sold` - `Year Built`.
- **`Total_Baths`**: Sum of full and half bathrooms.

### 3️⃣ **Encoding Categorical Variables**
- Used `LabelEncoder` to convert all categorical features (e.g., `Neighborhood`, `MS Zoning`) into numerical values.

### 4️⃣ **Final Dataset**
- Clean dataset saved as `AmesHousing_Cleaned.csv` in the `data/` folder.
- Shape: **2,930 rows × 68 columns**.
- **0 missing values**.

## 📋 **Dataset Dictionary**

> **Explore the Ames Housing dataset with this comprehensive guide.**

### 🏠 **General & Location Features**

| # | Column | Description (English) | توضیح (فارسی) |
|:-:|:---|:---|:---|
| 1 | **Order** | Sequential order of the record | شماره ترتیب رکورد در دیتاست |
| 2 | **PID** | Unique identifier for each property parcel | شناسه یکتای هر ملک |
| 3 | **MS SubClass** | Building class or type | نوع یا کلاس ساختمان |
| 4 | **MS Zoning** | General zoning classification | نوع منطقه‌بندی شهری (کاربری زمین) |
| 5 | **Lot Frontage** | Linear feet of street frontage | عرض زمین از سمت خیابان (فوت) |
| 6 | **Lot Area** | Total lot size in square feet | مساحت کل زمین (فوت مربع) |
| 7 | **Street** | Type of road access | نوع خیابان دسترسی |
| 8 | **Alley** | Alley access type | نوع کوچه دسترسی |
| 9 | **Lot Shape** | General shape of the property lot | شکل هندسی زمین |
| 10 | **Land Contour** | Flatness or contour level | وضعیت همواری یا شیب زمین |
| 11 | **Utilities** | Available public utilities | امکانات و خدمات شهری موجود |
| 12 | **Lot Config** | Configuration or position of the lot | نحوه قرارگیری زمین نسبت به خیابان |
| 13 | **Land Slope** | Slope inclination level | میزان شیب زمین |
| 14 | **Neighborhood** | Physical location within the city | محله قرارگیری ملک |
| 15 | **Condition 1** | Proximity to main road/railway (1st) | شرایط محیطی اطراف ملک (اول) |
| 16 | **Condition 2** | Proximity to main road/railway (2nd) | شرایط محیطی اطراف ملک (دوم) |
 
### 🏗️ **Building & Structure Features**

| # | Column | Description (English) | توضیح (فارسی) |
|:-:|:---|:---|:---|
| 17 | **Bldg Type** | Type of dwelling structure | نوع ساختمان |
| 18 | **House Style** | Style and number of stories | سبک یا تعداد طبقات خانه |
| 19 | **Overall Qual** | Overall material and finish quality | کیفیت کلی طراحی و ساخت خانه |
| 20 | **Overall Cond** | Current condition and maintenance | وضعیت کلی و میزان نگهداری ساختمان |
| 21 | **Year Built** | Original construction year | سال ساخت خانه |
| 22 | **Year Remod/Add** | Remodeling or addition year | سال بازسازی یا نوسازی |
| 23 | **Roof Style** | Type of roof design | نوع طراحی سقف |
| 24 | **Roof Matl** | Roof covering material | جنس پوشش سقف |
| 25 | **Exterior 1st** | Primary exterior wall covering | جنس نمای اصلی ساختمان |
| 26 | **Exterior 2nd** | Secondary exterior wall covering | جنس نمای دوم ساختمان |
| 27 | **Mas Vnr Type** | Masonry veneer type (stone, brick, etc.) | نوع نمای تزئینی (سنگ، آجر و ...) |
| 28 | **Mas Vnr Area** | Masonry veneer area in sq. ft. | مساحت نمای تزئینی (فوت مربع) |
| 29 | **Exter Qual** | Exterior material quality | کیفیت نمای بیرونی |
| 30 | **Exter Cond** | Exterior material condition | وضعیت نمای بیرونی |
| 31 | **Foundation** | Type of foundation | نوع فونداسیون ساختمان |


### 🏚️ **Basement & Garage Features**

| # | Column | Description (English) | توضیح (فارسی) |
|:-:|:---|:---|:---|
| 32 | **Bsmt Qual** | Basement quality rating | کیفیت زیرزمین |
| 33 | **Bsmt Cond** | Basement condition status | وضعیت زیرزمین |
| 34 | **Bsmt Exposure** | Walkout or garden level basement exposure | میزان نورگیری یا دید زیرزمین |
| 35 | **BsmtFin Type 1** | First basement finished area type | نوع تکمیل بخش اول زیرزمین |
| 36 | **BsmtFin SF 1** | First basement finished area (sq. ft.) | مساحت بخش تکمیل‌شده اول زیرزمین |
| 37 | **BsmtFin Type 2** | Second basement finished area type | نوع تکمیل بخش دوم زیرزمین |
| 38 | **BsmtFin SF 2** | Second basement finished area (sq. ft.) | مساحت بخش تکمیل‌شده دوم زیرزمین |
| 39 | **Bsmt Unf SF** | Unfinished basement area (sq. ft.) | مساحت تکمیل‌نشده زیرزمین |
| 40 | **Total Bsmt SF** | Total basement area (sq. ft.) | کل مساحت زیرزمین |
| 41 | **Heating** | Type of heating system | نوع سیستم گرمایشی |
| 42 | **Heating QC** | Heating system quality | کیفیت سیستم گرمایشی |
| 43 | **Central Air** | Central air conditioning availability | وجود سیستم تهویه مطبوع مرکزی |
| 44 | **Electrical** | Electrical system type (fuse, breaker, etc.) | نوع سیستم برق‌کشی |
| 60 | **Garage Type** | Garage type (attached, detached, etc.) | نوع گاراژ |
| 61 | **Garage Yr Blt** | Garage construction year | سال ساخت گاراژ |
| 62 | **Garage Finish** | Garage interior finish type | میزان تکمیل بودن فضای داخلی گاراژ |
| 63 | **Garage Cars** | Garage capacity (number of cars) | ظرفیت گاراژ بر حسب تعداد خودرو |
| 64 | **Garage Area** | Garage size in square feet | مساحت گاراژ |
| 65 | **Garage Qual** | Garage quality rating | کیفیت گاراژ |
| 66 | **Garage Cond** | Garage condition status | وضعیت گاراژ |
| 67 | **Paved Drive** | Paved driveway access type | وضعیت آسفالت بودن مسیر ورودی |

### 📐 **Area & Room Features**

| # | Column | Description (English) | توضیح (فارسی) |
|:-:|:---|:---|:---|
| 45 | **1st Flr SF** | First floor square footage | مساحت طبقه اول |
| 46 | **2nd Flr SF** | Second floor square footage | مساحت طبقه دوم |
| 47 | **Low Qual Fin SF** | Low quality finished square footage | مساحت فضای تکمیل‌شده با کیفیت پایین |
| 48 | **Gr Liv Area** | Above-grade living area (sq. ft.) | کل فضای قابل سکونت بالای سطح زمین |
| 49 | **Bsmt Full Bath** | Full bathrooms in the basement | تعداد حمام کامل در زیرزمین |
| 50 | **Bsmt Half Bath** | Half bathrooms in the basement | تعداد نیم‌حمام در زیرزمین |
| 51 | **Full Bath** | Full bathrooms above grade | تعداد حمام کامل |
| 52 | **Half Bath** | Half bathrooms above grade | تعداد نیم‌حمام |
| 53 | **Bedroom AbvGr** | Bedrooms above grade (excluding basement) | تعداد اتاق خواب بالای سطح زمین |
| 54 | **Kitchen AbvGr** | Kitchens above grade | تعداد آشپزخانه |
| 55 | **Kitchen Qual** | Kitchen quality rating | کیفیت آشپزخانه |
| 56 | **TotRms AbvGrd** | Total rooms above grade (excluding bathrooms) | تعداد کل اتاق‌های بالای سطح زمین (به جز حمام) |
| 57 | **Functional** | Home functionality rating | وضعیت عملکرد و کارایی خانه |
| 58 | **Fireplaces** | Total number of fireplaces | تعداد شومینه |
| 59 | **Fireplace Qu** | Fireplace quality rating | کیفیت شومینه |
| 68 | **Wood Deck SF** | Wood deck area (sq. ft.) | مساحت تراس یا سکوی چوبی |
| 69 | **Open Porch SF** | Open porch area (sq. ft.) | مساحت ایوان روباز |
| 70 | **Enclosed Porch** | Enclosed porch area (sq. ft.) | مساحت ایوان سرپوشیده |
| 71 | **3Ssn Porch** | Three-season porch area (sq. ft.) | مساحت ایوان سه‌فصل |
| 72 | **Screen Porch** | Screen porch area (sq. ft.) | مساحت ایوان توری‌دار |
| 73 | **Pool Area** | Pool area (sq. ft.) | مساحت استخر |
| 74 | **Pool QC** | Pool quality rating | کیفیت استخر |
| 75 | **Fence** | Fence quality or type | نوع حصار یا نرده ملک |
| 76 | **Misc Feature** | Miscellaneous feature (e.g., elevator, workshop) | سایر امکانات ویژه ملک |
| 77 | **Misc Val** | Dollar value of miscellaneous features | ارزش ریالی امکانات جانبی |

### 📅 **Sale & Transaction Features**

| # | Column | Description (English) | توضیح (فارسی) |
|:-:|:---|:---|:---|
| 78 | **Mo Sold** | Month the property was sold | ماه فروش ملک |
| 79 | **Yr Sold** | Year the property was sold | سال فروش ملک |
| 80 | **Sale Type** | Type of sale transaction | نوع معامله یا فروش |
| 81 | **Sale Condition** | Sale condition (normal, partial, etc.) | شرایط فروش |
| 82 | **SalePrice** | Final sale price (Target Variable) | قیمت نهایی فروش خانه (متغیر هدف) |

> **📌 Note**: This comprehensive dictionary helps you understand every column in the Ames Housing dataset.

## 🛠️ **Technologies Used**

| Category | Technology | Version |
| :--- | :--- | :--- |
| **Language** | Python | 3.14.5 |
| **Data Manipulation** | Pandas | 3.0.3 |
| **Numerical Computing** | NumPy | 2.4.6 |
| **Data Visualization** | Matplotlib | 3.11.1 ||
| **Machine Learning** | Scikit-Learn | 1.9.0 |
| **Environment** | Jupyter Notebook | 7.0.0 |

---

## 📁 **Project Structure**

```
Ames-Housing-Project/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── data/
│   |── AmesHousing.csv
|   └── AmesHousing_Cleaned.csv
│
├── images/
│   
├── notebooks/
│   └──AmesHousing.ipynb
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   └── data_cleaner.py
│
└── models/
```

---

## 🔧 **Installation & Setup**

### 1️⃣ **Clone the Repository**

```bash
git clone https://github.com/osgooie/Ames-Housing-Cleaning-Data.git
cd Ames-Housing-Cleaning-Data
```

### 2️⃣ **Create a Virtual Environment (Recommended)**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3️⃣ **Install Dependencies**

```bash
pip install -r requirements.txt
```

### 4️⃣ **Run Jupyter Notebook**

```bash
jupyter notebook notebooks/01_EDA_and_Data_Cleaning.ipynb
```

---

## 📦 **Dependencies**

All required packages are listed in `requirements.txt`:

```txt
pandas==3.0.3
numpy==2.4.6
matplotlib==3.11.1
scikit-learn==1.9.0
jupyter==7.0.0
```

> **Note**: Python 3.14.5 or higher is required.

---

## 📊 **Results**

- **Cleaned Dataset Shape**: 2,930 rows, 68 columns
- **Missing Values**: 0 (All columns are fully populated)
- **Categorical Columns Encoded**: 15+ columns
- **New Features Created**: 5+ features
---

## 📌 **Future Improvements**

- [ ] Add more advanced feature engineering
- [ ] Deploy as a web application (Flask/Streamlit)
- [ ] Add uncertainty estimation using Bayesian methods
- [ ] Implement real-time prediction API

---

## 📄 **License**

This project is licensed under the MIT License.

---

## 👨‍💻 **Author**

- **Ali Zaki Osgooie** - [GitHub](https://github.com/Osgooie)

---

## 🙏 **Acknowledgments**

- Kaggle for providing the dataset
- The open-source community for amazing tools

---