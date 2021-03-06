# API Test Platform

[![Status badge](https://img.shields.io/endpoint.svg?style=plastic&url=https%3A//api-test.nl/api/v1/provider-latest-badge/3fa51402-62c6-42d6-89fd-e14a2b818a6c/)](https://api-test.nl/server/2/dff1f823-ecc7-4ab8-8fb6-cc20793bd60f/3fa51402-62c6-42d6-89fd-e14a2b818a6c/latest/) [![Build Status](https://jenkins.nlx.io/job/gemma-zaken-build-and-test/badge/icon?style=plastic)](https://jenkins.nlx.io/) ![Repo Status](https://img.shields.io/badge/status-concept-lightgrey.svg?style=plastic)
 ![Uptime (30 days)](https://img.shields.io/uptimerobot/ratio/m782967733-af2d9fd1617222dbece6f648?style=plastic)

## Introduction 

To reach the goals of the [Common Ground](https://commonground.nl) for Dutch municipalities a platform to test their API's is being developed. These are the main features of the [API Test Platform](https://api-test.nl):

* Functionality for testing both consumers as providers of the API's.
* Sandbox to play with API's.
* Facilities for demonstrating compliancy such as test reports and badges.
* Scheduler for monitoring API's.
* [API](https://api-test.nl/api/v1/schema) for integration with your own CI/CD pipeline.

## Documentation
First, in order to use the API Test Platform you need to create a user, you can easily follow the tutorial [here](https://github.com/VNG-Realisatie/api-testvoorziening/blob/master/tutorials/USER.md).
Then, you can test both provider and consumer following the steps depicted in these guides:

0. [Register](https://github.com/VNG-Realisatie/api-testvoorziening/blob/master/tutorials/USER.md)
1. [Consumer session](https://github.com/VNG-Realisatie/api-testvoorziening/blob/master/tutorials/CONSUMER_SESSION.md)
2. [Provider test](https://github.com/VNG-Realisatie/api-testvoorziening/blob/master/tutorials/PROVIDER_TEST.md)
3. [API](https://github.com/VNG-Realisatie/api-testvoorziening/blob/master/tutorials/API.md)
4. [Roadmap](https://github.com/VNG-Realisatie/api-test-platform/blob/master/doc/general/Roadmap.md)

Regarding the API endpoints, you can analyze the swagger generated schema [here](https://vng-staging.maykin.nl/api/v1/schema) or directly the OpenApi yaml [file](https://github.com/VNG-Realisatie/api-testvoorziening/blob/master/api-specificatie/openapi.yaml). 


## Software
The code of this project can be found [here](https://github.com/VNG-Realisatie/api-testvoorziening-code).


## Roles

- Client: [@TheoVNGPeters](https://github.com/TheoVNGPeters)
- Product owner: [@HenriKorver](https://github.com/HenriKorver)
- Scrum master:  [@JanWillemKooi](https://github.com/JanWillemKooi)

## License
Copyright © VNG Realisatie

[Licensed under the EUPL](LICENCE.md)
