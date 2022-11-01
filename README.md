## What is clouding computing?
Cloud computing is the sharing of resources over the internet, such as computing power, storage, and databases
#### benefits
One of the main benefits of cloud computing is the saving of price. The reason for this is because companies don't longer need to to build infrastructure, paying for their maintenance or any physical data centers and servers. It can be access by anyone, in any place over the world, making easier for developers of anywhere over the world, have access to the data/codes or working anywhere around the world.
- ease of use
- flexibility 
- robustness - Cost - PAY AS YOU GO
<img src="./images/benefits.png" />

### Three categories
- Infrastructure (IaaS) 
- Platform as a service (PaaS)
- software as a service (SaaS)
 
- SaaS allows user to connect to and use cloud apps over the internet,
- IaaS is a type of cloud computing service that offers essential virtualized computing, storage and network resources
- 

## How to start a virtual machine in AWS

First copy the secret key "eng130.pem" file into your ".ssh" folder, run the command line `chmod eng130.pem` to make it readable. <br/>

We need to create a ec2 machine, this is the location where we will configure our instances. Location is an option, but for this course, we are going to be using our location as of ireland. This can be changed at the top right corner of the page, next to your username. <br/>
In the box called "launch instance", we will be able to launch our virtual machines, just select "Launch instance" in the drop down menu. Once we are inside, we can start going shopping and choosing our virtual machine configuration. For this project, we are going to choose the ubuntu 18.04 LTS version, everything default but make sure the name is "eng130_<"name">", the thing that might need adjusting are the security rules. make sure you can ssh using your own device(my IP) and then make sure both 80 and 3000 port is open everywhere. This is so that we can connect via the internet and port 3000 is for the app.js<br/>
Once all of this is done, we can start launching the system. In the main ec2 dashboard, we can go to "instances (running)" and look for the name we have inserted. inside there, we will be able to ssh into our system. by selecting our instance, we can click on the top right corner "connect". We will then be given instruction on how to connect to the virtual machine using our terminal in our local machine.