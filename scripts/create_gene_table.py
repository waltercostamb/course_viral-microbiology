#Generated by ChatGPT

import pandas as pd
import random

# Number of genes to generate
num_genes = 100

# Hypothetical gene data
gene_data = {
    'Gene_ID': ['Gene{}'.format(i) for i in range(1, num_genes + 1)],
    'Start': [random.randint(1, 900) for _ in range(num_genes)]
}

# Calculate the end position based on start position and a random length
gene_data['End'] = [start + random.randint(100, 1000) for start in gene_data['Start']]

# Creating the DataFrame
gene_df = pd.DataFrame(gene_data)

# Display the first ten genes
print(gene_df.head(10))
