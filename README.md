# Random Exercise Generator
This is a simple web application to generate random exercises for a user to complete when they do not know how they should workout. This has been made following the criteria needed for the SFIA project due in on Monday 13 January 2020 at the QA Consulting Academy. This brief will highlight the planning, design, creation, testing and deployment processes used during this project.

Presentation: https://docs.google.com/presentation/d/1tm3JUXxm1hJjnSwjx0A_a75Bs4UwrT1y485jIgPjrs0/edit#slide=id.p  <br/>
Trello: https://trello.com/b/NbFXSnI8/projecttwee  <br/>
Website:  http://34.89.127.153/  <br/>
<a name="ansible"><a/>Ansible Playbooks: https://github.com/jellevink/playbooks  <br/>


## Index
[Brief](#brief)
   * [Solution](#solution)
   * [User Stories](#userstories)
   * [User Cases](#usercases)
   * [Trello](#trello)
   * [Risk Assessment](#risk)
   
[Architecture](#architecture)
   * [Entity Relationship Diagrams](#erd)
   * [Back-End Architucture](#backend)
	
[Installation Guide](#install)

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

Below are shown three user cases for how this app may be used (a user case for registering to the app, logging into and updating user details and logging into and reloading the app to generate more exercises). The app may of course be used in other ways. 

User Case: Registering an account:
![usercase1](/Documentation/usercase1.png)

User Case: Changing the details of an account: 
![usercase2](/Documentation/usercase2.png)

User Case: Using the app to view exercises: 
![usercase3](/Documentation/usercase3.png)

<a name="trello"></a>
### Trello

Trello has been used as a tool for planning the project, both before starting and during the project to update what I believed needed to be done, shown below are screenshots of the Trello board towards the end of the project, a link to the Trello board can be found at the top of this document. 
![Trello1](/Documentation/trello1.png)

<a name="risk"></a>
### Risk Assessment

A number of risks have been identified and categorised, complete with how I intend to minimise the likelihood of them occuring and the risk they pose. These risks may take the form of both technical risks and risks involved with executing projects in general. 

| Risk | Impact | Likelihood | Response | Threat after response |
| ------ | ------ | ------ | ------ | ------ |
| Lack of clear objectives | High: poor planning often leads to project failing | Medium: New to programming and difficult to structure project while still learning | Trello board used to identify aims and plan the project | Lack of understanding of project led to not finishing everything I had wanted to | 
| Problems with building the project | High: this is the focus of the project and so not building it will result in a poor project | Medium: new to programming so there is a good chance that I will run into issues | Dealing with issues as and when they occur and by trying to follow my plan as closely as possible | Some problems occured, but most very solvable | 
| Issues with implementing the DevOps materials (Jenkins, Ansible, Git, Docker) | High: this is another crucial part of the project and so implementing them will result in a poor project | Medium: new to programming and have not had much experience with these materials | Ensuring that I understand the materials while learning about them will avoid most issues | Have had some, but not many issues, and most issues I have been able to solve, especially with the help of the trainers | 
| Issues with implementing testing | Medium: while this does not prevent the application from working, it may lead to issues with the app that I have not spotted. This is also a crucial part of the project | Medium: we have never covered integration testing and there may be issues with running testing in parallel with other services | Will rely on manual testing as much as possible and try to keep the application as simple as possible to minimise errors as much as possible | No known issues with the application following manual testing, but have been unable to implement automated testing, possibly due to issues with Docker | 
| Accidental release of data (eg account info, private IP addresses or environment variables) when uploading | High: If someone finds the data they can access and manipulate the application | Low: It is unlikely that I will upload something, and even lower that someone with malicious intent finds it and acts upon it | Ensure that .gitignore is used correctly | Low | 
| Loss of data due to VM shutdown | Medium: when a VM shuts down, the containers being run on it will exit, so the app will suffer downtime | Low: GCP is responsible for the upkeep of the VMs and so will do their best to keep them up | Set containers to --restart=always so that they restart immediately should a VM go down | Low | 


<a name="architecture"></a>
## Architecture
<a name="backend"></a>
### Back-End Architecture

The application consists of four services working together. Two services (random1 and random2) generate a random number between 1 and 10 inclusive. These are accessed by a GET request by a service (combine) which combines the numbers such that one randomly generated number refers to the number of reps to complete (after a mathematical operation has been applied to it) and the other randomly generated number refers to the exercise to be completed. In a second implemtation of this service, the number of reps is increased. This is accessed by another GET request by a fourth service (flask) which generates the front-end of the application. An nginx container acts as a proxy pass to direct traffic to the application. These are all held within a Docker network. The structure is shown below. 

![Back-end Structure](/Documentation/structure.png)

<a name="erd"></a>
### Entity Relationship Diagrams
#### Initial plan

The application is connected to a GCP hosted mySQL server which stores a users details and allows for users to register to and login to the application. In future versions, this could also store completed exercises. Below is shown the ERD of the users table. 

![Initial ERD](/Documentation/ERD.png)

<a name="install"></a>
## Installation Guide
* Create two GCP instances (In this project, they are called qaproject2 and qaproject2jenkins, but you may change these names, just remember to change the names in the inventory of the ansible-playbooks). These should be running Ubuntu 18.04 LTS if possible.
* Create a mySQL instance in GCP and follow the GCP tutorial to allow access to it from the qaproject2 VM.
* Install Ansible onto your local machine, an installation guide can be found here: https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html
* Install this repo (https://github.com/jellevink/playbooks.git) with the 'git clone' command.
* Add the public keys from your two VMs into the ansible_id_rsa.pub file within the .ssh folder on your local machine.
* Edit the ansible inventory to include the correct usernames/IPs for your accounts and using the 'ansible-playbook' command, install the needed environments contained with the playbooks onto your VMs. Retrieve the Jenkins Initial Admin Password from the 'Jenkins Install Task' once ansible has run.
* On your qaproject2 VM, navigate to ~/.bashrc and add the following environment variables, adding those of your mySQL instance:
	* MYSQL_USER={your mySQL instance user}
	* MYSQL_PASSWORD={your mySQL instance user password}
	* MYSQL_HOST={your mySQL instance IP address}
	* MYSQL_DB={your mySQL instance database name}
	* YOUR_SECRET_KEY={any random string}
* Clone this repo (git clone https://github.com/jellevink/randomnumberproject.git) onto your VM.
* Save this as your own project and GitHub and save the link as this will be needed later.
* Navigate to the settings of this GitHub repo, select 'Webhooks' and add a webhook. The payload url should be added as follows: http://{ip of qaproject2jenkins}:8080/github-webhook/ and set 'content type' to 'application/json' and save!
* Open port 5000 on the qaproject2 VM and port 8080 on the qaproject2jenkins VM.
* Navigate to port 8080 of the qaproject2jenkins VM in the web browser and insert the Jenkins Initial Admin Password when prompted, install the recommened plugins and create an account. 
* Create a new Pipeline job and select the following options in the configuration:
	* 'Discard old builds'
	* 'GitHub project' and insert te link of your new repo
	* 'GitHub hook trigger for GitScm polling', select 'Git' in the 'SCM' option and add your repo link.
	* Press Save 
* To deploy the web application, select the 'Build Now' option on the left hand side of the Jenkins window, or make a commit to your new GitHub repo to activate the webhook. 
* Navigate to the public IP of your qaproject2 VM and add ':5000' to access the correct port. 
* Congratulations, you are now on the web app!!!!


<a name="depl"></a>
## Deployment

A CI pipeline was involved in the development and deployment of the project, a mock-up of this can be seen below. 

![Deployment Pipeline](/Documentation/pipeline.png)
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

### Ansible
Ansible is a simple IT automation tool used (here) for the generation of ready-to-use environments for projects to be deployed on; installing  and configuring any tools needed on each machine in a system. In this project, a local machine was used to run Ansible, and Ansible installed tools on 2 VMs. The Ansible playbooks used in this project can be seen [here](#ansible).

### Git
Git is a version-control system used for tracking changes within a project during the software development process. Git has been used via the GitHub client for keeping the project backed up and for tracking changes to it.

### Docker
Docker is a series of PaaS 'Platform as a Service' tools that use OS-level virtualization to package services in 'containers', which can be stored as images, allowing for the product stored within the images to be run on an system thanks to everything they need to run being stored within the Docker container.

### Docker Compose
Docker Compose is a tool that builds upon the Docker tool and allows for defining and simultaneous running of multiple Docker containers, using a YAML file to configure the services needed. Docker Compose has been used in this project to build the images of each service.

### Docker Swarm
Docker Swarm refers to a collection of machines all running the same Docker application that have been configured to run in a group; run by a node known as a Swarm Mananger who controls a series of nodes known as Swarm Workers. This allows for multiple users to be using version of the same services, instead of sharing it. Due to this, if one replica fails, others will immediately pick up the slack and prevent system downtime. Additionaly, this means that updates to the application will be smooth and will not affect the user experience of the app. In this project, the main application is run on a Swarm Manager, and no Swarm Workers have been set up. 3 replicas of each service have been created. 

### Jenkins
Jenkins is an automation tool for continuous integration, making it simpler to integrate changes to projects seamlessly and deliver the latest version of the project to users. In this project, a pipeline project was used to make it easier to break the deployment process down into stages and see where errors in the build may be occuring, a screenshot of the pipeline process is shown below. 
![Jenkins](/Documentation/jenkins.png)


<a name="testing"></a>
## Testing

Pytest unit testing has been used to test the web app. The services for the random number generators are very simple and therefore testing is also very simple, so having a large coverage (100%) is no surprise! The testing for the front-end service was satisfactory (57% coverage) given that that integration testing was not used and only unit testing was applied. The combination service was not able to be tested as it required inputs from the random number generation services and thus needs integration testing, which we have not covered. The testing has been run through Docker too, but removed (by editing out the command) as some errors occur and to reduce time of the Jenkins pipeline build. 
![Coverage Report](/Documentation/testingflaskscreenshot.png)
![Coverage Report2](/Documentation/testingrandom.png)
![Coverage Report3](/Documentation/testingrandom2.png)

<a name="improve"></a>
## Improvements for the Future and Difficulties

Overall, I am fairly happy with how the project has been completed. The main difficulties faced during the development stage were due to a lack of knowledge of the tools being used, but the act of completing this project has helped hugely with this. 
<br/>
&nbsp;
This project was fairly simple, so in the future I would like to expand on it, either by adding more services or by adding complexity to the services already created. Additionaly, I would like to add integrated testing as some of the services cannot currently be tested or must be tested when run as a Flask app (without Docker/Jenkins) as this would make the app more stable.
I would also like to incorporate the exercises into a table (this was intended for this project), so that exercises may be logged against the users that have completed them. Another addition I would like to make (and had planned to include) is to let the user be able to switch the difficulty of the exercises by changing the rolling implementation update manually.
Finally, I would like to make the project look neater, by incorporating CSS or Bootstrap, as apps that look nicer are more likely to be used more be users.


<a name="auth"></a>
## Authors

Jelle Vinkenoog
