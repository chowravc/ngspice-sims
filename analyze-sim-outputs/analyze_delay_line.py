import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

names = ['time', 'vin', 'v1', 'v2', 'vout', 'inp1', 'inn1', 'inp2', 'inn2']
df = pd.read_csv('delay_chain.txt', sep='\\s+', header=None)

# Every other column is just time again
df_new = df.iloc[:, 1::2]
# New column names
df_new.columns = names

time = df_new['time']
# pe_nn1 = np.abs(df_new['v1'] * df_new['inn1'])
# pe_nn2 = np.abs(df_new['v2'] * df_new['inn2'])

# plt.plot(time, pe_nn1, label='NMOS1')
# plt.plot(time, pe_nn2, label='NMOS2')

plt.plot(time, df_new['vin'], label='vin')
plt.plot(time, df_new['v1'], label='v1')
plt.plot(time, df_new['v2'], label='v2')
plt.plot(time, df_new['vout'], label='vout')

# plt.plot(time, df_new['inn1'], label='NMOS1')
# plt.plot(time, df_new['inn2'], label='NMOS2')
plt.legend()
plt.tight_layout()
plt.show()