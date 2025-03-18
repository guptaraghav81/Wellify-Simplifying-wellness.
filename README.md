# Wellify — Personalized Health and Fitness Recommendation System

A cloud-powered, machine learning-based health and fitness recommendation system that generates personalized exercise and diet plans using **AWS Elastic Beanstalk** for deployment and **Random Forest (scikit-learn)** for predictions. Built on a **14,000-row dataset** with a **Flask web app** for real-time recommendations.

## ✨ Overview
**Wellify** is a cloud-based web application designed to provide **personalized exercise and diet recommendations** based on user inputs such as age, BMI, and health conditions. The machine learning model is deployed using **AWS Elastic Beanstalk**, ensuring scalability and reliability in handling user requests and delivering real-time predictions.

## 🔄 Project Architecture
1. **Model Training (Local Environment):**
   - Cleaned and processed dataset using **Pandas** and **NumPy**.
   - Trained **Random Forest Models** for exercise and diet recommendations.
   - Saved trained models as **.pkl files** for easy deployment.

2. **Web App Development (Flask):**
   - Built a **Flask web app** to serve predictions and handle user requests.
   - Integrated the trained models to generate personalized plans.

3. **Cloud Deployment (AWS):**
   - **Elastic Beanstalk:** Deployed the Flask app on Elastic Beanstalk for automatic scaling and simplified infrastructure management.
   - **EC2:** Underlying compute instances managed by Elastic Beanstalk.
   - **VPC:** Secure cloud environment for networking.
   - **ALB (Application Load Balancer):** Distributes incoming traffic across EC2 instances.
   - **ASG (Auto Scaling Group):** Automatically adjusts the number of EC2 instances based on traffic.
   - **Route 53:** Manages domain name (raghav.cloud) for easy access.
   - **ACM (AWS Certificate Manager):** Provides SSL/TLS certificates for secure HTTPS access.
   - **CloudWatch:** Monitors logs and application health.
   - **S3 (Optional):** Stored trained model files and static assets.
   - **RDS (Optional):** Integrated with **AWS RDS** for storing user data and recommendations.

## 📈 Tech Stack
- **Machine Learning:** Random Forest, Scikit-learn, Pandas, NumPy
- **Web Framework:** Flask
- **Frontend:** HTML, CSS, JavaScript
- **Cloud Services:**
  - **Elastic Beanstalk:** Deployment and scaling
  - **EC2, ALB, ASG, VPC:** Compute and networking
  - **Route 53 & ACM:** Domain management and SSL/TLS security
  - **S3:** Static asset and model file storage
  - **CloudWatch:** Monitoring and logging
  - **RDS:** Data persistence (optional)

## 🔍 How It Works
1. **User Input:** Users provide data such as age, BMI, and health conditions through the web app.
2. **Model Prediction:** Pretrained Random Forest models generate personalized exercise and diet plans.
3. **Results Display:** The web app presents tailored recommendations in a clean, user-friendly format.
4. **Cloud Scaling:** Elastic Beanstalk handles traffic spikes, ensuring seamless performance.
5. **Domain & Security:** Route 53 manages the custom domain, and ACM secures the app with HTTPS.

## 📝 Deployment Steps
1. **Fork and Clone:**
   ```bash
   git clone https://github.com/your-username/wellify.git
   cd wellify
   ```
2. **Prepare the Environment:**
   - Ensure you have **AWS CLI** and **Elastic Beanstalk CLI** installed.
   - Configure AWS CLI:
     ```bash
     aws configure
     ```
3. **Initialize Elastic Beanstalk:**
   ```bash
   eb init -p python-3.8 wellify-app
   ```
4. **Create and Deploy:**
   ```bash
   eb create wellify-env
   eb deploy
   ```
5. **Set Up Custom Domain:** (Optional, if using Route 53)
   - Configure your **Route 53** domain (raghav.cloud) to point to the Elastic Beanstalk environment.
   - Request and attach an **SSL certificate** from **ACM** for HTTPS security.

6. **Access the App:**
   - Open **raghav.cloud** in your browser to access the Wellify app.

## 🛠️ Future Enhancements
- Integrate **AWS Lambda** for serverless prediction.
- Implement **API Gateway** for managing endpoints.
- Add **CI/CD Pipeline** using **AWS CodePipeline** for continuous deployment.

## 🔎 Why Wellify?
- **Personalized Recommendations:** Tailored health insights for each user.
- **Cloud Powered:** Scalable and reliable with AWS.
- **Easy Deployment:** Elastic Beanstalk simplifies infrastructure management.
- **Real-Time Predictions:** Fast and accurate health plans at your fingertips.
- **Secure & Accessible:** Custom domain with SSL/TLS security (raghav.cloud).

---
Deployed with ❤️ on **AWS Elastic Beanstalk** | Made with ☕ by **Raghav Gupta**  

**Ready to Transform Your Health Journey? Try Wellify Now!** 💪  
**URL:** [raghav.cloud](https://raghav.cloud)  

**Credit:** 👉 [GitHub: bhumin-patel029](https://github.com/bhumin-patel029)

