# FlashSwapForCofixAndUni
Use dydx to arbitrage between Cofix and Uni

### Contract part

#### Use flash loan method

```
function initiateFlashLoan(uint256 _amount)
        external
    {
        ISoloMargin solo = ISoloMargin(dydxAddress);
        uint256 marketId = _getMarketIdFromTokenAddress(dydxAddress, WETHAddress);
        uint256 repayAmount = _getRepaymentAmountInternal(_amount);
        IERC20(WETHAddress).approve(dydxAddress, repayAmount);

        Actions.ActionArgs[] memory operations = new Actions.ActionArgs[](3);
        operations[0] = _getWithdrawAction(marketId, _amount);
        operations[1] = _getCallAction(
            abi.encode(MyCustomData({token: WETHAddress, repayAmount: repayAmount}))
        );
        operations[2] = _getDepositAction(marketId, repayAmount);

        Account.Info[] memory accountInfos = new Account.Info[](1);
        accountInfos[0] = _getAccountInfo();

        solo.operate(accountInfos, operations);
    }
```

#### Operations in the flash loan process

```
function callFunction(
        address sender,
        Account.Info memory account,
        bytes memory data
    ) public {
        MyCustomData memory mcd = abi.decode(data, (MyCustomData));
        uint256 tokenBalanceBefore = IERC20(mcd.token).balanceOf(address(this));
        // money
        // WETH->ETH
        WETH9(WETHAddress).withdraw(tokenBalanceBefore);
        // ETH->USDT
        uint256 loopTimes = address(this).balance.div(cofixETHSapn);
        for(uint256 i = 0; i < loopTimes; i++) {
            CoFiXRouter(cofixRouter).swapExactETHForTokens{value:cofixETHSapn}(USDTAddress,cofixETHSapn.sub(nestPrice),1,address(this), address(this), uint256(block.timestamp).add(100));
        }
        // USDT->ETH
        uint256 usdtBalance = IERC20(USDTAddress).balanceOf(address(this));
        address[] memory uniData = new address[](2);
        uniData[0] = address(0xdAC17F958D2ee523a2206206994597C13D831ec7);
        uniData[1] = address(0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2);
        UniswapV2Router(uniRouter).swapExactTokensForETH(usdtBalance,1,uniData,address(this),uint256(block.timestamp).add(100));
        // ETH->WETH
        WETH9(WETHAddress).deposit{value:tokenBalanceBefore.add(2)};
        
        uint256 balOfLoanedToken = IERC20(mcd.token).balanceOf(address(this));
        require(
            balOfLoanedToken >= mcd.repayAmount,
            "Not enough funds to repay dydx loan!"
        );
        
    }
```

### python part

A scale with an upper limit of 3900 ETH with an interval of 300 ETH is used to circularly detect whether there is arbitrage space. The detailed parameters can be modified in the config.py file.
