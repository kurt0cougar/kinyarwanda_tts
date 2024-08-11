
The model is kept on huggingface and you must be logged in to access it. Use this (link)[https://huggingface.co/join] to create an account if you do not have one.

To download the model, use:
Go to the pre-allocated directory:
```
cd model_files
```
The download the model files from huggingface:
```
 huggingface-cli download --local-dir . DigitalUmuganda/KinyarwandaTTS_female_voice
```
To run the model, use:

```
tts --text "mwaramutse" --model_path best_model.pth --config_path config.json --speakers_file_path speakers.pth --speaker_wav conditioning_audio.wav --out_path out.wav
```
