# Crypto_MirrorTrading_Simulation
Simulates a mirror trading technique between a DEX and CEX on a real-time basis. 

### Disclaimer:
It should be noted that this is solely for research purposes to gain a better understanding of price movements in the crypto markets. I do not recommend using this script for trading purposes. Please do your own research about the outcomes of this trading technique while also keeping in mind ethical and legal aspects around mirror trading. Neither do I guarantee returns, and nor am I aware of the ethical or legal aspects of using this strategy.

### Instructions:
Running this code creates an excel file called “thread.xlsx” on the user’s machine. The file contains 3 sheets (for the 3 stablecoins used - DAI, USDT and USDC). 

One can change the time parameter (in seconds) on line ** in the code to run the simulation for longer, default is set to 60 seconds. 

After running the simulation for hours, days or weeks, the data from all the three sheets can be used for analysis either together or separately for each individual stablecoin and ETH. 

Amount-in and amont-out is shown from Uniswap's perspective. Look at this data from the trader's perspective for eg. ETH swapped for USDT is taken as ETH sold __(this will be reflected as ETH amount in and USDT amount out on the excel sheet from Uniswap's perspective)__. Mirror this ETH sale on Binance and calculate the profit/loss. 

Similarly, continue to mirror trade each Uniswap transaction on Binance at real-time respective prices and then calculate the total net profit/loss position over the entire run time period. 