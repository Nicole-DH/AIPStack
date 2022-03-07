# AIPStack
The AIPStack is a two-layer stacking ensemble model, proposed for the identification of Anti-inflammatory peptides. In this model, the peptide sequences are represented by the combination of two feature encoding schemes, i.e. Dipeptide Deviation from Expected Mean and Composition of k-spaced amino acid pairs. To construct the prediction framework, Random Forest and Extremely randomized Tree are employed as the base-classifiers in the first layer and Logistic Regression is applied as a meta-classifier in the second layer, which accepts the outputs from the first layer. The systematic workflow for the prediction of AIPs is depicted in the figure below.


![Alt text](https://github.com/Nicole-DH/AIPStack/blob/master/img/flowchart.png)

# Licence
The code and datasets are only allowed for accedemic research. Commercial usage is not granted.
