# Setara - Bangkit 2024 Capstone Project

Setara (Sistem Rekomendasi Tenaga Kerja Inklusif) addresses workforce exclusion among individuals with disabilities in Indonesia, where only 2 in 5 are employed (BPS, 2023). This Android app uses machine learning to provide personalized job recommendations based on users' abilities, experiences, and locations. With cloud-based infrastructure and real-time job matching, Setara promotes inclusivity and accessibility in the workforce. Aligned with SDGs 8 and 10, it aims to reduce employment barriers, foster equality, and support Indonesia's goals of reducing unemployment and inequality (Kementerian PPN, 2023).

Theme: Health Innovation

### Team C242-PS372

- **Claudya Cindri Kasinda**: M002B4KX0948
- **Vridha Amalia Rozaq**: M002B4KX4446
- **Sausan Habiibah Mughni**: M002B4KX4087
- **Mohammad Farhan Fahrezy**: C002B4KY2567
- **Hirzy Fakhriadh Ardika Harnedi**: C002B4KY1791
- **Muhamad Faizal Yusuf**: A246B4KY2630
- **Lilis Apriah**: A246B4KX2272

## Machine Learning Learning Path

### Steps to Generate the Job Recommendation Model

1. **Open Google Colaboratory Notebook.** 
You can begin by opening a Google Colab notebook for this project. It will serve as your workspace for training and evaluating the job recommendation model. You can follow the notebook to implement the machine learning model using a deep neural network.
2. **Prepare and Upload the Dataset**
- Ensure you have the job_data.xlsx dataset containing the relevant features: Disability, Age Experience, City, and Job.
- Upload the dataset to your Colab environment for preprocessing and training the model.
3. **Data Preprocessing**
Use One-Hot Encoding to preprocess the categorical features, such as Disability, Age, Experience, and City. This will allow the model to better understand and process the input data for job recommendations.
4. **Model Training**
The model will be built using TensorFlow and Keras, leveraging a fully connected deep neural network. Train the model using the preprocessed dataset with the following key steps:
- Build the neural network architecture (e.g., with layers like Dense, Dropout).
- Compile the model using an optimizer like Adam and the categorical_crossentropy loss function.
- Train the model with the X_train and y_train sets, using validation data to monitor the model's performance.
5. **Save the Model**
After the model has been successfully trained, convert it into TensorFlow Lite format (job_recommendation_model.tflite) for mobile deployment.

### Featured Technologies

1. **TensorFlow**
The core open-source library used for developing and training machine learning models. TensorFlow provides robust tools and workflows to quickly build machine learning applications.
2. **TensorFlow Lite**
TensorFlow Lite is an open-source deep learning framework optimized for on-device inference, ideal for deploying machine learning models on mobile devices.
3. **Keras**
Keras is a high-level API, running on top of TensorFlow, that simplifies building and training deep learning models. It provides easy-to-use interfaces for implementing neural networks.

## Mobile Development Learning Path

## Cloud Computing Learning Path

### Deployment Steps

1. Clone the repository on virtual machine
```bash
git clone <repository-url>
cd <repository-name>
```
2. Pull the latest update
```bash
git pull origin main
```
3. Install dependencies
```bash
pipenv install
pipenv shell
```
4. Install PM2 and Nginx
```bash 
npm install -g pm2
sudo apt update
sudo apt install nginx
```
5. Set up reverse proxy with nginx
```bash
sudo ln -s /etc/nginx/sites-available/<your-config-file> /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```
6. Run database migrations
```bash
flask db upgrade
```
7. Run the flask application with PM2
```bash
pm2 start flask -- flask run
```

### Featured Technologies

1. **Flask**
A lightweight Python web framework used to build the backend API. Flask is simple yet powerful, allowing rapid development with features like routing, templating, and built-in development server.
2. **PostgreSQL**
A powerful, open-source relational database management system known for its reliability, scalability, and extensive feature set, used to manage and store application data.
4. **Nginx**
A high-performance web server and reverse proxy server used to route requests from the internet to the Flask backend while ensuring scalability and security.
5. **Google Cloud Platform (GCP)**
A comprehensive cloud computing platform that supports the deployment of virtual machines, database services, and scalable infrastructure for modern application development.


## Featured Technologies

- [Flask](https://flask.palletsprojects.com/)  
  A lightweight Python web framework used to build the backend API. Flask is simple yet powerful, allowing rapid development with features like routing, templating, and built-in development server.

- [PostgreSQL](https://www.postgresql.org/)  
  A powerful, open-source relational database management system known for its reliability, scalability, and extensive feature set, used to manage and store application data.

- [PM2](https://pm2.keymetrics.io/)  
  A production-ready process manager for Node.js applications, used to manage the Flask application in a scalable and efficient way, with built-in logging and process monitoring.

- [Nginx](https://www.nginx.com/)  
  A high-performance web server and reverse proxy server used to route requests from the internet to the Flask backend while ensuring scalability and security.

- [Google Cloud Platform (GCP)](https://cloud.google.com/)  
  A comprehensive cloud computing platform that supports the deployment of virtual machines, database services, and scalable infrastructure for modern application development.

- [Google Cloud SQL](https://cloud.google.com/sql)  
  A fully managed relational database service for PostgreSQL, providing automated backups, high availability, and easy integration with Flask applications.

- [Google Cloud Storage](https://cloud.google.com/storage)  
  A secure and scalable object storage service used to store static assets or files, ensuring high availability and performance.

- [Pipenv](https://pipenv.pypa.io/en/latest/)  
  A dependency manager for Python that simplifies the management of virtual environments and package installations, ensuring consistency across development and production environments.