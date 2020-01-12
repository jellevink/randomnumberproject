# Random Exercise Generator
This is a simple web application to generate random exercises for a user to complete when they do not know how they should workout. This has been made following the criteria needed for the SFIA project due in on Monday 13 January 2020 at the QA Consulting Academy. This brief will highlight the planning, design, creation, testing and deployment processes used during this project.

Presentation:   <br/>
Trello:   <br/>
Website:  <br/>


## Index
[Brief](#brief)
   * [Solution](#solution)
   * [Trello](#trello)
   
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

This application is designed to allow users to log recently caught pokemon and their attributes (ie movesets) with the intention of using these pokemon to form teams. 

Below are entailed a series of user stories for how the app may be used and their level of requirement according to a MoSCoW (Must, Shoud, Could, Would) scale.



|  | User Stories and their MoSCoW |
| ------ | ------ |
| MUST | As a trainer, I want to be able to add pokemon to my database so that I know what they are |
| MUST | As a trainer, I want to be able to add pokemon moves so that I know what moves are available and what their power is |
| MUST | As a trainer, I want to be able to view the pokemon and their movesets that I have entered |
| SHOULD | As a trainer, I want to be able to create a team out of the pokemon in the database so that I can use a preset team in gameplay |
| SHOULD | As a trainer, I want to be able to create multiple teams out of the pokemon in the database so that I can create teams for gameplay |
| SHOULD | As a trainer, I want to be able to delete teams when I no longer need them so that my team list does not become too cluttered |
| SHOULD | As a trainer, I want to see the pokemon in the my team so that I know what that team is good for |
| COULD | As a trainer, I want to see the movesets and damage of the pokemon in my team so that I can better see what my team is good for |
| COULD | As a trainer, I want to be able to see the theme (typing) of my teams so that I can easily select one for gameplay |
| COULD | As a user, I want to use an app that looks nice so that I can enjoy using it |

<a name="trello"></a>
### Trello
![Trello1](/Documentation/trello1.png)
![Trello2](/Documentation/trello2.png)

<a name="architecture"></a>
## Architecture
<a name="erd"></a>
### Entity Relationship Diagrams
#### Initial plan
![Initial ERD](/Documentation/ERD_Initial.jpeg)

The initial plan for the project, reflected in the ERD above, consisted of a lot more tables and entities than were produced in the final application. Given the time constraints and technical capability issues, I decided to narrow the range of the scope of the project and so started with a MVP (Minimum Viable Product), which has been created and so I only managed to deliver two tables plus a join, as shown below. 

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

* Google Cloud Platform VMs
* mySQL Instance on VCP - Database
* Python - Programming
* Flask - Web microframework
* Jenkins - CI Server
* Pytest - Unit Testing

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
