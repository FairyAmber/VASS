import pvporcupine
import pyaudio
import struct

#API KEY for hot word picovoice
PICOVOICE_API_KEY = "KNIrwq9lmXqHfNxhvDTDPsFQ5hTYOAmGdK0PAQqaFtPunAsbXHO2Vg=="
porcupine = pvporcupine.create(
    access_key= PICOVOICE_API_KEY,
    keyword_paths=[],

)

myaudio = pyaudio.PyAudio()
stream = myaudio.open(
    input_device_index=0,
    rate= porcupine.sample_rate,
    channels=1,
    format=myaudio.paInt16,
    frames_per_buffer=porcupine.frame_length
)

audio_obj = stream.read(porcupine.frame_length, exception_on_overflow=False)
audio_obj_unpacked = struct. unpack_from("h" * porcupine.frame_length, audio_obj)

keyword_index = porcupine.process(audio_obj_unpacked)

if keyword_index >= 0 :
    print("I heard it")