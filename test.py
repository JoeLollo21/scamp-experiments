from scamp import *

s = Session(tempo=50)
guitar = s.new_part("Guitar")
s.start_transcribing()

melody = [ # This is really just a C chromatic scale
  (60, 0.25), # C, quarter note
  (64, 0.25), # E, quarter note
  (67, 0.5) # G, half note
  (72, 0.25) # C, quarter note
  (76, 1.0) # E, whole note
  (79, 0.25) # G, quarter note
  (84, 0.25), # C, quarter note
  (None, 0.25), # Quarter rest
  (81, 0.5), # A, half note
  (79, 0.25), # C, quarter note
  (76, 0.5), # E, half note
  (72, 0.125), # C, eighth note
  (69, 0.125), # A, eighth note
  (67, 0.125), # G, eighth note
  (64, 0.125), # E, eighth note
  (60, 0.5), # C, half note
  (55, 0.25), # G, quarter note
  (62, 0.25), # D, quarter note
  (67, 0.5), # G, half note
  (72, 0.25), # C, quarter note
  (76, 0.25), # E, quarter note
  (60, 1.0) # C, whole note
]

for pitch_duration in melody:
  guitar.play_note(pitch, 0.7, duration)
 
s.stop_transcribing().to_score().show()
