from mlxtend.classifier import StackingCVClassifier
from sklearn.linear_model import LogisticRegressionCV as LR
from sklearn.ensemble import ExtraTreesClassifier as ET, RandomForestClassifier as RF

seed = 42

def build_model():
    """
    A two-layer stacking ensemble model.
    """
    et = ET(max_features='log2', n_estimators=1300, random_state=seed)
    rf = RF(max_features='log2', n_estimators=1600, oob_score=True, random_state=seed)
    lr = LR()

    sclf = StackingCVClassifier(classifiers=[et, rf],
                                  use_probas=True,
                                  drop_proba_col='last',
                                  meta_classifier=lr,
                                  cv=10,
                                  n_jobs=20,
                                  random_state=seed)

    return sclf


clf = build_model()
