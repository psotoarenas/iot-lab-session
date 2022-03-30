# IoT Lab session: Data analytics and machine learning in the cloud and edge for IoT

This repository is created for the IoT lab session on Data analytics and machine learning in the cloud and edge for IoT. It is composed from two session. During the first session, the students will have a brief introduction to cloud computing and how to containarize applications to be deployed in the cloud and in the edge. During the second session, the students will have also a brief introduction to machine learning, how to use pre-trained models for computer vision problems, and how to train models from a time-series data to forecast future values. 

## Containarized applications. 
The modules used during this session are within the folders helloworld and covid19_cases. During the theoretical part of the session, we will follow the getting started tutorial directly from docker. For that, it is highly recommended that the students have docker already installed and create a free account on docker hub. Then we will head to developing our first containarized application. The first example (helloworld) shows the differences between running your application locally at your computer and running an application inside a docker container. It is a really simple application but it allows to demonstrate the initial steps of developing application for the cloud. 

The second application (covid19_cases) is a dashboard-like application that displays some figures of the current situation of the covid19 pandemic in different countries around the world. This application is more complex than the first, but it follows the same patterns, showing the students the benefits of containers. This application also can be useful towards the final project. 

## Machine Learning
During this part of the session, the students will use [YOLOv4](https://github.com/AlexeyAB/darknet) to identify objects in images and videos. We will use an image and homemade video to test the efficiency of the pre-trained model. Afterwards we will see two algorthms for time-series forecasting. We will use an open dataset to predict a variable of interest in the future. The modules used during this session are under the folder time_series. There the students will find two jupyter notebooks each with the respective forecasting algorithm (SARIMA and GradientBoost). Additionally, the csv files that contain the dataset we will use. 

For yolo, we will use a VM in the cloud, colab more specifically. The jupyter notebook used during the session can be found in the YOLOv4 tutorials online.  


## Useful links

### Cloud Computing
1. Google. Google Cloud Topics: Learn the basics of cloud computing and how to get started. [https://cloud.google.com/learn 
](https://cloud.google.com/learn 
). Accessed: 01/03/2022.
2. AWS Public Sector. Cloud 101: An Introduction to Cloud Computing | AWS Public Sector. [https://youtu.be/GneIpdOirZY](https://youtu.be/GneIpdOirZY). Accessed: 01/03/2022.
3. TechWorld with Nana. Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours]. [https://youtu.be/X48VuDVv0do](https://youtu.be/X48VuDVv0do). Accessed: 01/03/2022.

### Containerized Applications
1. Docker. Docker Getting Started Tutorial. [https://github.com/docker/getting-started](https://github.com/docker/getting-started). Accessed: 01/03/2022. 
2. Docker. Docker for beginners [https://github.com/docker/labs/blob/master/beginner/readme.md](https://github.com/docker/labs/blob/master/beginner/readme.md). Accessed: 01/03/2022. --> Homework!
3. Mahbub Zaman. 12 Essential Docker Commands You Should Know. [https://towardsdatascience.com/12-essential-docker-commands-you-should-know-c2d5a7751bb5](https://towardsdatascience.com/12-essential-docker-commands-you-should-know-c2d5a7751bb5). Accessed: 01/03/2022.

### Python Dashboard
1. Meinhard Ploner. Visualise COVID-19 case data using Python, Dash, and Plotly. [https://towardsdatascience.com/visualise-covid-19-case-data-using-python-dash-and-plotly-e58feb34f70f](https://towardsdatascience.com/visualise-covid-19-case-data-using-python-dash-and-plotly-e58feb34f70f). Accessed: 01/03/2022.
2. Bee Guan Teo. Building A Real-time Dashboard Using Python Plotly Library And Web Service. [https://towardsdatascience.com/building-a-real-time-dashboard-using-python-plotly-library-and-web-service-145f50d204f0](https://towardsdatascience.com/building-a-real-time-dashboard-using-python-plotly-library-and-web-service-145f50d204f0). Accessed: 01/03/2022.
3. Anmol Tomar. Dash for Beginners : Python Dashboards. [https://towardsdatascience.com/dash-for-beginners-create-interactive-python-dashboards-338bfcb6ffa4](https://towardsdatascience.com/dash-for-beginners-create-interactive-python-dashboards-338bfcb6ffa4). Accessed: 01/03/2022.
4. World Health Organization. WHO Coronavirus (COVID-19) Dashboard. [https://covid19.who.int/](https://covid19.who.int/). Accessed: 01/03/2022.

### Machine Learning
1. DeepLearning.AI. Deep Learning Specialization with Andrew Ng. [https://www.coursera.org/specializations/deep-learning](https://www.coursera.org/specializations/deep-learning). Accessed: 29/03/2022

### YOLO
1. Aleksey Bochkovskiy. Yolo v4, v3 and v2 for Windows and Linux. [https://github.com/AlexeyAB/darknet](https://github.com/AlexeyAB/darknet)
2. Aleksey Bochkovskiy. YOLOv4 — the most accurate real-time neural network on MS COCO dataset. [https://alexeyab84.medium.com/yolov4-the-most-accurate-real-time-neural-network-on-ms-coco-dataset-73adfd3602fe](https://alexeyab84.medium.com/yolov4-the-most-accurate-real-time-neural-network-on-ms-coco-dataset-73adfd3602fe)
3. Joseph Redmon. Darknet: Open Source Neural Networks in C. [https://pjreddie.com/darknet/](https://pjreddie.com/darknet/)

### Containerized ML
1. Xavier Vasques. Build and Run a Docker Container for your Machine Learning Model. [https://towardsdatascience.com/build-and-run-a-docker-container-for-your-machine-learning-model-60209c2d7a7f](https://towardsdatascience.com/build-and-run-a-docker-container-for-your-machine-learning-model-60209c2d7a7f)
