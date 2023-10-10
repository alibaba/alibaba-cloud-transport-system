# Alibaba-Cloud Transport System Dataset
## Terms explanation
- EDFA: Erbium Doped Fiber Amplifier

- OCM：Optical Channel Monitor

- OMS：Optical Multiplex Section

- OCH: Optical Channel

- GOSNR: Generalized Optical Signal to Noise Ratio

- BER: Bit Error Ratio

- OLR: Optical Line Router

- ROADM: Reconfigurable Optical Add Drop Multiplexer

- OLA: Optical Line Amplifier

- OLE: Optical Line Equalizer

- PN: Product Number

## Dataset Folder Structure
The whole dataset folder structure is shown as following:

![imag](https://github.com/alibaba/alibaba-cloud-transport-system/blob/main/png/data_structure.jpg)

In the dataset, three Json files and three csv files are provided with comprehensive information required for transport network performance estimation.
### Json File Structure

`ber-margin.json` records two transponders' BER-GOSNR curves measured in the laboratory at B2B condition. Those two transponders are distinguished by their IDs. Besides that, osnr-limit and baud rate of the transponders are also provided.

`ola.json` and `olr.json` records the relationship between the noise figure (NF) and gain of EDFAs classified by PN. It is worth noting that for OLA and OLR, the NF-GAIN curves corresponding to the same PN are different.

### Csv File Structure

We Provide `performance_optical.csv`, `ocm.csv`, 'performance_elec.csv` in the dataset.

`performance_optical.csv` records the total input/output optical power of the EDFA with one data point per hour, and both of them are calibrated to the panel port which is equivalent to the panel power when VOA is set to 0 dB. For each of them, three statistic data types are recorded: min, max, and average, which are distinguished by the column stats_type, representing the maximum, minimum, and average during the scanning period of 15 minutes. It is worth noting that the time interval provided by us is one hour, meaning that we only consider data for 15-minute intervals within a one-hour period. Each EFDA’s tilt configuration and VOA’s attenuation value are also stored in this table. The structure of the table and the meaning of each column of the table is shown as following:
| column   | meaning |
|----------|----------|
|device_name|the name of the device|
|logical_name|the logical name of the device|
|item| including "inputTPM" and "outputTPM" which indicates the input power and the output power of the locator in device|
|stats_type| including "min", "avg", 'max" which indicates the min, avg and max power within 15 minutes|
|value| the value of the power and the unit is dBm|
|actual_gain| the gain of the edfa|
|actual-gain_tilt| the gain tilt of the edfa|
|pn| the product-number of the edfa|
|attenuation| the attenuation of the VOA after the edfa|
|time| the time of the value|

Through the device ID and locator, key performances of different components in the device can be found.

`ocm.csv` records the optical channel power after each EDFA. The structure of the table and the meaning of each column of the table is shown as following:
| column   | meaning |
|----------|----------|
|device_name| the name of the device|
|logical_name|the logical name of the device|
|online_channel| the number of channels pass through the edfa|
|center_frequency| the center frequency of the channel|
|power| the channel power of the center frequency, the unit is dBm|
|time| the time of the value|

Similar as that in table `performance_optical`, such spectrum information is also located by the device index and the locator. Again, the channel power is calibrated to the output port on the panel which is equivalent to the panel power when VOA is set to 0 dB.

In the table `performance_elec`, performance of optical terminals (transponders) is saved. Each terminal is identified by the OCH Group index, center frequency, and A or Z end by the column name as ochgroup, center_freuqency, side. For each OCH, transponders at two ends are denoted by A and Z. In the table performance_elec, statistic data of pre-FEC BER is saved in the column value, including max, min and average/instant value within each 15 minutes. It is worth noting that the time interval provided by us is also one hour, and we only select the 15-minute data within a one-hour period. The structure of the table and the meaning of each column of the table is shown as following:
| column   | description |
|----------|----------|
|device_name|the name of the device|
|logical_name|the logical name of the device|
|item| all of this column is 'preFecBer'|
|stats_type| including "min", "avg"/"instant", "max" which indicates the min, avg(instant) and max within 15 minutes|
|value| the ber of the device|
|och| the och ID corresponding to the device name and logical name|
|center_frequency| the center frequency of the och|
|och_group| the och group ID of the och|
|time| the time of the value|
|side| the side of the och, including 'A' and 'Z'|
|pn| the product number of the device| 

By the PN of transponder and the ber value, we can obtain the GOSNR with `ber-margin.json`. 
## Python Demo
We provide a simple python demo to show how to use the data. Taking OMS1 as an example, we can obtain the output power of device 1 and the input power of device 2. Then, the real fiber loss can be calculated.  In the meanwile, with the actual gain of device 1 and the `olr.json`, the noise figure can be obtained. And we also illustrate how to obtain the real channel power from OCM which is used in [1,2], The channel power visualization of device 1 at '2000-01-01 00:00:00' is shown as following:

![imag](https://github.com/alibaba/alibaba-cloud-transport-system/blob/main/png/ocm.png)

## Related papers
[1] Y. He, Z. Zhai, L. Wang, Y. Yan, L. Dou, C. Xie, C. Lu and A. P. T. Lau, “Improved QoT Estimations Through Refined Signal Power Measurements in a Disaggregated and Partially-Loaded Live Production Network,” in 2023 Optical Fiber Communications Conference and Exhibition (OFC), (2023), pp. Tu2F.5.

[2] Y. He, Z. Zhai, L. Wang, Y. Yan, L. Dou, C. Xie, C. Lu and A. P. T. Lau, “Improved QoT estimations through refined signal power measurements and data-driven parameter optimizations in a disaggregated and partially loaded live production network,” J.Opt. Commun. Netw., 15, pp. 638-648 (2023).




