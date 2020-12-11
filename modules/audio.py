# AUDIO STREAMING
import pyaudio
import numpy as np
import simpleaudio as sa

CHUNK = 2 ** 13
RATE = 44100
DURATION = 1.0
FREQUENCY = 440.0
VOLUME = 0.5


class Speaker:
	def __init__(self, device = None, startStreaming = True):
		self.chunk = CHUNK
		self.rate = RATE
		self.duration = DURATION
		self.frequency = FREQUENCY
		self.volume = VOLUME
		self.p = pyaudio.PyAudio()

		if startStreaming:
			self.stream_start()

	def stream_start(self):
		self.stream = self.p.open(format = pyaudio.paInt16,
                                channels = 1,
                                rate = self.rate,
                                input = True,
                                frames_per_buffer = self.chunk)
    
	def extract_stream_data(self):
		header = self.genHeader(self.rate, 16, 1)
		first_run = True

		while True:
			if first_run:
				data = header + self.stream.read(self.chunk, exception_on_overflow = False)
				first_run = False
			else: 
				data = self.stream.read(self.chunk, exception_on_overflow = False)
			yield data
    
	def stream_stop(self):
		self.stream.stop_stream()
		self.stream.close()

	def close(self):
		self.stream_stop()
		self.p.terminate()

	def genHeader(self, sampleRate, bitsPerSample, channels):
		datasize = 2000*10**6
		o = bytes("RIFF",'ascii')                                               # (4byte) Marks file as RIFF
		o += (datasize + 36).to_bytes(4,'little')                               # File size in bytes excluding this and RIFF marker
		o += bytes("WAVE",'ascii')                                              # (4byte) File type
		o += bytes("fmt ",'ascii')                                              # (4byte) Format Chunk Marker
		o += (16).to_bytes(4,'little')                                          # (4byte) Length of above format data
		o += (1).to_bytes(2,'little')                                           # (2byte) Format type (1 - PCM)
		o += (channels).to_bytes(2,'little')                                    # (2byte)
		o += (sampleRate).to_bytes(4,'little')                                  # (4byte)
		o += (sampleRate * channels * bitsPerSample // 8).to_bytes(4,'little')  # (4byte)
		o += (channels * bitsPerSample // 8).to_bytes(2,'little')               # (2byte)
		o += (bitsPerSample).to_bytes(2,'little')                               # (2byte)
		o += bytes("data",'ascii')                                              # (4byte) Data Chunk Marker
		o += (datasize).to_bytes(4,'little')                                    # (4byte) Data size in bytes
		return o

