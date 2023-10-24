# Mastodon data analysis

Consuming mastodon's api to get data, applying mapreduce on the data and inserting it into hbase. Automizing this process using airflow.

## Table of Contents

- #introduction
- #GDPR compliance
- #Requirements
- #getting-started
  - #installation
  - #usage
- #problems faced

## Introduction

This project is dedicated to the analysis of data from the Mastodon platform and aims to address various critical needs for the extraction, processing, and analysis of massive data. As a data developer, the mission is to establish an automated pipeline to tackle these complex challenges. This project responds to the necessity of extracting meaningful insights from raw Mastodon data, focusing on user analysis, content analysis, language analysis, media engagement, tags, mentions, and more. To achieve this, several key steps need to be followed, from raw data collection to in-depth analysis of the results. These needs define the framework of this Big Data project and will be detailed in the following sections.

#GDPR compliance

Ensuring GDPR compliance is paramount when working with data from Mastodon's API, performing MapReduce operations, and storing it in HBase, especially if this data involves personal information. GDPR, or the General Data Protection Regulation, mandates that any processing of personal data must adhere to strict data protection principles, which include transparency, data minimization, and security. To comply with GDPR, it is essential to obtain explicit consent from users whose data is being collected, and to handle the data with care throughout the entire pipeline. This entails anonymizing or pseudonymizing the data where possible, encrypting sensitive information, and maintaining a comprehensive record of data processing activities. Moreover, setting up access controls, audit trails, and regularly conducting Data Protection Impact Assessments (DPIAs) are critical steps to ensure GDPR compliance. In the context of Airflow automation, it's vital to include mechanisms for automatically managing data retention and deletion, further upholding individuals' right to be forgotten as per GDPR regulations. By prioritizing GDPR compliance, your project will not only be legally sound but also demonstrate a commitment to respecting user privacy and data protection.

## Requirements

Data Collection: Use the Mastodon API, store data in HDFS, and model the HDFS Data Lake.
MapReduce Processing: Mapper and reducer to transform and aggregate data.
MapReduce Job Execution: Utilize the Hadoop streaming API and monitor through the Hadoop Web interface.
Store Results in HBase: Design the HBase schema, create tables, and insert data.
Orchestration with Apache Airflow: Define a DAG, create tasks, and monitor through Airflow.
Results Analysis: Query data in HBase to extract information about users, content, language, media engagement, tags, and mentions.
Optimization and Monitoring: Optimize MapReduce scripts, monitor HBase, set up Airflow alerts, and monitor Hadoop.
Update Permissions and Documentation: Update API tokens, document roles, permissions, and access rules.
Scheduled Developments: Regularly schedule DAGs to keep data current.
GDPR Compliance: Document personal data, comply with GDPR regulations.

## Getting Started

As we mentioned in Requirements, we installed :
- hadoop : https://learnubuntu.com/install-hadoop/
- hbase : https://www.linkedin.com/pulse/how-install-apache-hbase-ubuntu-dr-virendra-kumar-shrivastava/
- airflow :https://hevodata.com/learn/install-airflow/#Installing-PIP
- it is recommended to use a virtual machine ( or wsl) on ubuntu.

### Installation

The instructions to install the technologies we used are provided in the links in #getting started.

### Usage

Use the scripts provided to consume mastodon's api and get data about users, followers, language etc. You'll need your proper keys to execute the code, you may generate them on mastodon's platform.
You can then apply mapreduce on the data collected depending on your needs, and then insert that data into Hbase and automize this whole process using airflow.

## Problems faced
permission denied : A pretty common problem we faced while working on this project, as we used ubuntu on a virtual machine, sometimes this error pop up whenever we wanted to start hadoop services, we solved this issue using the following commands : 

# ls -ld /home/hadoop

# sudo chown hadoop:hadoop /home/hadoop
# sudo chmod 700 /home/hadoop

# ls -l /home/hadoop/.ssh
# ls -l /home/hadoop/.ssh/authorized_keys

# sudo chown -R hadoop:hadoop /home/hadoop/.ssh
# sudo chmod 700 /home/hadoop/.ssh
# sudo chmod 600 /home/hadoop/.ssh/authorized_keys

# sudo service ssh restart

# eval $(ssh-agent)

# ssh-add ~/.ssh/id_rsa

# ssh hadoop@localhost

# sudo reboot

# chmod 600 ~/.ssh/id_rsa

# ssh-add ~/.ssh/id_rsa









