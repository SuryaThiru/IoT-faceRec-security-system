# IoT - Face recognition based security system

## Instructions to Run
1. Make sure the webcam or ip cam is connected and device id specified in the camera_loop.py file
2. Specify the ip adress of the mediator server in the camera_loop.py
3. Run cameral_loop.py on a raspberry pi
4. Run the server.py on the mediator -- a local server
5. Run the tele_receive.py on the mediator

To use the docker container for raspberry pi 3, use the docker image
```
docker run -it --rm --network host \
    -v `pwd`:/`pwd` \
    <docker image name/id> \
    bash
```
and run the scripts in the container
