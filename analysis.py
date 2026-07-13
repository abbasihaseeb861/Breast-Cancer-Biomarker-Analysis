# Breast Cancer Biomarker Analysis
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("=== Breast Cancer Biomarker Analysis ===")

df = pd.read_csv('Sample_tcga_data.csv')
print("Data loaded:")
print(df)

df['FoldChange'] = df['Cancer'] / df['Normal']
df['Log2FC'] = np.log2(df['FoldChange'])

print("\nTop Upregulated Genes in Cancer:")
print(df.sort_values('Log2FC', ascending=False)[['Gene', 'Log2FC']].head())

plt.figure(figsize=(10,5))
plt.bar(df['Gene'], df['Log2FC'], color='skyblue')
plt.axhline(y=1, color='r', linestyle='--', label='2x Upregulated')
plt.title('Log2 Fold Change: Cancer vs Normal')
plt.ylabel('Log2 Fold Change')
plt.xlabel('Gene')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig('volcano_plot.png')
print("\nGraph saved as volcano_plot.png")
