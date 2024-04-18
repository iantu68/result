import matplotlib.pyplot as plt

# Data
data = {'0': 86713519,
        '1': 23610352,
        '2': 9522485,
        '3': 145508857,
        '4': 70665235,
        '5': 61591485,
        '6': 42461998,
        '7': 14096023}
# Create bar chart
plt.figure(figsize=(10,6))
plt.bar(range(len(data)), data.values(), align='center')
plt.xticks(range(len(data)), list(data.keys()))
plt.xlabel('Gate Number')
plt.ylabel('Count')
plt.title('Bert_Medium_Layer3(n=50000)')
plt.ylim(0, 150000000)
# Save plot as a PDF file
plt.savefig('gate_count_Layer3_50000.png', bbox_inches='tight')
plt.show()
