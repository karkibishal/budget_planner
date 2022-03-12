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
    - [Planning](#planning)
  - [Risk Assessment](#risk-assessment)

## Introduction
This project is the final submission for the QA DevOps bootcamp. I have developed a webapp which can be used to track a user's expenses. The user can record their expense items and expense amount at particular dates under various expense categories. The user is able to view graphical representation of their expenses on the app home page. The app is served through a CI/CD pipeline to the end user. Microsoft azure resources were used to maintain the pipeline. The following sections of this document will go through the development stages of the app and the pipeline.

## Objectives
- To create a web application that integrates with a database and demonstrates CRUD functionality.
- To utilise containers to host and deploy your application.
- To create a continuous integration (CI)/continuous deployment (CD) pipeline that will automatically test, build and deploy your application

## Web Application

### Planning

![Jira Roadmap](images/jira.png)

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