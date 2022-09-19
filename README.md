# CSM voice encode / synthesis experimental code  

CSM stands for composite sinusoidal modeling, an algorithm for the speech synthesizer.  
Some of the YAMAHA FM sound devices support this feature, and several game used this feature to speak in the game application.  

|program|description|
|-|-|
|`csm_encoding.ipynb`|Audio to CSM data converter.<br>Reads an audio file and generates a CSM data file.|
|`csm_synthesis.ipynb`|CSM synthesizer.<br>Reads a CSM data file and synthesis an audio file from the CSM data|
|`csm_synthesis_rt.py`|Real-time CSM synthesizer.<br>Perform real-time CSM voice synthesis. You can change the key (frequency) of the playback sound with keyboard. This feature is something like a [vocoder](https://en.wikipedia.org/wiki/Vocoder). This program repeatedly playback the sound until you press 'q' key.|

### csm_synthesis_rt.py run example 
```sh
>python csm_synthesis_rt.py
21.82 sec
max amplitude: 123.0367660522461
Real-time CSM audio synthesis.
Keyboard layout - You can change the key of the playing back sound.
| s d   g h j   |
|z x c v b n m ,|
Press 'q' to quit.

```
### Audio samples:

[apollo11-original](https://github.com/yas-sim/csm_voice_encode_synthesis_python/blob/main/resources/apollo11_launch.wav?raw=true)  
<audio controls>
    <source src="https://github.com/yas-sim/csm_voice_encode_synthesis_python/blob/main/resources/apollo11_launch.wav?raw=true">
</audio>  

[apollo11-csm](https://github.com/yas-sim/csm_voice_encode_synthesis_python/blob/main/resources/apollo11_launch_out.wav?raw=true)

<audio controls>
    <source src="https://github.com/yas-sim/csm_voice_encode_synthesis_python/blob/main/resources/apollo11_launch_out.wav?raw=true">
</audio>  

### Memo:  
Convert audio data into mono/32Kbps wav format data.

```sh
ffmpeg\bin\ffmpeg.exe -i input.wav -ar 32000 -ac 1 -f wav "output.wav"
```
