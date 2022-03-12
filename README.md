# Budget Planner
## Demo Video
[![App Demo](https://i.ytimg.com/vi/VVAD5VCRSAk/maxresdefault.jpg)](https://www.youtube.com/watch?v=VVAD5VCRSAk)
#
## Contents
- [Budget Planner](#budget-planner)
  - [Demo Video](#demo-video)
  - [Contents](#contents)
  - [Introduction](#introduction)
  - [Objectives](#objectives)
  - [Web Application](#web-application)
    - [Database](#database)
    - [Planning and development](#planning-and-development)
  - [CI/CD Pipeline](#cicd-pipeline)
    - [Infrastructure](#infrastructure)
    - [Pipeline](#pipeline)
  - [Risk Assessment](#risk-assessment)

## Introduction
This project is the final submission for the QA DevOps bootcamp. I have developed a webapp which can be used to track a user's expenses. The user can record their expense items and expense amount at particular dates under various expense categories. The user is able to view graphical representation of their expenses on the app home page. The app is served through a CI/CD pipeline to the end user. Microsoft azure resources were used to maintain the pipeline. The following sections of this document will go through the development stages of the app and the pipeline.

## Objectives
- To create a web application that integrates with a database and demonstrates CRUD functionality.
- To utilise containers to host and deploy your application.
- To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application

## Web Application
The application is a budget planner where user can keep a running record of their expenses. Each expense item is named and has an amount and date associated with it. The date and amount is useful to produce charts based on the expenses recorded. Each expense item, should also be categorised in an expense category so that the user can view expenses ocurred in each category. The user can also record their income in order to calculate their savings.

The following tools and technologies were used to develop the app:
- VSCode: IDE for coding
- Python: Programming language used
- Flask: Web framework used to develop the app
- MySQL: Database to store the entered data (Azure MySQL database was used)
- Version control: Git and github used as source control measures
  
### Database
![Current ERD](images/erd.png)<p align="center">Current ERD</p>
The database structure consists of 3 tables as shown in the ERD above. The income table is used to record the gross income along with any taxes and contributions. The taxes and contributions are subtracted from the gross income to calculate the take home pay which is also recorded in the table.

The category table records the expense categories and the expense table records the individual expense items. There is a one to many relationship between the category table and expense table.

The diagram below shows the ERD which was prepared at the beginning of the project. A few details have been changed as the project evolved. For example, I got rid of the updated at column from the category and expense tables as I felt there was was no use to record two separate time values.
![Old ERD](images/erd_old.png)<p align="center">Old ERD</p>

The database was created on Azure Database for MySQL. The database was configured to accept connections only from azure resources and the local development machine. Using the Azure database ensured that the data persisted on the azure server.

### Planning and development
![Jira Roadmap](images/jira.png)<p align="center">Jira Roadmap</p>
Jira was used to plan and keep track of the app development. User stories were developed to determine the functionalities of the app. Some of the user stories developed were as follows:
- As a user, I want to categorize my expenses, so that I can know where do I spend most
- As a user, I want to add my expense item, so that I can view them later
- As a user, I want to edit my expenses, so that I can rectify mistakes
  
Each user story was assigned a story point estimate and then assigned to an epic. Sprints were conducted lasting 1 week each and where the story points were assigned to the sprints. The backlog of the remaining issues was cleared with each sprint session.

## CI/CD Pipeline

### Infrastructure

### Pipeline


## Risk Assessment
| Description                                 | Evaluation                                             | Likelihood | Impact | Responsibility       | Control Measures                                                   | Response                                                      |
|---------------------------------------------|--------------------------------------------------------|------------|--------|----------------------|--------------------------------------------------------------------|---------------------------------------------------------------|
| Azure resources  malfunctioning             | App cannot be deployed through  azure                  | Low        | High   | Microsoft            | Backup code to VCS and transfer to another provider                | Move to another  cloud provider                               |
| Exposing logins and secrets on  remote repo | Database and forms can be accessed by unwanted parties | Medium     | High   | Bishal               | Use environmental variables throughout the code                    | Change the login details and secrets of compromised entities  |
| Failed jenkins  pipeline builds             | App fails to deploy                                    | Medium     | High   | Bishal               | Test individual build steps independently in local machine and VMs | Debug the failed build step                                   |
| Failed docker  swarm deployment             | App cannot be deployed                                 | Low        | High   | Bishal               | Test docker stages independently in VM                             | Debug docker stage                                            |
| Cannot connect to  Azure MySQL database     | Database cannot be accessed                            | Low        | High   | Microsoft and Bishal | Connection details stored as environment variables                 | Check for errors in login details, connection url             |
| No connection to nginx load balancer        | App cannot be accessed                                 | Low        | High   | Bishal               | Use public ip of docker swarm nodes in nginx as  a backup          | Check private and public  ip addresses of  docker swarm nodes |
| Source code changes breaking the app        | App cannot be used                                     | Medium     | High   | Bishal               | Use testing to cover most code                                     | Revert to most recent working version                         |