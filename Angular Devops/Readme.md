# Building a Secure, Monitored, and Efficient Angular App Deployment Pipeline
## Introduction
Welcome to the showcase of my DevSecOps pipeline for an Angular-based application. This blog highlights the integration of various tools and technologies to ensure a secure, efficient, and continuously monitored deployment process. Below, I outline the key components of the pipeline, demonstrating my skills and the project's comprehensive nature.

## Project Overview
- **App Repository**: [angular-portfolio](https://github.com/krishchadha/angular-portfolio.git)
- **Live Website**: https://www.krishchadha.online
- **Jenkins**: An open-source automation server for CI/CD.
- **Docker**: For Sonarqube, prometheus and grafana.
- **Docker Hub**: Containerization of the Angular app.
- **AWS S3**: Static website hosting.
- **Slack**: Notifications for build and deployment status.
- **OWASP ZAP**: Security testing.
- **SonarQube**: Code quality and security analysis.
- **Google Analytics**: Tracking website usage.
- **Cloudflare**: DNS management and SSL.
- **Prometheus** and **Grafana**: Monitoring and visualization.

## Visual Workflow Diagram

![Screenshot 2024-07-06 001225](https://github.com/krishchadha/Devop_projects/assets/30497676/4f5a5868-729c-48f9-b034-2dc742c5cefd)

<img width="2457" alt="Untitled (1)" src="https://github.com/krishchadha/Devop_projects/assets/30497676/42244d5f-d08c-4d7a-969d-788fc5509d2d">


This diagram illustrates the workflow from code commit to deployment, showcasing the interaction between Jenkins, Docker, OWASP ZAP, SonarQube, AWS S3, and Slack.

Metrics and Results
Build Time Improvement:

Initial build time: 7 minutes 16 seconds
Optimized build time: 5 minutes 52 seconds

Code Quality Scores:

- Initial SonarQube Bugs: 2
- - Current SonarQube score: 0
  - 
- Initial SonarQube CodeSmell: 14
- Current SonarQube CodeSmell: 6

Security Vulnerabilities:
- Initial vulnerabilities: 3
- Current vulnerabilities: 0


## Jenkins for CI/CD
![image](https://github.com/krishchadha/Devop_projects/assets/30497676/406a2132-6eb1-4b5c-aef6-ce2c26ece014)

Jenkins is the backbone of our continuous integration and continuous deployment (CI/CD) pipeline. It orchestrates the entire workflow, from code commits to deployment, ensuring a seamless and automated process. Jenkins allows for the integration of multiple tools and scripts, making it an indispensable part of the pipeline.

Why Jenkins?

- Automation: Automates build, test, and deployment processes.
- Integration: Supports numerous plugins for seamless integration with other tools.
- Efficiency: Reduces manual intervention, speeding up the deployment process.

## Docker for Containerization

![image](https://github.com/krishchadha/Devop_projects/assets/30497676/6361f92b-a097-4f03-bbda-3697f68e18f8)

Docker plays a crucial role in containerizing the Angular application, ensuring consistency across different environments. By containerizing the app, we can avoid the "it works on my machine" problem and ensure the app behaves the same way in development, testing, and production.

Docker was also used for containerization of the angular app, creating different versions,and to build code.

Why Docker?

- Consistency: Provides a consistent environment across various stages of development.
- Isolation: Isolates the application, ensuring dependencies and configurations do not conflict.
- Scalability: Makes it easier to scale the application as needed.

##AWS S3 for Static Website Hosting
![image](https://github.com/krishchadha/Devop_projects/assets/30497676/01638d32-6b67-406f-90a4-f6f2a707ab2c)

AWS S3 is used to host the static Angular website. S3 provides a highly durable and available storage infrastructure that allows for the efficient delivery of the website content.

Why AWS S3?
- Scalability: Automatically scales to meet traffic demands.
- Cost-Effective: Only pay for what you use, making it a cost-effective solution.
- Reliability: High durability and availability ensure the website is always accessible.

## Slack for Notifications
![image](https://github.com/krishchadha/Devop_projects/assets/30497676/3ee37643-d8c4-4e3d-9407-65642b582cda)

Integrating Slack with Jenkins allows for real-time notifications about the build and deployment status. This ensures the team stays informed about the pipeline's health and can quickly address any issues.

Why Slack?

- Real-Time Communication: Provides instant notifications about build status.
- Team Collaboration: Enhances team collaboration and response time to issues.
- Customizable Alerts: Allows for customizable notifications based on specific events.

## OWASP ZAP for Security Testing
![image](https://github.com/krishchadha/Devop_projects/assets/30497676/766348f0-c888-4359-a596-f34a5780aa6c)

Security is paramount, and OWASP ZAP helps identify vulnerabilities in the application. By integrating ZAP into the Jenkins pipeline, we can automate security testing and ensure the application is secure before deployment.

Why OWASP ZAP?

- Automated Security Testing: Integrates seamlessly into the CI/CD pipeline for automated security checks.
- Comprehensive Coverage: Provides extensive security testing capabilities.
- Open Source: A free and widely-used security tool.

## SonarQube for Code Quality and Security Analysis
![image](https://github.com/krishchadha/Devop_projects/assets/30497676/0d9c4177-dd98-467f-a316-5da663daf3fe)

SonarQube is used to analyze the code quality and identify potential security issues. Integrating SonarQube with Jenkins ensures that code quality is continuously monitored and improved.

Why SonarQube?

- Code Quality: Ensures high code quality by identifying issues and suggesting improvements.
- Security: Detects security vulnerabilities in the code.
- Continuous Monitoring: Provides continuous code analysis and feedback.

## Google Analytics for Tracking
![image](https://github.com/krishchadha/Devop_projects/assets/30497676/39270c8c-4836-4462-856e-8688d565f876)

Google Analytics is integrated into the Angular application to track user interactions and gather valuable insights. This helps in understanding user behavior and improving the application's performance.

Why Google Analytics?

- User Insights: Provides valuable insights into user behavior.
- Performance Tracking: Helps in tracking the performance of the application.
- Data-Driven Decisions: Enables data-driven decisions for improving the application.

## Cloudflare for DNS and SSL
![image](https://github.com/krishchadha/Devop_projects/assets/30497676/0a9ba9ba-3a0b-4e94-ac6e-15629b05319f)

Cloudflare manages DNS and SSL for the website, ensuring fast and secure access. It provides robust security features and enhances the website's performance by caching content and providing DDoS protection.

Why Cloudflare?

- Security: Offers SSL encryption and DDoS protection.
- Performance: Improves website performance through caching and content delivery optimization.
- Reliability: Provides reliable and fast DNS resolution.

## Prometheus and Grafana for Monitoring
![image](https://github.com/krishchadha/Devop_projects/assets/30497676/d475aaeb-b4d5-4d43-8eaf-43ae77b143af)

![image](https://github.com/krishchadha/Devop_projects/assets/30497676/caee04ca-9263-463a-89cb-bc9bafd8a035)

Prometheus and Grafana are used to monitor the Jenkins pipeline, providing valuable metrics and visualizations. This helps in keeping track of the pipeline's performance and identifying any issues early.

Why Prometheus and Grafana?

- Metrics Collection: Prometheus collects detailed metrics about the pipeline.
- Visualization: Grafana provides powerful visualizations for better understanding of the metrics.
- Alerting: Allows for setting up alerts to notify about potential issues.

## Challenges and Learnings
Implementing this pipeline was not without its challenges. Configuring Jenkins to integrate with all the tools seamlessly required meticulous setup and troubleshooting. Ensuring Docker containers worked consistently across different environments also posed a challenge. Security testing with OWASP ZAP needed careful configuration to avoid false positives and ensure meaningful results.

Despite these challenges, the process was enriching. It provided valuable learnings about automating and securing the deployment pipeline, integrating various tools, and monitoring the system effectively.

## Conclusion
Building this DevSecOps pipeline has been a transformative experience. It has equipped me with the skills to automate, secure, and monitor deployments effectively. The integration of Jenkins, Docker, AWS S3, Slack, OWASP ZAP, SonarQube, Google Analytics, Cloudflare, Prometheus, and Grafana has resulted in a robust and efficient pipeline, ensuring the Angular application is always in top shape.

Check out the live website at https://www.krishchadha.online and explore the GitHub repository for more details.

Feel free to reach out if you have any questions or feedback!
