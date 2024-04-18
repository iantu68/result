import imageio
import os 

image_path = ["gate_count_Layer2_5000.png", "gate_count_Layer2_15000.png", "gate_count_Layer2_30000.png", "gate_count_Layer2_50000.png"]

gif_filename = "gate_count_Layer2_top_1.gif"

duration = 0.8

images = []

for image_path in image_path:
    images.append(imageio.imread(image_path))

imageio.mimsave(gif_filename, images, duration=duration)

print(f"Created GIF successfully!")
