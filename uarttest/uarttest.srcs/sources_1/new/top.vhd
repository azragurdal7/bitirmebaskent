
library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
use IEEE.STD_LOGIC_UNSIGNED.ALL;
use IEEE.STD_LOGIC_ARITH.ALL;




entity top is
  Port (
    clk :   in std_logic;
    tx_o :  out std_logic;
    rx_i :  in std_logic
   );
end top;

architecture Behavioral of top is

component uart_rx is
generic (
c_clkfreq		: integer := 100_000_000;
c_baudrate		: integer := 115_200
);
port (
clk				: in std_logic;
rx_i			: in std_logic;
dout_o			: out std_logic_vector (7 downto 0);
rx_done_tick_o	: out std_logic
);
end component;


component  uart_tx is
generic (
c_clkfreq		: integer := 100_000_000;
c_baudrate		: integer := 115_200;
c_stopbit		: integer := 2
);
port (
clk				: in std_logic;
din_i			: in std_logic_vector (7 downto 0);
tx_start_i		: in std_logic;
tx_o			: out std_logic;
tx_done_tick_o	: out std_logic
);
end component;

  signal tx_data : std_logic_vector (7 downto 0);
  signal tx_start : std_logic;
  signal tx_done_tick : std_logic;
  signal rx_data : std_logic_vector  (7 downto 0);
  signal rx_done_tick : std_logic;
  
  type states is (S_IDLE,next_state,next_state_1,tx_state);
  signal state : states := S_IDLE;
  
begin

  inst_uart_tx : uart_tx 
    generic map(
      c_clkfreq => 100_000_000,
      c_baudrate => 115_200,
      c_stopbit => 2  
    )
    port map(
      clk			   => 	    clk,
      din_i			   =>   tx_data,
      tx_start_i 	   => 	tx_start,
      tx_o			   =>   tx_o,
      tx_done_tick_o	=>  tx_done_tick      
    );
    
 inst_uart_rx : uart_rx 
   generic map(
     c_clkfreq => 100_000_000,
     c_baudrate => 115_200
   )
   port map(
     clk => clk,
     rx_i => rx_i,
     dout_o => rx_data,
     rx_done_tick_o =>  rx_done_tick 
   );



  P_FSM : process(clk)
  begin
    if(rising_edge(clk)) then
    case state is 
      when S_IDLE => 
        if(rx_done_tick = '1')then
          if(rx_data = x"AA") then
            state <= next_state;
          end if;
        end if;
        
       when next_state =>
         if(rx_done_tick = '1')then
            if(rx_data = x"BB") then
              state <= next_state_1 ;
            end if;
          end if;
        
        when next_state_1 => 
          tx_data <= x"FF";
          tx_start <= '1';
          state <= tx_state;
          
        when tx_state => 
          tx_start <= '0';
          if(tx_done_tick = '1') then
            state <= S_IDLE;
          end if;
          
    
    end case;
  end if;
  
  end process;

end Behavioral;
