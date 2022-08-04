This is the corresponding repository of the paper titled "AIPStack: a sequence-based stacking ensemble model for the prediction of anti-inflammatory peptides".


# AIPStack

The AIPStack is a two-layer stacking ensemble model, proposed for the identification of Anti-inflammatory peptides. In this model, the peptide sequences are represented by the combination of two feature encoding schemes, i.e. dipeptide deviation from expected mean and composition of k-spaced amino acid pairs. To construct the prediction framework, random forest and extremely randomized tree are employed as the base-classifiers in the first layer and logistic regression is applied as a meta-classifier in the second layer, which accepts the outputs from the first layer. The systematic workflow for the prediction of AIPs is depicted in the figure below.

![Alt text](https://github.com/Nicole-DH/AIPStack/blob/master/img/flowchart.png)


# Licence
The code and datasets are only allowed for accedemic research. Commercial usage is not granted.
