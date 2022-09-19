import os
import math

from pynput import keyboard
import readchar
import numpy as np
import pyaudio

# Sine wave generator
class sine_gen:
    def __init__(self):
        self.phase = 0
        self.set_frequency(1000)
        self.set_sample_rate(44100)

    def generate_sine_wave(self):
        self.wave = [ math.sin((step * (2 * math.pi)) / self.sample_rate) for step in range(self.sample_rate) ]

    def read(self):
        res = self.wave[int(self.phase)]
        self.phase += self.frequency
        if self.phase >= self.sample_rate:
            self.phase -= self.sample_rate
        return res

    def set_frequency(self, frequency):
        self.frequency = frequency
        #self.phase = 0

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate
        self.generate_sine_wave()


# Read CSM data file
input_file = 'apollo11_launch.csm'
input_file = '0001.csm'

with open(input_file, 'r') as f:
    lines = [[float(dt) for dt in (l.rstrip('\n')).split(',')] for l in f.readlines()]

# CSM data = [ [[f1,a1],[f2,a2],[f3,a3][f4,a4]], [[f1,a1],[f2,a2]].... ]
csm_data = []
for line in lines:
    item = []
    for idx in range(4):
        item.append([line[idx*2], line[idx*2+1]])
    csm_data.append(item)

print(len(csm_data) * 0.01, 'sec')

##--------------------------------------------------------------------------
# Playback

# normalize amplitude data in advance
max_amp = 0
for csm in csm_data:  # find max amplitude
    for s in range(4):
        if csm[s][1] > max_amp:
            max_amp = csm[s][1]
for csm in csm_data:  # normalize (0.0-1.0)
    for s in range(4):
        csm[s][1] /= max_amp
print(f'max amplitude: {max_amp}')

chunk_size = int(44100 * 10e-3)         # 10ms

p = pyaudio.PyAudio()
astream = p.open(format=pyaudio.paFloat32, channels=1, rate=44100, frames_per_buffer=chunk_size, output=True)

tone_ratio = [ pow(2, i/12) for i in range(13)]     # freqency ratio by tone
tone_keymap = [ch for ch in 'zsxdcvgbhnjm,']
tone_key = 0
KEY = 0
def on_press(key):
    global KEY
    if 'char' in dir(key):
        KEY = key.char
    readchar.readkey()    # read a key to clear the key buffer

print('''\
Real-time CSM audio synthesis.
Keyboard layout - You can change the key of the playing back sound.
| s d   g h j   |
|z x c v b n m ,|
Press 'q' to quit.\
''')

# CSM playback
ops = [ sine_gen() for i in range(4) ]              # CSM operators = sine wave generators

with keyboard.Listener(on_press=on_press) as listener:
    while KEY != 'q':
        for csm in csm_data:
            if KEY == 'q':
                break
            if KEY in tone_keymap:
                tone_key = tone_keymap.index(KEY)
            output = [0] * chunk_size                   # output audio buffer
            for s in range(4):
                freq, amp = csm[s]
                ops[s].set_frequency(freq * tone_ratio[tone_key])
                for i in range(len(output)):            # Generate CSM wave for 10ms.
                    output[i] += ops[s].read() * amp    # CSM
            output = np.array(output, dtype=np.float32) / 4
            astream.write(output.tobytes())
    #listener.join()

astream.close()
