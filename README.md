# Alibaba-Cloud Transport System Dataset
## Terms Explanation
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
| column   | description |
|----------|----------|
|device_name| ID of the device.|
|logical_name| ID of the component within a device, e.g. /to_east_edfa denotes a specific EDFA in OLA device.|
|item| Physical monitor name, e.g. "inputTPM" and "outputTPM" indicate the input and output power of one specific component.|
|stats_type| Statistic type, e.g. "min", "avg" and 'max" indicate the minimum, average and maximum value within 15 minutes time interval.|
|value| Value of the specifc item. For optical power, its unit is dBm.|
|actual_gain| Gain value of EDFA, in unit of dB.|
|actual-gain_tilt| Gain tilt value of EDFA, in unit of dB.|
|pn| Product number of EDFA|
|attenuation| Attenuation value of the variable optical attenuator after EDFA, in unit of dB.|
|time| Data query time.|

Through the device ID and locator, key performances of different components in the device can be found.

`ocm.csv` records the optical channel power after each EDFA. The structure of the table and the meaning of each column of the table is shown as following:
| column   | description |
|----------|----------|
|device_name| ID of the device.|
|logical_name| ID of the component within a device, e.g. /TO_WEST_OCM denotes a specific OCM in OLA device.|
|online_channel| Pre-defined channel number in this OCM.|
|center_frequency| Center frequency of the channel, in unit of GHz.|
|power| Channel power value, in unit of dBm.|
|time| Data query time.|

Similar as that in table `performance_optical`, such spectrum information is also located by the device index and the locator. Again, the channel power is calibrated to the output port on the panel which is equivalent to the panel power when VOA is set to 0 dB.

`performance_elec` records the performance data of optical terminals (transponders). Each terminal is identified by the OCH Group index, center frequency, and A or Z end by the column name as ochgroup, center_freuqency, side. For each OCH, transponders at two ends are denoted by A and Z. In the table performance_elec, statistic data of pre-FEC BER is saved in the column value, including max, min and average/instant value within each 15 minutes. It is worth noting that the time interval provided by us is also one hour, and we only select the 15-minute data within a one-hour period. The structure of the table and the meaning of each column of the table is shown as following:
| column   | description |
|----------|----------|
|device_name| ID of the device.|
|logical_name| ID of the component within a device, e.g. /1/1/L1 denotes a specific transponder port in the terminal device.|
|item| Physical monitor name, e.g. 'preFecBer' means the Pre-FEC BER value.|
|stats_type| Statistic type, e.g. "min", "avg" and 'max" indicate the minimum, average and maximum value within 15 minutes time interval.|
|value| Value of the specifc item. |
|och| Och ID corresponding to the specific transponder port in the terminal device.|
|center_frequency| Center frequency of the channel, in unit of GHz.|
|och_group| ID of an OCH group which this OCH belongs to. OCHes within one OCH group share the same source, destination and path.|
|time| Data query time.|
|side| ID to describe the position of this transponder in the OCH, e.g. 'A' or 'Z' means that this transponder is on the 'A' or 'Z' side of the OCH.|
|pn| Product number of the terminal device.|

`ber-margin.json` records the BER vs. GOSNR margin curves of two terminals, and they are measured in B2B condition. GOSNR margin is defined by the difference between measured GOSNR value at specific BER and GOSNR limit which is provided by vendor. GOSNR margin is in unit of dB.

## Python Demo
We provide a simple python demo to show how to use the data. Taking OMS1 as an example, we can obtain the output power of device 1 and the input power of device 2. Then, the real fiber loss can be calculated.  In the meanwile, with the actual gain of device 1 and the `olr.json`, the noise figure can be obtained. And we also illustrate how to obtain the real channel power from OCM which is used in [1,2], The channel power visualization of device 1 at '2000-01-01 00:00:00' is shown as following:

![imag](https://github.com/alibaba/alibaba-cloud-transport-system/blob/main/png/ocm.png)

## Related Papers
[1] Y. He, Z. Zhai, L. Wang, Y. Yan, L. Dou, C. Xie, C. Lu and A. P. T. Lau, “Improved QoT Estimations Through Refined Signal Power Measurements in a Disaggregated and Partially-Loaded Live Production Network,” in 2023 Optical Fiber Communications Conference and Exhibition (OFC), (2023), pp. Tu2F.5.

[2] Y. He, Z. Zhai, L. Wang, Y. Yan, L. Dou, C. Xie, C. Lu and A. P. T. Lau, “Improved QoT estimations through refined signal power measurements and data-driven parameter optimizations in a disaggregated and partially loaded live production network,” J.Opt. Commun. Netw., 15, pp. 638-648 (2023).




