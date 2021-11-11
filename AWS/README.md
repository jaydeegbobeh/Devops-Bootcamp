# What is Cloud Computing?
The delivery of computing service to offer faster innovation, flexible resources and economies of scales.

## Types of Cloud and their use cases
- Public Clouds
- Private Clouds
- Hybrid Clouds

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
### Regions
- AWS has several regions (physical location around the world where amazon clusters data centres) where you can create resources: each region has several availability zones (consists of one or more data centres at a location within an AWS region - each AZ has independent cooling, power and physical security
- If app is partitioned accross AZs, companies are better isolated/ protected from power outages, natural disasters (AZs within a region are separated within 100km from each other)
- Pick region (and AZ) thats geographically close to company/ customers:  lowest network latency and quickest response

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
- Security Groups `SG`
- Cloudwatch `CW`
- Simple Notification Service `SNS`
- Simple Que Service `SQS`
- Load Balancers `LB` - `ALB` - `ELB`- `NLB`
- Autoscaling Groups `ASG`
- Amazon Machine Image `AMIs`
    - Provides the information required to launch an instance
    - Contains an operating system (Linux, Unix, Windows) , application server (containers: mysql server, phpmyadmin server) and applications - software configuration, contains launch permissions that control which AWS accounts can use the AMI to launch instances


## Building an EC2 instance

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