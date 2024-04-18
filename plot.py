import matplotlib.pyplot as plt

# Data
data = {'0': 428402,
'1': 10889577,
'2': 8358152,
'3': 4767277,
'4': 1085102,
'5': 4476042,
'6': 6563337,
'7': 1860409}
# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.xlabel('Gate Number')
plt.ylabel('Count')
plt.title('Bert_Medium_Layer3(n=50000)')
plt.ylim(0, 15000000)
# Save plot as a PDF file
plt.savefig('gate_count_Layer3_50000.png', bbox_inches='tight')
plt.show()
