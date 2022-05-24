import re
import joblib

pred_string = """"""

run_idx = 0
predictions = [int(s) for s in re.findall(r'\b\d+\b', pred_string)]
print(len(predictions))
joblib.dump(predictions, "./classifiers/tut5-model_KFR{}.pkl".format(run_idx))
