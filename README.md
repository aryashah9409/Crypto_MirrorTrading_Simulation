# Crypto_MirrorTrading_Simulation
Simulates a mirror trading technique between a DEX and CEX on a real-time basis. (DEX: Uniswap, CEX: Binance, Asset: ETH)

### Disclaimer:
It should be noted that this is solely for research purposes to gain a better understanding of price movements in the crypto markets. I do not recommend using this script for trading purposes. Please do your own research about the outcomes of this trading technique while also keeping in mind ethical and legal aspects around mirror trading. Neither do I guarantee returns, and nor am I aware of the ethical or legal aspects of using this strategy.

### Instructions:
Running this code creates an excel file called “thread.xlsx” on the user’s machine. The file contains 3 sheets (for the 3 stablecoins used - DAI, USDT and USDC). 

One can change the time parameter (in seconds) on line 452 in the code to run the simulation for longer, default is set to 60 seconds. 

After running the simulation for hours, days or weeks, the data from all the three sheets can be used for analysis either together or separately for each individual stablecoin and ETH. 

Amount-in and amont-out in the excel file is shown from Uniswap's perspective. Look at this data from the trader's perspective, for eg. ETH swapped for USDT is taken as ETH sold __(this will be reflected as ETH amount in and USDT amount out on the excel sheet from Uniswap's perspective, so make sure you view this as ETH sold and not ETH bought)__. Mirror this ETH sale on Binance and calculate the profit/loss. 

Similarly, continue to mirror trade each Uniswap transaction on Binance at real-time respective prices and then calculate the total net profit/loss position over the entire run time period. 

The excel fetches the real time trades from Uniswap and the corresponding ETH prices prevalent on Binance at the time of each Uniswap trade. This data is used to do your own mirror calculations like I explained above. 

Continue those calculations in the same excel file. I am attaching a demo file called "demo_1_5hrs.xlsm" that shows my calculation for one of the stablecoins and ETH, over 5 hours of run time. 

In demo_1_5hrs.xlsm, a range of net profit/loss position is calculated keeping in mind the time lag between querying the trade from Uniswap and executing it's mirror transaction on Binance. This is done by taking the corresponding ETH price on Binance just as it is fetched by the script, as one end of the range. The other end of the range considers the ETH price at the time of the next immediate query made by the script, accounting for the changed ETH price after the slight delay that might happen during execution. (Excel macros have been used to do this last bit of calculation, thus the file has an extension of .xlsm. To view this, enable macros when you download and open the file.)



