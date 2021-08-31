# How to Use Board Files in Vivado

Here are two methods to include the EdgeBoard board files in Vivado.

## Specify Search Paths in Vivado Initialization Script

We need to specify the third-part board_files folder in its initialization script `Vivado_init.tcl`.

In most cases, this file should be at `$HOME/.Xilinx/Vivado/` in Linux.
Vivado does not create this file by default, so you can create it by yourself.
For more details about `Vivado_init.tcl`, please read *Vivado Design Suite Tcl Command Reference Guide ([UG835](https://www.xilinx.com/support/documentation/sw_manuals/xilinx2021_1/ug835-vivado-tcl-commands.pdf))*.

**WARN**: Note that in some eariler Vivado versions, this file may be named as `init.tcl`.

The specific steps are as follows:
1. Clone this repository to your disk.

   `git clone https://github.com/zhutmost/edgeboard.git $THIS_REPO_ROOT`

2. Append the following statement to your `Vivado_init.tcl`.

   `set_param board.repoPaths [list "$THIS_REPO_ROOT/board_files"]`

These paths can also be added in the GUI using `Tools > Setting > XHub Store > Board Repository`.

## Copy Board Files into `board_files` folder (For Vivado <= v2020.2)

Vivado has pre-installed some board files in its installation directory. You can find `zcu102`, `zc706` and other boards in `$INSTALL_DIR/Vivado/<version>/data/boards/board_files`. You can put third-part board files into this folder.

For example, add the board_files of FZ3A to Vivado:
```
cp -r $THIS_REPO_ROOT/board_files/fz3a $INSTALL_DIR/Vivado/<version>/data/boards/board_files/
```

**WARN**: Vivado 2021.1 has removed the built-in board_files folder, so this methos is not recommended any longer.
