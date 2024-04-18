import matplotlib.pyplot as plt

# Data
data = {'0': 763604,
'1': 4416961,
'2': 1076498,
'3': 3935966,
'4': 3973830,
'5': 1515982,
'6': 2326734,
'7': 822119}
# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.xlabel('Gate Number')
plt.ylabel('Count')
plt.title('Bert_Medium_Layer4(n=50000)')
plt.ylim(0, 15000000)
# Save plot as a PDF file
plt.savefig('gate_count_Layer4_50000.png', bbox_inches='tight')
plt.show()
