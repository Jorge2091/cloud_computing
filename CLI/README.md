# What is disaster recovery 
Lost revenue of an unplanned downtime is estimated to cost around 2 billion pounds in the uk and Ireland. Another problem is that it brings a bad reputation to the business if an organization had suffered a data breach.
## What is S3

Amazon, as of 2015, offers Cross Region Replication for S3. which can reduce the rick of data lost if a region encounters a major disaster as one data will have the same name and metadata as the other.

<img src="https://miro.medium.com/max/580/1*DHe24MbDHtbkOeIJzxrfdA.png"/>

## how to configure S3

When creating to AWS, we are given a secret key, access key and so on, using this unique keys, we are able to connect to our machine in aws and also with this, we can make a S3 bucket.<br/>
All of this steps must be done inside the Virtual machine:
1. ssh to AWS VM
2. update and upgrade -y
3. install python3
```
sudo install python3
```
4. install pip
```
sudo install python3-pip
```
if required, check `python --version` and it should output python 3 and above, if not:
```
alias python=python3
```
5. install awscli using pip
```
sudo pip3 install awscli
```
6. configure aws
```
aws configure
```
and then fill in your unique access key, secret key, output=json, region=eu-west-1
