# Mastodon data analysis

Consuming mastodon's api to get data, applying mapreduce on the data and inserting it into hbase. Automizing this process using airflow.

## Table of Contents

- #introduction
- #prerequisites
- #getting-started
  - #installation
  - #usage
- #problems faced

## Introduction

In order to get familiar with Hadoop, Hbase and Airflow, we consumed Mastodon's api in order to get data. We used this data for analysis after we applied mapreduce on it.

## Prerequisites

Before executing the scripts in this repository, you have to have hadoop, hbase, airflow, python, java installed on your PC. Preferably you'd want to install all of those technologies on a virtual machine using ubuntu.

## Getting Started

As we mentioned in prerequisites, we installed :
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









