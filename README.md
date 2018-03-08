# Pied_Piper_Project

IOT Project with PCF application

This is simple Parking Automation System where its using proximity sensor to detect availability of parking lot. If parking lot is available, it will show Red light sign to show to driver. Else lighting will be turn off. Driver can also check parking lot availbility beforehand using webapplication running on Pivotal Cloud Foundry

Project including 
- parking-publish.py for raspberry pi sensor and publisher
- mqtt-sub.py for local broker subscriber
- app.py for webapp deploy on PCF 
- Redis database running on PCF
- Parking project.ppx for project overview
