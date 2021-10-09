<img src="./board_files/fz3a/A.0/fz3a_board.jpeg" alt="logo" height="160" align="right" />

# Awesome EdgeBoard Lite

**Use EdgeBoard Lite as a general Zynq development board**

[![en](https://img.shields.io/badge/lang-en-red.svg)](./README.md)

**注意** 本文档是对[英文版本README](./README.md)的翻译，仅供参考。更新可能不及时，以英文版本为准。

EdgeBoard Lite (即FZ3）是百度在2019年推出的一款嵌入式AI计算卡。作为百度EdgeBoard软硬件一体AI解决方案的一部分，它可以快速将神经网络部署到边缘计算和嵌入式场景。

EdgeBoard Lite开发板基于Xilinx Zynq Ultrascale+ ZCU3EG MPSoC，可以达到1\~2 TOP/s的算力，平均功耗5\~10 W。它的外设包括：

- 2GB DDR4 RAM
- 8GB eMMC Flash
- 256Mb QSPI Flash
- PCIe x1 connector
- MIPI camera connector
- BT1120 HDTV connector
- 1000Mbps Ethernet
- TF-card slot
- USB Hub (1 x USB 3.0, 1 x USB 2.0)
- Mini DisplayPort (miniDP)
- USB UART

除了丰富的外设，最重要的是它仅需约人民币1000元！这几乎是最便宜的Xilinx Zynq Ultrascale+开发板。与之对比，另一款广受社区欢迎的Zynq ZCU3EG开发板[Ultra96](https://www.96boards.org/product/ultra96)售价249美元。在中国市场上，Ultra96一般需要人民币2200元以上，差不多是EdgeBoard Lite的两倍。

然而，百度销售EdgeBoard系列开发板是作为其AI解决方案的硬件平台，而不是一块通用的Zynq开发板。因此，我们很难获得完整的官方技术支持。

这个GitHub仓库包括各种材料，希望能有助于将EdgeBoard Lite用作一块普通的Ultrascale+ Zynq开发板。

## 文档

你可以在`./docs`文件夹中找到这些文档。

- [硬件手册](./docs/FZ3A-Hardware-Handbook.pdf)。百度也提供了它的[在线版本](https://ai.baidu.com/ai-doc/HWCE/8kq9b2121)。
- [PCB电路原理图](./docs/FZ3A-Schematic.pdf)
- [IO引脚分配](./docs/FZ3A-io-definition.xls)

上述文档都来自于ALINX，这块开发板的制造商。

这里不包括任何关于如何将EasyDL/PaddlePaddle模型部署到该开发板上的文档。如果需要的话，你可以访问百度的[官方在线文档](https://ai.baidu.com/ai-doc/HWCE/Yk3b86gvp)。

## 硬件开发相关

我已完成PYNQ框架到EdgeBoard Lite开发板的移植，并提供镜像文件的下载。
同时，我也一并提供了所需要的各种源代码。

### Vivado board files

它们在`./board_files`路径下。你可以阅读[其中的README文件](./board_files/README.md)了解更多内容。

### PYNQ镜像

该预编译的镜像文件基于PYNQ v2.7制作。因为它的容量（约10GB）超出了GitHub上传文件的上限，我将它放在了阿里云盘上。这是[下载链接](https://www.aliyundrive.com/s/6biJpMiKrpD)。

文件夹`./pynq`是编译PYNQ所需的开发板配置文件。如果你需要自己重头编译PYNQ，你可以阅读[我的博客文章](https://zhutmost.com/uncategorized/pynq-compile)。

## 转载许可与声明

除非文中注明，本仓库下所有文档均以[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/)协议发布。如需转载，请按照License的指示进行。所有的代码均以[MIT](./LICENSE)协议发布。

这个项目是我的个人项目，与Baidu官方没有任何关系。
