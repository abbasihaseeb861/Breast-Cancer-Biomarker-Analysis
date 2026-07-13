# Breast-Cancer-Biomarker-Analysis
Analysis of TCGA breast cancer RNA-seq data using Python and ML to identify biomarker genes

## How to Run
```bash
pip install pandas numpy matplotlib
python analysis.py
```

## Expected Output
The code generates a bar plot showing Log2 Fold Change of genes.
Genes with Log2FC > 1 are considered significantly upregulated in Cancer.

## Key Finding
BRCA1, TP53, and ERBB2 showed highest upregulation in cancer samples.

## Technologies Used
- Python
- Pandas, NumPy
- Matplotlib for visualization
