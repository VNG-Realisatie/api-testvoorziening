# TUTORIAL CONSUMER SESSION

In this section the following will be explained:
1. Consumer session overview
2. Starting a session
3. Using its API
4. Checking the calls
5. Running the tests

## Consumer session overview
In order to understand consumer sessions, a little knowledge of session types is required. A session type is like a blueprint for test sessions for a specified API. The session type stores the URLs of the API for which endpoints must be created by the API Test Platform. Additionally, for each endpoint scenario cases can be defined. Scenario cases consist of specific URIs that live under these endpoints and an HTTP method (i.e. GET, POST, PATCH, PUT, DELETE). Finally, a test file can be supplied, which should be a JSON
file containing Postman testscripts.

When a consumer session is started, each request made to one of the created endpoints will be logged. In order for a consumer session to succeed, all of the calls specified in the scenario cases must be made and must be successful (e.g. must have resulted in status code 200). When the consumer session is stopped, the Postman tests will be run (if a test file was supplied).

For this tutorial, the [Demo API](https://demo.api-test.nl/api/v2/schema/) will be used to demonstrate consumer sessions. It is a simple API that registers quotes, allowing the user to create, read, update and delete. 

In this tutorial, Postman is used to make API calls, a tutorial for Postman can be found [here](https://learning.getpostman.com/docs/postman/launching_postman/installation_and_updates/).

## Select an API to test
In the menu on the right, a list is displayed of the APIs that can be tested on the API Test Platform. Select the API that you wish to test and click on `Consumer`. For this tutorial, we will use the API of the ATP itself.
![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/select_consumer.png)

## Starting a session
From the session list page, we click on `Start session` in the top right corner of the page.
![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/session_list.png)

To start a session click on **Start session** in the left hand side bar. 
A list of all possible session types is presented, clicking on the name of a session type, a brief description of it is displayed.  
![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/start_testrun.png)   
The functionality of the checkbox **sandbox** is explained below.

## Using the created API
After having created a new session, and clicked the Session ID the available endpoints for this session are listed on the right hand side, under `Endpoints & Rapports`. In the case of the Demo API, only one endpoint is created.

![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/endpoints.png) 

If we were to make a call to the Demo API endpoint by using Postman for example, the following data would be returned

![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/postman_request1.png)

Every call performed to one of these endpoints is logged in the detail page under `Log`
![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/consumers_log.png)

## Checking the calls
Clicking of the report page, the list of all the calls that should be performed is shown. Once the url and the query parameters are strictly matched, the scenario case is registered, successfully if the result of the HTTP calls is not a error code.

In the case of the Demo API, if a GET request is made to the `quotes` endpoint, as shown below:

![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/postman_request1.png)

It will appear in the `Report` of the session as a successful call:

![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/consumers_report.png)

If the **sandbox** option has been checked, it is possible to call several times the same url path and override the result with the last one. On the other side, if the sandbox option is off, only the first result is saved.  

## Running the tests
When the consumer session is stopped, if a test file with Postman testscripts was provided, it will be run against the endpoints for additional validation.

To illustrate this with our Demo API, the session can be stopped from the main consumer session view by pressing the blue `Stop` button:

![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/stop_session.png)

When the session is stopped, the result of the Postman tests will be displayed and the badge will be generated:

![](https://raw.githubusercontent.com/VNG-Realisatie/api-testvoorziening/master/tutorials/images/session_result.png)

Because not all of the required calls have been made in the example above, the badge will display "not completed". Only if all required calls have been made and were successful will the badge display "Success".
