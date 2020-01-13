# Random Exercise Generator
This is a simple web application to generate random exercises for a user to complete when they do not know how they should workout. This has been made following the criteria needed for the SFIA project due in on Monday 13 January 2020 at the QA Consulting Academy. This brief will highlight the planning, design, creation, testing and deployment processes used during this project.

Presentation:   <br/>
Trello:   <br/>
Website:  <br/>


## Index
[Brief](#brief)
   * [Solution](#solution)
   * [User Stories](#userstories)
   * [User Cases](#usercases)
   * [Trello](#trello)
   * [Risk Assessment](#risk)
   
[Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)
	
    
[Deployment](#depl)
   * [Technologies Used](#tech)
   
[Testing](#testing)
     

[Improvements for the Future](#improve)

[Authors](#auth)

<a name="brief"></a>
## Project Brief
The project brief listed a number of goals to achieve, these are as follows:
* Plan the project using a Kanban board, including any risks and issues encountered
* An integrated VCS that can be built through a CI server and deployed to a cloud-based VM, making use of web-hooks to achieve this. 
* Service-oriented architecture using Python Flask
   * This should consist of four services: Two which generate random objects, one which combines said random objects and a fourth to host the Flask application
   * An SQL database should be used to store some information
   * Different implementation of the project must be able to be switched between without website downtime
* Containerisation of each service with Docker
* Ansible playbook to provision the environments that the application needs to run



<a name="solution"></a>
### Solution

This application is designed to allow users to log in and randomly generate a an exercise and number of reps for when they do not know how best to workout. A second implementation is available for when user wish to increase the difficult of the exercises, although currently this is only modifiable through the app; ideally this would be editable by a user. 

<a name="userstories"></a>
### User Stories

Below are entailed a series of user stories according to the planned uses for the application and their level of requirement according to a MoSCoW (Must, Shoud, Could, Would) scale. Note that some of these were considered 'stretch goals' and so have not been completed, although may be completed in the future, so please check in later to see if some of these exciting features have been added!

|  | User Stories and their MoSCoW |
| ------ | ------ |
| MUST | As a user, I want to be able to log in to the app so that I can use the app |
| MUST | As a user, I want to be able to generate random exercises so that I can work out |
| SHOULD | As a user, I want to be able to edit my account details so that my details can stay up to date when they change |
| SHOULD | As a user, I want to be able to delete my account so that my details are no longer stored when I do not wish them to be |
| COULD | As a user, I want to be able to change the difficulty of the exercises so that I can workout better when I want to |


<a name="usercases"></a>
### User Cases

Below are shown three user cases for how this app may be used (a user case for registering to the app, logging into and using the app and reloading the app to generate more exercises). The app may of course be used in other ways. 

User Case: Registering an account:
![usercase1](/Documentation/usercase1.png)
User Case: 
![usercase2](/Documentation/usercase2.png)
User Case:
![usercase3](/Documentation/usercase3.png)

<a name="trello"></a>
### Trello

![Trello1](/Documentation/trello1.png)
![Trello2](/Documentation/trello2.png)

<a name="risk"></a>
### Risk Assessment

| Risk | Impact | Likelihood | Response | Threat after response |
| ------ | ------ | ------ | ------ | ------ |
| Lack of clear objectives | High: poor planning often leads to project failing | Medium: New to programming and difficult to structure project while still learning | Trello board used to identify aims and plan the project | Lack of understanding of project led to not finishing everything I had wanted to |
| Problems with building the project | High: this is the focus of the project and so not building it will result in a poor project | Medium: new to programming so there is a good chance that I will run into issues | Dealing with issues as and when they occur and by trying to follow my plan as closely as possible | Some problems occured, but most very solvable |
| Issues with implementing the DevOps materials (Jenkins, Ansible, Git, Docker) | High: this is another crucial part of the project and so implementing them will result in a poor project | Medium: new to programming and have not had much experience with these materials | Ensuring that I understand the materials while learning about them will avoid most issues | Have had some, but not many issues, and most issues I have been able to solve, especially with the help of the trainers |
| Issues with implementing testing | Medium: while this does not prevent the application from working, it may lead to issues with the app that I have not spotted. This is also a crucial part of the project | Medium: we have never covered integration testing and there may be issues with running testing in parallel with other services| Will rely on manual testing as much as possible and try to keep the application as simple as possible to minimise errors as much as possible| No known issues with the application following manual testing, but have been unable to implement automated testing, possibly due to issues with Docker |

<a name="architecture"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagrams
#### Initial plan
![Initial ERD](/Documentation/ERD.png)

The application is connected to a GCP hosted mySQL server which stores a users details and allows for users to register to and login to the application. In future versions, this could also store completed exercises. Below is shown the ERD of the users table. 

#### Delivered solution
![Final ERD](/Documentation/ERD_Final.jpeg)

As shown in this ERD, the focus of the initial tables has been altered slightly to remove the team and move set additions. Simply due to time constraints and techinical limitations, I started to create the app more simply, with the intention of expanding it once the MVP was done. However, the MVP was only just completed in time (and with issues!) and so none of the stretch goals (the Could and Should of the MoSCow table) have been achieved.


<a name="depl"></a>
## Deployment

A webhook linked to the GitHub feature branch (can also be linked to the master branch if desired) allows for the continouos building and deployment of the web app through a Jenkins server (hosted on a GCP instance), which is triggered whenever an update is pushed to GitHub.
An instance on the GCP cloud platform containing a mySQL instance hosted the database and was linked to another GCP instance hosting the Flask application. 

![Deployment Pipeline](/Documentation/CI_Pipeline.jpeg)
<a name="tech"></a>
### Technologies Used

This project has made use of numerous skills and technologies used that have been taught at the QA Consulting Academy, the technologies used within this project include: 
* Google Cloud Platform VMs
* mySQL Instance on GCP - Database
* Python - Programming
* Flask - Web microframework
* Jenkins - CI Server
* Docker (Swarm and Compose) - Containerisation
* Pytest - Unit Testing
* Ansible Playbooks - Build Environments

<a name="testing"></a>
## Testing

Pytest unit testing has been used to test the web app, currently only for being tested for accessing certain pages depending on whether a user is logged in or not. Shown below is a coverage report for the app.
![Coverage Report](/Documentation/report.png)

<a name="improve"></a>
## Improvements for the Future and Difficulties

Despite numerous warnings about the dangers of being overly ambitious, my initial ERD and goals were overly ambitious and meant that a lot of time was wasted on creating pages and forms that would never be used. More time was spent trying to figure out how to technicially create something similar to what my goal was. Whilst this time was spent trying to learn a technology and cannot be considered as time wasted (given that I definetely learnt from it), it is still time that ate into what I was able to do for this project. In the future I will try to ensure that I create a plan with an easily scalable solution; an MVP that can easily be changed into a more interesting product should time allow for it. In any case, simplicity is not my enemy and I should try to embrace it and use it as a stepping stone.
<br/>
&nbsp;
Due to this, I would say that the majority of the improvements that this app could do with, relate to implementing (firstly learning how to correctly implement) the functions that I was not able to achieve due to time constraints.
<br/>
&nbsp;
A further improvement to this app relates to the visuals of the app. Currently, the app is not interesing to look at or interact with (partially as the scope of this project focused on creating an app that worked, and not an app that looked good), however, a visually appealing product is something that is highly valued in the world at present, so I would work on using CSS and Bootsrtap to create a more visually appealing app.

<a name="auth"></a>
## Authors

Jelle Vinkenoog
