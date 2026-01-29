class Metal_Detector:
    def __init__(self, signal_amp: bool, signal_dur: int, phase_angle: int, spatial_density: int):
        self.signal_amp = signal_amp
        self.signal_dur = signal_dur
        self.phase_angle = phase_angle
        self.spatial_density = spatial_density

    def metal_size_check(self, signal_amp, signal_dur):
        pass

    def detect_battery(self):
        pass

    def detect_size(self):
        pass

    def detect_duration(self):
        pass

    def get_threshold(self):
        pass

"""
levels
---
metal
1- true
0 - false
---
signal duration
1-3 - low (small-sized)
4-6 - medium (medium-sized)
7-10 - high (large-sized)
---
phase angle
1-3 - low (inductive)
4-6 - medium (mixed)
7-10 - high (conductive)
---
spatial density
1-3 - low
4-6 - medium
7-10 - high
---
"""