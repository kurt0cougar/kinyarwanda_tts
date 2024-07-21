#!/usr/bin/python2
from naoqi import ALProxy
import subprocess
import sys

audio_path = sys.argv[1] 
audio_name = audio_path.split("/")[-1]
IP = "172.29.111.230"
PORT = 9559

subprocess.call(["sshpass","-p","nao","scp",audio_path,"nao@172.29.111.230:/home/nao"]) 
print "Initializing the audio player"
audio_player = ALProxy("ALAudioPlayer",IP,PORT)

audio_player.playFile("/home/nao/"+audio_name)
print "After playing the audio"
subprocess.call(["sshpass","-p","nao","ssh","nao@172.29.111.230","rm /home/nao/"+audio_name])

