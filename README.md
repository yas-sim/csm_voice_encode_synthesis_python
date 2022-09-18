# CSM voice encode / synthesis experimental code  

CSM stands for composite sinusoidal modeling, an algorithm for the speech synthesizer.  
Some of the YAMAHA FM sound devices support this feature, and several game used this feature to speak in the game application.  

|program|description|
|-|-|
|`csm_encoding.ipynb`|reads an audio file and generates a CSM data file.|
|`csm_synthesis.ipynb`|reads a CSM data file and synthesis an audio file from the CSM data|

### Audio samples:
[apollo11-original](./resources/apollo11_launch.wav)  
[apollo11-csm](./resources/apollo11_launch_out.wav)

### Memo:  
Convert audio data into mono/32Kbps wav format data.

```sh
ffmpeg\bin\ffmpeg.exe -i input.wav -ar 32000 -ac 1 -f wav "output.wav"
```
