# Software Development Lifecycle (SDLC)
- Plan/Design
- Develop
- Test
- Deploy


# Continuous intergration and continuous delivery/deployment (CI/CD)
- In CI/CD the development, testing, and operations teams work collaboritively to implement productive workflows within the SDLC pipeline. 

![](../images/CICD.png)
- **Continuous intergration** - implementing small changes and check in code to version control repositories frequently
	- run automatic code quality scans on it and generate a report of how well latest changes adhere to good coding practices
	- build code and run any automated tests that you might have written to make sure changes don't break functionality
	- generating test coverage reports to observe how thorough automated tests are


- **Continuous delivery** - automate software release but final step of approving and initiating a deploy to production is done manually. Beneficial if your software release day is a year away, maybe you would like to test how it manages with a large volume of users
    - Advantages
        - Less pressure on decisions for small changes => faster iterating
        - Find and address bugs quicker before they become large problems, you can perfom additional and more comprehensive testing on code
- **Continuous deployment** - automating the deployment of applications to selected infrastructure environments. 
    - doing so in short cycles
    - Code done -> unit tests -> integrate -> acceptance test -> deploy to production (each step is automated)
    - Advantages
        - Customers see continuous stream of improvements every day
        - Releases are less risky & easier to fix if problem arises - smaller changes made
        - Develop faster, no need to pause development for releases, deployment is triggered automatically for every change

## CI/CD Pipeline
### CI
- Build 
- Testing
- Integration
### CD
- Review
- Staging 
- Production

## Benefits of CI/CD
- Reduce cost
- Faster release rate
- Smaller code changes
- Fault isolations
- More test reliability
- Increase team transparency and accountability
- Easy maintenance and updates

## Jenkins
- Jenkins is a **CI/CD server**, facilitates CI/CD by can buiding, testing and deploying software.
- You can set up Jenkins to watch for any code changes in places e.g **GitHub** and automatically do a build.
- You can utilize container technology such as **Docker**, initiate tests and then take actions like rolling back/forward in production.

## Docker
- Docker allows your to containerise your app, companies such as Paypal and Spotify use Docker.
- Allows you yo build a container imahe and use the same image across every step of the deployment process
- Separate non-dependent steps and run them in parallel
- Run apps in containers rather than VMs
- Run unit tests as part of your docker build command by adding a target for them in your Dockerfile. This way, as you are making changes and rebuilding locally, you can run the same unit tests you would run in the CI on your local machine using a simple command.
- Once you build docker image, you deploy it e.g Amazon EC2 container supports Docker images