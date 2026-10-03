# AWS Infrastructure Monitoring & Alerting Platform

A hands-on AWS monitoring and alerting platform built to monitor EC2 infrastructure, visualize system metrics, and send email notifications when CPU utilization exceeds a defined threshold.

## 📌 Project Overview

This project demonstrates an end-to-end infrastructure monitoring solution using **Prometheus, Grafana, Node Exporter, AWS CloudWatch, and Amazon SNS**.

A Flask demo application is containerized using Docker and deployed on an AWS EC2 instance. Node Exporter collects infrastructure metrics, Prometheus scrapes and stores the metrics, and Grafana provides dashboards for visualization.

AWS CloudWatch monitors EC2 CPU utilization and triggers an alarm when CPU usage exceeds **70%**. Amazon SNS is used to deliver email notifications.

## 🏗️ Architecture

```text
                         AWS EC2
                    monitoring-server
                           │
             ┌─────────────┴─────────────┐
             │                           │
             ▼                           ▼
       Docker Containers            AWS CloudWatch
             │                           │
      ┌──────┴──────┐              CPUUtilization
      │             │                    │
 Flask App    Node Exporter              ▼
                    │              CloudWatch Alarm
                    ▼                 CPU > 70%
               Prometheus                 │
                    │                      ▼
                    ▼                  Amazon SNS
                 Grafana                    │
                    │                      ▼
                    ▼                  Email Alert
        CPU / Memory / Disk /
           Network Metrics
```

## 🛠️ Technologies Used

* **AWS EC2** – Cloud infrastructure
* **Docker** – Application and monitoring containerization
* **Node Exporter** – System metrics collection
* **Prometheus** – Metrics collection and monitoring
* **Grafana** – Metrics visualization and dashboards
* **AWS CloudWatch** – EC2 monitoring and alarms
* **Amazon SNS** – Email notifications
* **Linux / Ubuntu** – Server environment
* **Flask** – Demo application

## 🔍 Monitoring

Prometheus collects infrastructure metrics from Node Exporter, including:

* CPU utilization
* Memory utilization
* Disk utilization
* Network traffic

Grafana is connected to Prometheus and provides a dashboard named:

**AWS Infrastructure Monitoring**

The dashboard contains panels for:

* CPU Usage %
* Memory Usage %
* Disk Usage %
* Network Receive
* Network Transmit

## 🚨 Alerting

AWS CloudWatch monitors the EC2 instance's `CPUUtilization` metric.

The configured alarm:

```text
Alarm Name: EC2-High-CPU-monitoring-server1
Metric: CPUUtilization
Statistic: Average
Period: 5 minutes
Threshold: 70%
```

When CPU utilization exceeds the configured threshold, CloudWatch can trigger an Amazon SNS notification to the subscribed email address.

The alerting workflow was tested successfully using an SNS test notification.

## 🐳 Docker Containers

The monitoring environment used the following containers:

```text
monitoring-demo-app
node-exporter
prometheus
grafana
```

All monitoring components were connected through a Docker network.

## 📊 Grafana Dashboard

The Grafana dashboard provides a centralized view of EC2 infrastructure performance.

### Dashboard

![Grafana Dashboard](screenshots/05-grafana-dashboard.png)

## 📈 Prometheus Targets

Prometheus was configured to scrape the monitoring targets.

![Prometheus Targets](screenshots/03-prometheus-targets.png)

## ☁️ AWS CloudWatch Alarm

The EC2 CPU alarm was configured with a 70% threshold.

![CloudWatch Alarm](screenshots/07-cloudwatch-alarm.png)

## 📧 SNS Email Alert

The SNS notification workflow was tested successfully.

![SNS Email Alert](screenshots/08-sns-email-alert.png)

## 📁 Project Structure

```text
aws-infrastructure-monitoring-alerting/
│
├── app/
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
│
├── prometheus/
│   └── prometheus.yml
│
├── grafana/
│   └── dashboard/
│
└── README.md
```

## ⚙️ Key Prometheus Queries

### CPU Usage

```promql
100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

### Memory Usage

```promql
100 * (1 - (node_memory_MemAvailable_bytes / node_memory_MemTotal_bytes))
```

### Disk Usage

```promql
100 * (1 - (
  node_filesystem_avail_bytes{mountpoint="/",fstype!~"tmpfs|overlay"}
  /
  node_filesystem_size_bytes{mountpoint="/",fstype!~"tmpfs|overlay"}
))
```

### Network Receive

```promql
rate(node_network_receive_bytes_total{device!="lo"}[5m])
```

### Network Transmit

```promql
rate(node_network_transmit_bytes_total{device!="lo"}[5m])
```

## 🎯 Key Learning Outcomes

Through this project, I gained practical experience in:

* AWS EC2 infrastructure monitoring
* Docker containerization
* Prometheus metrics collection
* Grafana dashboard creation
* Node Exporter configuration
* AWS CloudWatch monitoring
* CloudWatch alarm configuration
* Amazon SNS email notifications
* Linux server administration
* Infrastructure observability and alerting

## 👨‍💻 Author

**Shaun John Mathew**

GitHub: [shaunjohn-04](https://github.com/shaunjohn-04)

LinkedIn: [Shaun John Mathew](https://linkedin.com/in/shaun-john-mathew)
