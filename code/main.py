# This is a sample Python script.

import pandas as pd
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
# load data
berToGosnr = pd.read_json('data/ber-Gosnr.json')
nfDictOla = pd.read_json('data/ola.json')
nfDictOlr = pd.read_json('data/olr.json')
ocm = pd.read_csv('data/ocm.csv')
performance_elec = pd.read_csv('data/performance_elec.csv')
performance_optical = pd.read_csv('data/performance_optical.csv')


# take OMS1, OCH1, 2000-01-01 00:00:00 as example
# device1---------device2, center frequency is 191.4THz
time = '2000-01-01 00:00:00'
center_frequency = 191.4e3
IL_ODF = 0.5
IL_O = 0.9
IL_I = 0.6
# ## get device1 power and configuration
device = 1
locator = '/D1/OA-W/EGR_EDFA'
optical_df = performance_optical[(performance_optical['time'] == time)
                                 & (performance_optical['device_name'] == device)
                                 & (performance_optical['logical_name'] == locator)
                                 & (performance_optical['item'] == 'outputTPM')
                                 & (performance_optical['stats_type'] == 'instant')]
actual_gain_1 = optical_df['actual_gain'].values[0]  # the EDFA gain of device 1
actual_gain_tilt_1 = optical_df['actual_gain_tilt'].values[0] # the EDFA gain tilt of device 1
pn_1 = optical_df['pn'].values[0]  # the EDFA pn of device 1
power_1 = optical_df['value'].values[0]  # the panel output power of device 1
edfa_power_1 = power_1 + IL_O


# ### get device1 noise figure
nf_gain_map = []
for edfa_dict in nfDictOlr['amplifier'].values:
    if edfa_dict['part-number'] == pn_1 and edfa_dict['type'] == 'BA':
        nf_gain_map = edfa_dict['noise-figure-map']

gain_points = [key_gain['gain'] for key_gain in nf_gain_map]
nf_points = [key_nf['noise-figure'] for key_nf in nf_gain_map]
tck = interpolate.interp1d(gain_points, nf_points, assume_sorted=False, kind=1)
nf = tck(actual_gain_1)

# ## get device1 ocm power of och1
locator = '/D1/OA-W/EGR_OCM'
ocm_power_1 = ocm[(ocm['time'] == time) & (ocm['device_name'] == device) & (ocm['logical_name'] == locator)]
# ## visualize the ocm
cf = ocm_power_1['center_frequency'].values
cf_1 = [191.4e3, 191.6e3, 191.8e3]
power_list_1 = [3.4, 3.2, 3.3]

power_list = ocm_power_1['power'].values

plt.bar(cf/1e3, power_list, width=0.05)

plt.bar(np.array(cf_1)/1e3, power_list_1, width = 0.05)
plt.xlabel("Center frequency [THz]")
plt.ylabel("Power [dBm]")
plt.legend(['alien och', 'provided och'])
plt.show()

# ### calibrate the ocm
ocm_power_sum_w = 0
for p_ii in ocm_power_1['power'].values:
    ocm_power_sum_w += np.power(10, p_ii / 10)
ocm_power_sum = 10 * np.log10(ocm_power_sum_w)
offset = ocm_power_sum - edfa_power_1
channel_power = ocm_power_1[ocm_power_1['center_frequency'] == center_frequency]['power'].values[0]  # get the channel power of the edfa output

# ## get device2 input power
device = 1
locator = '/D1/OA-W/IGR_EDFA'
optical_df_2 = performance_optical[(performance_optical['time'] == time)
                                 & (performance_optical['device_name'] == device)
                                 & (performance_optical['logical_name'] == locator)
                                 & (performance_optical['item'] == 'inputTPM')
                                 & (performance_optical['stats_type'] == 'instant')]
power_2 = optical_df_2['value'].values[0]  # the EDFA input power of device 1

# ## get fiber parameter
fiber_output_power = power_2 - IL_ODF  # the output power of fiber 1
fiber_input_power = power_1 - IL_ODF  # the launch power of fiber 1
fiber_loss = fiber_input_power - fiber_output_power
fiber_length = 74e3  # the fiber length of fiber 1 as shown in figure


