import wave
from bitstring import BitArray

def convertBinaryToWav(name, binary):
    samplerate = 44100
    bitArray = BitArray(binary)
    with wave.open(f"{name}.wav", "w") as f:
        f.setnchannels(2)
        f.setsampwidth(2)
        f.setframerate(samplerate)
        f.writeframes(binary)

def convertWavToBinary(path):
    with wave.open(path, 'r') as f:
        return f.readframes(f.getnframes())