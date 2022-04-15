import matplotlib.pyplot as plt
import numpy as np
import joblib

# run_status = {"loss_D": [],
#               "loss_G": [],
#               "loss_GAN": [],
#               "loss_cycle": [],
#               "loss_identity": []}
result_1 = joblib.load('results/cyclegan_run_e16-d8_r7_cyc1.0_id0.0.pkl')
result_2 = joblib.load('results/cyclegan_run_e16-d8_r7_cyc1.0_id1.0.pkl')
result_3 = joblib.load('results/cyclegan_run_e16-d8_r3_cyc1.0_id1.0.pkl')

print(result_1["loss_G"].__len__())
fig, ax = plt.subplots()
line1, = ax.plot(np.arange(0, result_1["loss_G"].__len__()), result_1["loss_G"])
line1.set_label("loss_G_id0")
line2, = ax.plot(np.arange(0, result_1["loss_D"].__len__()), result_1["loss_D"])
line2.set_label("loss_D_id0")

line3, = ax.plot(np.arange(0, result_2["loss_G"].__len__()), result_2["loss_G"])
line3.set_label("loss_G_r7")
line4, = ax.plot(np.arange(0, result_2["loss_D"].__len__()), result_2["loss_D"])
line4.set_label("loss_D_r7")

line5, = ax.plot(np.arange(0, result_3["loss_G"].__len__()), result_3["loss_G"])
line5.set_label("loss_G_1.0")
line6, = ax.plot(np.arange(0, result_3["loss_D"].__len__()), result_3["loss_D"])
line6.set_label("loss_D_1.0")

ax.set(xlabel="time_tik", ylabel="Loss",
       title="CycleGAN Train/Val Result_1")
ax.legend()
ax.grid()

plt.show()
