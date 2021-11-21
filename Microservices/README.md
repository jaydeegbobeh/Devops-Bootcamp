# Microservice
- Microservice
Consists of a collection of small, autonomous services, each service is self-contained.
- Advantages	
	- Microservices are deployed independently => easy to manage bug fixes and feature releases
	- Compared to monolithic application, code dependencies can become tangled adding a new feature requires editing code in many places, in a microservice you don't share code or data stores, minimising dependencies making it much easier to add new features.
	- You can use different technologies that fit your microservice
	- If a microservice becomes unavailable this does not distrupt the entire app
	- Microservices can be scaled independently from each other
- Disadvantages
	- There are lots of moving parts compared to monolithic applications, the system is more complex
	- Teams may use many different languages/frameworks meaning the app as a whole is difficult to maintain


## Kubernetes
- Kubernetes aka K8S is a container orchestration system perfect for automating the management, scaling and deployment of microservice applications
- Advantages:
	- Self healing
	- Load balancing and service discovery
	- Automated rollouts and rollback
	- Autoscaling
## Using Kubernetes to deploy Node app and Mongodb as microservices
### Definitions
- **Pods**: the smallest deployable units of computing that you can create and manage in Kubernetes
- **Service**: a service enables network access to a set of Pods in Kubernetes.
- **Persistent** volume claim: a request for storage, this is met by binding the PVC to a persistent volume
- **Deployment**: deployments represent a set of multipe, identical Pods. A Deployment runs multiple replicas of your application and automatically replaces any instances that fail or become unresponsive
#### mongo-service.yml
```
# This is a MongoDB service that is used by the other pods in the cluster to find and connect to MongoDB
apiVersion: v1
kind: Service
metadata:
  labels:
    name: mongo
  name: mongo
spec:
  ports:
    - port: 27017
      targetPort: 27017

```
- `kubectl create -f mongo-service.yml`
- `kubectl get svc`, show current services
#### mongo-pvc.yml
```
# Create a persistent volume claim
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: mongo-db
spec:
  # storageClassName: manual
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: 256Mi

```
- `kubectl create -f mongo-pvc.yml`
- `kubctl get pvc` show pvcs
#### mongo-deploy.yml

```
# MongoDB instance that runs the Database
---
apiVersion: apps/v1
kind: Deployment
metadata:
  name: mongo

spec:
  selector:
    matchLabels:
      app: mongo
  replicas: 1
  template:
    metadata:
      labels:
        app: mongo
    spec:
      containers:
      - name: mongo
        image: mongo
        ports:
          - containerPort: 27017
        volumeMounts:
          - name: mongo-persistent-storage
            mountPath: /data/mongo
      volumes:
        - name: mongo-persistent-storage
          persistentVolumeClaim:
            claimName: mongo-db

```
- `kubectl create -f mongo-deploy.yml`
- `kubectl gets pods`, show pods and their status
- `kubectl get deploy mongo`, show deployments
#### node-service.yml
```
apiVersion: v1
kind: Service

metadata:
  name: node
  namespace: default

spec:
  ports:
  - nodePort: 30001
    port: 3000
    protocol: TCP
    targetPort: 3000
  selector:
    app: node
  type: NodePort

```
- `kubectl create -f node-service.yml`
#### node-deploy.yml
```                                                 
apiVersion: apps/v1

kind: Deployment
metadata:
  name: node
spec:
  selector:
    matchLabels:
      app: node
  replicas: 1
  template:
    metadata:
      labels:
        app: node
    spec:
      containers:
        - name: node
          image: jaydeegb23/devops-bootcamp:v2

          ports:
            - containerPort: 3000
          env:
            - name: DB_HOST
              value: mongodb://mongo:27017/posts
          imagePullPolicy: Always
```
- `kubectl create -f node-deploy.yml`
- `kubectl exec "node-pod-name" env node seeds/seed.js`, seed database to node app
- load node app: localhost:30001
- load mongodb: localhost:30001/posts
