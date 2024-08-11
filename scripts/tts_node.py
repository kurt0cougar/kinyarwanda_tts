#!/usr/bin/python3

import rospy
from std_msgs.msg import String
import tempfile
from TTS.utils.synthesizer import Synthesizer
import subprocess
import os
import rospkg

rospack = rospkg.RosPack()
path = rospack.get_path('kinyarwanda_tts')
model_path = os.path.join(path,"model_files")
print("Path to package:", path)

python2_path = '/usr/bin/python2'
python2_script = os.path.join(path,"scripts",'send_and_play_audio.py')
class KinyarwandaTTSNode:
    def __init__(self):
        rospy.init_node('kinyarwandaTTS')
        
        # Initialize Coqui TTS model (example, adjust as per your model)
        
        self.synthesizer = Synthesizer(os.path.join(model_path,"model.pth"),
            os.path.join(model_path,"config.json"),
            tts_speakers_file=os.path.join(model_path,"speakers.pth"))
        # ROS Subscribers and Publishers
        rospy.Subscriber('text_to_say', String, self.text_to_say_callback)
        
    def text_to_say_callback(self, msg):
        text = msg.data
        rospy.loginfo(f"Received text to say: {text}")
        
        # Generate speech from text
        #audio_data = self.tts(text)
        wav = self.synthesizer.tts(text, speaker_wav=os.path.join(model_path,"conditioning_audio.wav"))
        # Publish audio data (you need to implement this part based on your needs)
        # For simplicity, you can publish audio as a ROS topic or save to a file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as fp:
            self.synthesizer.save_wav(wav, fp)
            print(fp.name)
        
        subprocess.run([python2_path, python2_script,fp.name])
    def run(self):
        rospy.spin()

if __name__ == '__main__':
    node = KinyarwandaTTSNode()
    node.run()

