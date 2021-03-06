# What is Cloud Computing?
The delivery of computing service to offer faster innovation, flexible resources and economies of scales.

## Types of Cloud and their use cases
- Public: owned and operated by a 3rd party, rent access to cloud - AWS, Microsoft Azure, Google.
- Private: used exclusively by a business and it's usually located witin the company (e.g bank ,government) or they might rent space at a provider for their own server.
- Hybrid: some resources on public and some on private e.g Netflix.

## Who's using it?
- Netflix
- Google
- McDonalds
- Spotify

## Benefits of Using Cloud Computing
- Reduced IT costs
- Scalability
- Collaboration efficiency
- Flexibility of work practices


## What is AWS?
- Comprehensive evolving cloud computing platform provided by Amazon
- Includes mixture of:
    - infrastructure as a service (IaaS)
    - platform as a service (PaaS)
    - software as a service (SaaS)

- AWS services can offer an organization tools such as compute power, database storage and content delivery services

## AWS Global Infrastructure
The AWS Cloud spans 81 Availability Zones within 25 geographic regions around the world.
![](../images/aws-global-infr.PNG)
### Regions
- AWS has several regions (physical location around the world where amazon clusters data centres) where you can create resources: each region has several availability zones (consists of one or more data centres at a location within an AWS region - each AZ has independent cooling, power and physical security
- If app is partitioned accross AZs, companies are better isolated/ protected from power outages, natural disasters (AZs within a region are separated within 100km from each other)
- Pick region (and AZ) thats geographically close to company/ customers:  lowest network latency and quickest response

![](../images/aws-az.png)
### Data centres
- Each region has at least 2 data centres, means its highly available
    - If one data centre becomes unavailable there is a backup

## AWS services
- Elastic Compute Service `EC2`
    - A web service that provides; secure, resizable computer capacity in the cloud, designed to make web-scale cloud computing services easier: with choice of processor, storage, networking, operating system.
- Simple Storage `S3`
    - Object storage service built to store and retrieve any amount of data from anywhere.
- Virtual Private Network `VPC`
    - VPC is the networking layer for Amazon EC2 and enables launching AWS resources into a virtual network that you've defined.
        - Internet Gateway `IG`
            - Internet gateway = gateway you attach to your VPC to enable communication between resources (VPC and internet)
        - Route Tables `RT`
            - Route table: set of rules (routes)determines where network traffic is directed - routes to particular network destinations
        - Subnets `sn`
            - Subnet: the range of IP addresses in your VPC/ virtual network
        - VPC endpoints enables private connections between your VPC and AWS services e.g a S3 bucket (gateway)
        - CIDR block: how you define subnet mask, specify the range of IP addresses for the VPC

- Network Access Control `NACLs`
    - Optional layer of security for your VPC that acts as a firewall for controlling traffic in and out of one or more subnets
- Security Groups `SG`
    - Acts as a virtual firewall for EC2 instances to control incoming and outgoing traffic. 
- Cloudwatch `CW`
    - A monitoring and observability service for DevOps engineers, developers etc. Provides you with data and insights to monitor applications, respond to system-wide performance changes, optimize resource utilization and get unified view of operational health
- Simple Notification Service `SNS`
    - A messaging service for both application-to-application and application-to-person communication
- Simple Que Service `SQS`
    - message queing service that allows you to decouple and scale microservices, distributed systems and serverless apps
- Load Balancers `LB` - `ALB` - `ELB`- `NLB`: The load balancer distributes incoming traffic across multiple targets, e.g Amazon EC2 instances. Increases the availability of your application. Add one or more listeners to your load balancer. A load balancer distributes incoming app traffic across multiple EC2 instances in multiple Availability Zones - increases the fault tolerance of your applications.

    - `ALB`: Application Load Balancer, operates at the request level (layer 7), routing traffic to targets- EC2 instances, containers, IP adds, based on the content of request.
        - Ideal for advanced load balancing of HTTP and HTTPS traffic.
    - `ELB`: Elastic Load Balancing, automatically distributes incoming application traffic accross multiple targets and virtual apps in one or more AZs
    - `NLB`: Network Load Balancer, functions at 4th layer (Transport), can handle millions of requests per second. After load balancer receives connection requests, it selects a target from the target group for the default rule. Then attempts to open a TCP connection to the selected target on the port specified in the listener configuration.
- Autoscaling Groups `ASG`
    - Contains a collection of Amazon EC2 instances, treated as a logical grouping for the purposes of automatic scaling and management.
- Amazon Machine Image `AMIs`
    - Provides the information required to launch an instance
    - Contains an operating system (Linux, Unix, Windows) , application server (containers: mysql server, phpmyadmin server) and applications - software configuration, contains launch permissions that control which AWS accounts can use the AMI to launch instances


## Building an EC2 instance for app

1. Choose an Amazon Machine Image (AMI)
    - Ubuntu Server 16.04 LTS (HVM), SSD
2. t2 microservice
3. Add EBS volume
    - An Amazon EBS volume is a durable, block-level storage device that you can attach to your instances. After you attach a volume to an instance, you can use it as you would use a physical hard drive.
4. Ports:
    - SSH, TCP, 22
    - HTTP, TCP, 80
    - App, TCP, 3000
5. Connect to instance
    - Add private key file to `~/.ssh`
    - `chmod 400 privatekey`
    - Connect to instance using `ssh -i`
6. Set up environment
    - update and upgrade system
    - install nginx
    - nginx enabled
    - check the public IP globally 
    - install node correct verison
    - install required dependencies
    - `app code` currently available on `local host` => must migrate it to cloud
        - `scp -i ./key.pem -r /local/host/path/ name@ipv4.compute.amazonaws.com:/instance/path/`
    - `npm install`
    - `npm start`
    - Reverse proxy
        - `sudo rm -rf /etc/nginx/sites-available/default`
        - `sudo mv ./edited_default_file /etc/nginx/sites-available/`
        - `sudo systemctl restart`
        - `sudo systemctl enable nginx`
        - `sudo systemctl status nginx`
        - `npm start`
        - access IP address without :3000 

## Building an EC2 instance for Mongodb - pseudo coding

1. Build EC2 instance as shown above
    - SSH 22 and port 27017 for security group
2. Update mongod.conf with:
```
# network interfaces
net:
  port: 27017
  bindIp: 0.0.0.0
  ```
3. 
    - `sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv D68FA50FEA312927`
    - `echo "deb https://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list`
    - `sudo apt-get update -y`
    - `sudo apt-get upgrade -y`
    - `sudo apt-get install mongodb-org=3.2.20 -y`
    - `sudo apt-get install -y mongodb-org=3.2.20 mongodb-org-server=3.2.20 mongodb-org-shell=3.2.20 mongodb-org-mongos=3.2.20 mongodb-org-tools=3.2.20`
    - `sudo systemctl restart mongod`
    - `sudo systemctl enable mongod`
- **SSH back into app instance**
4. Go back to app instance `sudo echo 'export DB_HOST="mongodb://ip:27017/posts"' >> ~/.bashrc`
    - `source ~/.bashrc`
5. `node app/app/seeds/seed.js`
6. `npm start`


## Amazon Machine AMI
- Which OS, distro version
- Dependencies
- VPC Networking - SG - or Rules
- If you save the AMI of your instance it means you can easily relaunch it at anytime

### Create an AMI
- Select the instance you wish to create an image of > Actions > Image and templates > Create an image > Launch 
- t2 microservice
- Select storage
- Select SG 

## Monitioring
![](../images/Monitoring_Diagram.png)
- What you monitor depends on the architecture: What resources? How often we monitor? What tools perform there tasks? Who performs? Who should be notified in an emergency? What action should be taken?
- Application server -EC2
- CPU utilisation, %
- Number of requests - response time - latency 
- Firewall

### Four Golden Signals of Monitoring
- **Latency**: time it takes to service a request e.g HTTP 500 error trigered due to loss of connection to a database
- **Traffic**: measure of how much demand is being placed on your system e.g HTTP requests sec<sup>-1</sup>
- **Errors**: rate of requests that fail, HTTP 500s or HTTP 200 auccess response coupled with wrong content, is your system failing?
- **Saturation**: how 'full' your service is, measure of your system fraction - shows what resources are most constrained (e.g CPU, memory)

### Actions to be taken when alarm goes off/ notification is sent
- Lambda: automatically monitors Lambda functions on your before and reports metrics through Amazon CloudWatch 
- SQS: message queing service that enables you to decouple and scale microservices, distrobuted systems and serverless apps. SQS and CloudWatch are integrated so you can use CloudWatch to view/ analyse metrics 
- HTTP/S
- Email
- SMS
### Enabled detailed monitoring
To enable detailed monitoring for an existing instance:

1. Open the Amazon EC2 console at https://console.aws.amazon.com/ec2/.

2. In the navigation pane, choose Instances.

3. Select the instance and choose Actions, Monitoring, Manage detailed monitoring.

4. On the Detailed monitoring detail page, for Detailed monitoring, select the Enable check box.

5. Choose Save.

### Automate the processes
- Application Load Balancer (ALB)
- Autoscaling Group
- Launch template config: how many instances we would like to run at all times
    - e.g 2 instances provide min=2 and max=3
- Policies of scaling out - and scaling in to meet minimum instances
-  Scaling or Demand?
    - Scaling up vs scaling out
    - Scaling up: increasing the size of your instance
    - Scaling out: adding more components (instances) in parallel to spread out a load

## AWS CLI, Command Line Interface
- A unified tool to manage your AWS services.
- With just one tool to download/ configure.
- Possible to control multiple AWS services from the command lie and automate them through scripts

### To create AWS CLI:
- AWS access and secret keys
- Update/upgrade: 
    - `sudo apt-get update -y` 
    - `sudo apt-get upgrade -y`
- Dependencies: python 3 
    -`sudo apt-get install python`
    - `sudo apt-get install python-pip`
    - `sudo apt-get install python3-pip -y` 
    - `alias python=python3`
- CLI: `sudo pip install awscli`
- `aws configure`, enter your access key, secret key, default region name: `eu-west-1`, default output format: `json`
- S3 access through our IAM role/account
- **CRUD: Create (Bucket) - Read - Update - Delete**
- Create a bucket `aws s3 mb s3://bucket-name` OR specify region `s3 mb s3://bucket-name --region eu-west-2`
- Upload file from machine to bucket:
    - create file `vi test.md`
    - `aws s3 cp test.md s3://bucket-name/`
- Copy file from bucket to machine:
    - `aws s3 cp s3://bucket-name/test.md ./`
    - `aws s3 sync s3://bucket-name/test.md ./`
- Delete bucket
    - Delete file `aws s3 rm s3://bucket-name/test.md`
    - Delete bucket `aws s3 rb s3://bucket-name --recursive` OR `aws s3api delete-bucket --bucket bucket-name`

## AWS S3, Simple Storage Service
- Storage service, built to store and retrieve any amount of data, anytime, anywhere on the web
- Bucket: container for objects stored in S3
- Object: entities that is stored in S3 bucket, consists of object data/ metadata
- Key: unique identifier for object within bucket
- Attach a S3 server to an EC2 instance so that if we ever destroy the instance all the data will be saved.
- S3 Storage classes:
    - S3 Standard- high durability, performance object storage for frequently accessed data. Delivers low latency and high throughput (rate at which something is processed). Can be used for cloud apps, mobile/gaming apps
    - S3 Glacier- secure, durable, low-cost storage class for data archiving.

## S3 Task
- s3_env
## Autoscaling and Load Balancing
### Application Load Balancer
- Autoscaling automatically adjusts the amount of computational resources based on the server load
- Load Balancing distributes traffic between EC2 instances so that no one instance gets overwhelmed
**Requirements**
- ASG: Launch template or launch configuration
- ALB: Target group HTTP 80
- AWS keys
- VCPC - Subnets - SG
- Type of instance
- AMI-id
- EBS storage
**Highly Available in Multiple AZs**
- eu-west-1 (Ireland) instance
- eu-west-2 (London) instance
- eu-west-3 (Paris) instance

### Autoscaling group to lauch Node app
- Create template
- Select provide guidance
- Chose your AMI for node, then DB
- User data: add script to update, upgrade, install dependencies
- Create Autoscaling group 
    - Choose launch template
    - Choose instance launch options (vpc, availability - eu-west-1a, 1b, 1c)
    - Load balancing: attach to new load balancer, application load balancer
    - Enable group metrics
    - Desired capacity:3, min cap:2, max cap:3
    - Scaling policies: target tracking, CPU, target val:30
    - Add SNS
    - Remember to add listeners as your application requires e.g port 3000
    
## AWS Networking - Virtual Private Cloud (VPC)
VPC is the networking layer for Amazon EC2 and enables launching AWS resources into a virtual network that you've defined.
- An **internet gateway (IG)** (VPC component that allows communication between your VPC and the internet) must be attached to the vpc for internet availability inside this isolated virtual network
- **Route table (RT)**: set of rules (routes)determines where network traffic is directed - routes to particular network destinations.
- **Subnet (sn)**: the range of IP addresses in your VPC/ virtual network
- VPC endpoints enables private connections between your VPC and AWS services e.g a S3 bucket (gateway)
- **CIDR block**: how you define subnet mask, specify the range of IP addresses for the VPC

### Create a VPC
![](../images/VPC.png)
1. VPC CIDR block 10.107.0.0/16
2. Internet gateway
    - Attach IG to VPC
3. Create Route table:
    - Allow CIDR block 
    - Allow IG (0.0.0.0/16) - allow all
4. Public subnet (10.107.1.0/24) for Node-app 3000
    - In line with CIDR block
    - Connect to VPC
    - Create sg, allows ssh (from my ip), port 3000 (listen), port 80 (reverse proxy)
5. Private subnet 10.107.2.0/24 - Mongodb 27017
    - Connect to VPC
    - Create sg, allows ssh (from my ip), port 27017 (allows access from sg of node app)

6. Associate public subnet to our RT
7. SG public and private w/ required rules for pub and private subnets
8. Create instances from AMIs for node app and db
    - Remeber to use the vpc, sg groups you have created!
    - When configuring the IP address of your db, use the private subnet IP: this makes sure your db server is **not publically accessible**


Testing VPC config for public subnet and SG for app

### NACL







