import re

raw_string = """
Epoch: 01 | Epoch Time: 7m 19s
	Train Loss: 1.197 | Train Acc @1:  67.78% | Train Acc @5:  90.75%
	Valid Loss: 1.136 | Valid Acc @1:  68.14% | Valid Acc @5:  93.04%
Epoch: 02 | Epoch Time: 7m 8s
	Train Loss: 1.094 | Train Acc @1:  69.00% | Train Acc @5:  92.93%
	Valid Loss: 1.055 | Valid Acc @1:  70.16% | Valid Acc @5:  94.26%
Epoch: 03 | Epoch Time: 7m 2s
	Train Loss: 0.749 | Train Acc @1:  77.71% | Train Acc @5:  96.55%
	Valid Loss: 0.821 | Valid Acc @1:  77.10% | Valid Acc @5:  96.21%
Epoch: 04 | Epoch Time: 7m 5s
	Train Loss: 0.435 | Train Acc @1:  86.68% | Train Acc @5:  98.78%
	Valid Loss: 0.552 | Valid Acc @1:  83.00% | Valid Acc @5:  98.37%
Epoch: 05 | Epoch Time: 6m 58s
	Train Loss: 0.259 | Train Acc @1:  92.23% | Train Acc @5:  99.55%
	Valid Loss: 0.293 | Valid Acc @1:  91.25% | Valid Acc @5:  99.35%
Epoch: 06 | Epoch Time: 6m 58s
	Train Loss: 0.125 | Train Acc @1:  96.12% | Train Acc @5:  99.89%
	Valid Loss: 0.281 | Valid Acc @1:  92.07% | Valid Acc @5:  99.31%
Epoch: 07 | Epoch Time: 7m 4s
	Train Loss: 0.057 | Train Acc @1:  98.22% | Train Acc @5:  99.98%
	Valid Loss: 0.106 | Valid Acc @1:  96.66% | Valid Acc @5:  99.82%
Epoch: 08 | Epoch Time: 7m 4s
	Train Loss: 0.014 | Train Acc @1:  99.65% | Train Acc @5: 100.00%
	Valid Loss: 0.078 | Valid Acc @1:  97.78% | Valid Acc @5:  99.85%
Epoch: 09 | Epoch Time: 7m 1s
	Train Loss: 0.003 | Train Acc @1:  99.91% | Train Acc @5: 100.00%
	Valid Loss: 0.069 | Valid Acc @1:  97.75% | Valid Acc @5:  99.82%
Epoch: 10 | Epoch Time: 7m 4s
	Train Loss: 0.002 | Train Acc @1:  99.96% | Train Acc @5: 100.00%
	Valid Loss: 0.064 | Valid Acc @1:  98.13% | Valid Acc @5:  99.88%
"""

train_loss = []
valid_loss = []
train_acc1 = []
train_acc5 = []
valid_acc1 = []
valid_acc5 = []
global_list = [train_loss, train_acc1, train_acc5, valid_loss, valid_acc1, valid_acc5]

loss = [float(s) for s in re.findall(r'\d+\.\d+', raw_string)]
for i in range(loss.__len__()):
    global_list[i % global_list.__len__()].append(loss[i])
print(train_loss)
print(train_acc1)
print(train_acc5)
print(valid_loss)
print(valid_acc1)
print(valid_acc5)
