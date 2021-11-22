// SPDX-License-Identifier: MIT
pragma solidity >=0.5.16 <=0.6.12;

import "truffle/Assert.sol";
import "truffle/DeployedAddresses.sol";
import "../contracts/Oracle.sol";

contract TestOracle {

  function testInitialPriceUsingDeployedContract() public {
    Oracle oracle = Oracle(DeployedAddresses.Oracle());

    uint test_price = 10000;
    oracle.setOperator(0x6ba94a11fB8CCF07638be72B19228796897479Bd);
    oracle.updatePrice("BNB", 10000);
    (uint256 Testprice,) = oracle.getPrice("BNB");

    Assert.equal(test_price, Testprice, "updatePrice failed");

  }

  function testInitialWithBNB() public {
    Oracle oracle = new Oracle();

    uint test_price = 10000;
    oracle.setOperator(0x6ba94a11fB8CCF07638be72B19228796897479Bd);
    oracle.updatePrice("BNB", 10000);
    (uint256 Testprice,) = oracle.getPrice("BNB");

    Assert.equal(test_price, Testprice, "updatePrice failed");

  }

}
