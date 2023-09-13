#wakeup model
import pvporcupine
#voice/wave/sound process
import pyaudio 

import struct
#API KEY for hot word picovoice


PICOVOICE_API_KEY = "KNIrwq9lmXqHfNxhvDTDPsFQ5hTYOAmGdK0PAQqaFtPunAsbXHO2Vg=="

porcupine = pvporcupine.create( #create procupine
    access_key = PICOVOICE_API_KEY,
    keyword_paths = ['./wakeWord/Hey-Yuki_en_windows_v2_2_0/Hey-Yuki_en_windows_v2_2_0.ppn'],
)

myaudio = pyaudio.PyAudio()
stream = myaudio.open(
    input_device_index=0,
    rate= porcupine.sample_rate,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    frames_per_buffer=porcupine.frame_length
)

while True:
    audio_obj = stream.read(porcupine.frame_length, exception_on_overflow = False)
    audio_obj_unpacked = struct.unpack_from("h" * porcupine.frame_length, audio_obj)

    keyword_idx = porcupine.process(audio_obj_unpacked)

    if keyword_idx >= 0:
        print("I heard it.")    

