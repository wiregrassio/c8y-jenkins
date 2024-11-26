docker run \
    -p 8080:8080 \
    -p 50000:50000 \
    -d \
    -v ~/jenkins_data:/var/jenkins_home \
    jenkins/jenkins:2.414.3-jdk17