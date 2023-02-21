# Assignment3_IoT
In this repository is contained the code I wrote for the third assignment of my IoT course at my univerisity: Sapienza.<br/>
Please note that this is an expantion of the work I've done for the previous two assiggnments, so you should first check them out to better understand this one:<br/>
- Assignment1_IoT: https://github.com/AssignmentsIoT/Assignment1_IoT.git<br/>
- Assignment2_IoT: https://github.com/AssignmentsIoT/Assignment2_IoT.git<br/>
## Introduction
We want to build a monitoring system for two environmental stations, where both have 5 different sensors:<br/>
- temperature (- 50 / 50 °C),<br/>
- humidity (0 / 100 %),<br/>
- wind direction (0 / 360 degrees),<br/> 
- wind intensity (0 / 100 m/s),<br/>
- rain height (0 / 50 mm/h).<br/>
We'll send the data collected by the devices to our ThingsBoard dashboard to visualize it in a nice and useful way.<br/>
## Architecture and Implementation
Each environmental station will be simulated by a program done with RIOT OS, but this time, to make things more realistic, the code will be deployed on FIT IoT-Lab nodes.
The stations will use the LoRaWAN network to send data to our application. To do this, a LoRaWAN network server is needed: The Things Network.
A Python bridge will take data from The Things Network and, after a little manipulation to make it compatible with the devices we created on ThingsBoard in the first assignment, it will send the data to the dashboard. All this part of the communication is done through MQTT protocol.<br/>
### FIT IoT-Lab
FIT IoT-Lab is an open testbed that makes boards and devices available for application testing and research purposes. Have a look at their site, an account is needed: https://www.iot-lab.info/ .<br/>
I suggest you complete the following tutorials to familiarize with the technology:<br/>
- SSH access: https://www.iot-lab.info/tutorials/ssh-access (this is mandatory)<br/>
- RIOT: https://www.iot-lab.info/tutorials/riot-networking-m3/<br/>
- CLI tools: https://www.iot-lab.info/tutorials/iotlab-experimenttools-client<br/>
                   https://www.iot-lab.info/tutorials/iotlab-nodetools-client<br/>
Take also a close look at this tutorial: https://www.iot-lab.info/tutorials/riot-ttn/ , this assignment is based on it.<br/>
As The Things Network is used as LoRaWAN network server, an account on that platform is also needed.<br/>
## Conclusion
To find more information on the main concepts, please take a look at the [PDF report](https://github.com/AssignmentsIoT/Assignment3_IoT/blob/master/Environmental%20Station%20Monitoring%20System-2.pdf) in this repository.<br/>   

A complete **guide** on how to set everything up is provided **on Hackster.io**: https://www.hackster.io/silvia-del-piano/environmental-station-monitoring-with-lorawan-and-iot-lab-d9b334<br/>   

To see everything up and running check out this **video**: https://www.youtube.com/watch?v=6Qp2TJKEdic&list=PL48Vw1VOWyOlHXXhDsXb-AHYS89vMOo4g&index=4&t=0s<br/>    

I hope this has been useful and fun. If you have trouble, please contact me on LinkedIn: https://www.linkedin.com/in/silvia-del-piano-2482391a6?lipi=urn%3Ali%3Apage%3Ad_flagship3_profile_view_base_contact_details%3BEdqyH9ACQj%2BSUgI39I%2FM1g%3D%3D<br/>
Until next time, bye!