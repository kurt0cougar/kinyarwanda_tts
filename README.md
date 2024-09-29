
The model is hosted on huggingface and must be logged in to access it. Use this [link](https://huggingface.co/join) to create an account if you do not have one.

For the model to run you will need at least python3.9 and the Coqui TTS library. To install the TTS library run the following:
```
pip install TTS
```

To download the model use the following steps:

Go into your ROS workspace, then
```
cd src
git clone https://github.com/kurt0cougar/kinyarwanda_tts.git
cd kinyarwanda_tts
mkdir model_files
cd model_files
```
The download the model files from huggingface:
```
 huggingface-cli download --local-dir . DigitalUmuganda/KinyarwandaTTS_female_voice
```

To run the node first launch the naoqi node:
```
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=172.29.111.230 network_interface:=enp0s3
```
Then launch the TTS node with:
```
roslaunch naoqi_driver naoqi_driver.launch nao_ip:=172.29.111.230 network_interface:=enp0s3
```
