GlassA = "Raspberry"
GlassB = "Lemonade"

print("Contents of Glass A and Glass B Before Exchanging")
print(f"GlassA = {GlassA}")
print(f"GlassB = {GlassB}")

temp = GlassA
GlassA = GlassB
GlassB = temp

print("*********************")
print("Contents of Glass A and Glass B After Exchanging")
print(f"GlassA = {GlassA}")
print(f"GlassB = {GlassB}")
