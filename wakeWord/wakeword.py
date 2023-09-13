#wakeup model
import pvporcupine
#voice/wave/sound process
import pyaudio 
import struct
#API KEY for hot word picovoice


PICOVOICE_API_KEY = "KNIrwq9lmXqHfNxhvDTDPsFQ5hTYOAmGdK0PAQqaFtPunAsbXHO2Vg=="
keyword_path = "*.ppn"

class PicoWakeWord:
    def __init__(self, PICOVOICE_API_KEY, keyword_path):
        self.PICOVOICE_API_KEY = PICOVOICE_API_KEY
        self.keyword_path = keyword_path
        self.porcupine = pvporcupine.create( #create procupine
            access_key = PICOVOICE_API_KEY,
            keyword_paths = ['./wakeWord/Hey-Yuki_en_windows_v2_2_0/Hey-Yuki_en_windows_v2_2_0.ppn'],
        )
        self.myaudio = pyaudio.PyAudio()
        self.stream = self.myaudio.open(
            input_device_index=0,
            rate= self.porcupine.sample_rate,
            channels=1,
            format=pyaudio.paInt16,
            input=True,
            frames_per_buffer=self.porcupine.frame_length
        )

    def detect_wake_word(self):
            audio_obj = self.stream.read(self.porcupine.frame_length, exception_on_overflow = False)
            audio_obj_unpacked = struct.unpack_from("h" * self.porcupine.frame_length, audio_obj)
            keyword_idx = self.porcupine.process(audio_obj_unpacked)
            return keyword_idx
        

if __name__ == '__main__':
    picowakeword = PicoWakeWord(PICOVOICE_API_KEY, keyword_path)

    while True:
        if(picowakeword.detect_wake_word() >= 0):
             print("I heard it")

        




