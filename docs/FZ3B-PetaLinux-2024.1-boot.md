FZ3B 上也复现了同款问题（同样的三行 BL31 卡死），并且已经定位 + 解决了，给后来者留个结论——
这个问题有**两层**，需要分别修：

**① 串口只见 BL31 三行**：sdbuild 自动生成的串口配置为 FSBL/PMU/内核 = UART0、
TF-A = UART1，而 FZ3 系列的调试口接在 **UART1**（官方手册 USB_UART 接口表：MIO24/25）。
只有 TF-A 的输出接对了线，U-Boot 和内核都在向未接线的 UART0 输出。
修复：project-spec/configs/config 里把 FSBL/PMU/Serial 三项改为 PSU_UART_1，重编 dtb/BOOT.BIN。

**② 修好串口后才能看到的第二层**：`Kernel panic - VFS: Unable to mount root fs on
unknown-block(179,10)`。FZ3 系列是 **eMMC + TF 卡双存储**：eMMC = mmcblk0（出厂分区，
非 ext4）、TF 卡 = mmcblk1。而模板 bootargs 是 `root=/dev/mmcblk0p2`——指向的是
eMMC 的出厂分区，不是 TF 卡上的 rootfs。
修复：`sdbuild/boot/meta-pynq/recipes-bsp/device-tree/files/pynq_bootargs.dtsi` 中
root=/dev/mmcblk0p2 → /dev/mmcblk1p2，重编 dtb/image.ub。

两处都改后，自编译的 PYNQ 3.1.2（PetaLinux 2024.1）在 FZ3B 上正常启动到 Jupyter。
完整排查过程与分步教程：https://lmy271828.github.io/fz3b/01-build-image/
