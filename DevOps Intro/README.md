# DevOps Intro
DevOps = Dev (development) + Ops (operations)
![](../images/devops_loop.webp)
## Life before DevOps
- Separate departments worked on different sides of a project
- Developers planned, designed and built the system before passing it over to the operations team for testing and implementation

### The problem
- Often a delay between the development and full implementation because of this separation between dev and ops
    - If there was something that needed to be reconfigured/ bug found/ not meeting user requirements, operation team would have to pass it back to development with the feedback and wait for updates
- Creates a blame culture  
## Why DevOps
- Devops expects people to make mistakes and is designed to allow these mistakes to be identified early on in the cycle and corrected before they make it any further => a blameless culture
- Software development lifecycle is shorter and more simple
- Developers and operations collaborate to deploy code to production faster in an automated/repeatable way
- Shorter + more simple #= faster = reduced costs

## Key pillars of DevOps
1. Customer-Centric action - focus on the customer needs
    - Use 'user stories' to plan your sprints, make sure you meet these requirements
2. End-To-End Responsibility - provide performance support from the beginning to the end of the life cycle
3. Continuous Improvement
4. Automate everything - everything as code: testing, application environment, version control
5. Work as one team
6. Monitor and test everything

## Stages in DevOps Lifecycle
- Continuous Development
- Continuous Testing
- Continuous Integration
- Continuous Deployment
- Continuous Monitoring

## Monolith Architecture
Traditional unified model for the design of a software program, software is composed all in one piece.

## N-tier (Front and back end)
- Separates the concerns between the visual elements of the app that the user will interact with (front end) and the building of the structure of the app (back end).
	- Front end - in which the user will see and deal with.
	- Back end – you have the software that will serve on the server and the database. This is where the DevOps team are.
## Microservice
- Consists of a collection of small, autonomous services, each service is self-contained.
- Advantages	
	- Microservices are deployed independently => easy to manage bug fixes and feature releases
	- Compared to monolithic application, code dependencies can become tangled adding a new feature requires editing code in many places, in a microservice you don't share code or data stores, minimising dependencies making it much easier to add new features.
	- You can use different technologies that fit your microservice
	- If a microservice becomes unavailable this does not distrupt the entire app
	- Microservices can be scaled independently from each other
- Disadvantages
	- There are lots of moving parts compared to monolithic applications, the system is more complex
	- Teams may use many different languages/frameworks meaning the app as a whole is difficult to maintain
