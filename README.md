# 🎓 GradeGuru: Student Exam Performance Predictor  

**GradeGuru** is an end-to-end machine learning pipeline and web application designed to predict a student’s exam performance. The system integrates **situational factors** (e.g., hours studied, attendance, access to resources, family income) and **psychological factors** (e.g., motivation level, parental involvement, peer influence, learning disabilities) to deliver reliable exam score predictions.  

---

## 🚀 Key Features  

- **Full ML Pipeline**  
  - Data ingestion & preprocessing for mixed numerical and categorical data  
  - Robust handling of missing values and unseen categories at inference  
  - Consistent feature ordering to ensure reproducibility  

- **Model Training & Evaluation**  
  - Multiple models tested with hyperparameter tuning  
  - Performance evaluated using standard regression/classification metrics (depending on task formulation)  
  - Best model + preprocessor saved as artifacts for deployment  

- **Deployment-Ready**  
  - Flask-based web app with an intuitive form interface  
  - Real-time predictions for new student data  
  - Backend robustness to handle edge cases gracefully  

- **End-to-End Workflow**  
  From raw data → preprocessing → model training → evaluation → deployment → user interaction.  

---

## 🧠 Problem Motivation  

Exam performance depends not only on **academic preparation** but also on **social, economic, and psychological dimensions**.  
By integrating these diverse factors, GradeGuru provides a more holistic prediction system—useful for educators, parents, and policymakers to identify at-risk students early.  

---

## ⚙️ Tech Stack  

- **Languages & Libraries:** Python, Pandas, NumPy, Scikit-learn  
- **Backend:** Flask  
- **Visualization:** Matplotlib, Seaborn  
- **Environment:** Jupyter Notebook for experimentation, Flask for deployment
- **Deployement:** Vercel  


---

## 📊 Visualization  

The project includes exploratory data analysis (EDA) and visualization modules to understand the influence of factors on exam performance. Some examples:  

- **Correlation heatmaps** to identify strong predictors  
- **Boxplots & histograms** for distribution of study hours, attendance, and scores  
- **Bar charts** to compare categorical features (school type, parental involvement, etc.)  
- **Feature importance plots** from trained models  

These visualizations guide model design and provide insights into which situational and psychological factors most affect student outcomes.  

<img width="394" height="356" alt="correlation" src="https://github.com/user-attachments/assets/524c1ccd-2d74-4795-b08d-a3d496225748" />
<img width="416" height="226" alt="graph" src="https://github.com/user-attachments/assets/d714e8aa-b0ab-4a7c-ba8f-9b3baabf8ecd" />
<img width="602" height="187" alt="boxes" src="https://github.com/user-attachments/assets/26f5a8e6-8bdd-4ff4-a85b-03554e51ed30" />

---

## 🏁 The WebApp

<img width="1104" height="1080" alt="Screenshot (554)" src="https://github.com/user-attachments/assets/f5549018-f66c-46e4-9719-432d2cf869b4" />

---

## 📌 Future Improvements

1. Integration with student information systems (SIS)
2. Deployment on cloud (AWS/GCP/Heroku) for scalability
3. Improved interpretability with SHAP/LIME for feature-level explanations
4. Expansion of dataset for better generalization.  

---

