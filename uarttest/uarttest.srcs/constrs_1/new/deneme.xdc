############## Clock Definition ##################
create_clock -period 20 [get_ports clk]
set_property IOSTANDARD LVCMOS33 [get_ports clk]
set_property PACKAGE_PIN U18 [get_ports clk]

############## AX7020/AX7010 J11 ##################
set_property IOSTANDARD LVCMOS33 [get_ports rx_i]
set_property PACKAGE_PIN J19 [get_ports rx_i]

set_property IOSTANDARD LVCMOS33 [get_ports tx_o]
set_property PACKAGE_PIN K19 [get_ports tx_o]

# Eğer reset sinyaline ihtiyacınız olursa aşağıdaki satırların yorumunu kaldırabilirsiniz:
# set_property IOSTANDARD LVCMOS33 [get_ports rst_n]
# set_property PACKAGE_PIN N15 [get_ports rst_n]
