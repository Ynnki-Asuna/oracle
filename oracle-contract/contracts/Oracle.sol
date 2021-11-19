// SPDX-License-Identifier: MIT
pragma solidity ^0.6.12;
pragma experimental ABIEncoderV2;

import "@openzeppelin/contracts/access/Ownable.sol";

contract Oracle is Ownable {

    address public operator;

    struct SymbolPrice {
        uint256 price;
        uint256 blockTimestampLast;
    }

    mapping(string => SymbolPrice) public prices;

    event PricePosted(string symbol, uint256 oldPrice, uint256 newPrice, uint256 blockTimestampLast);

    modifier onlyOperator() {
        require(msg.sender == operator, "Oracle: Caller is not the operator");
        _;
    }

    constructor() public {}

    function setOperator(address _operator) external onlyOwner {
        operator = _operator;
    }

    function updatePrice(string calldata _symbol, uint256 _price) external onlyOperator {
        require(bytes(_symbol).length != 0, 'Oracle: Symbol cannot be empty');
        require(_price != 0, 'Oracle: Price cannot be zero');
        emit PricePosted(_symbol, prices[_symbol].price, _price, now);
        prices[_symbol].price = _price;
        prices[_symbol].blockTimestampLast = now;
    }

    function getPrice(string calldata _symbol) external view returns (SymbolPrice memory) {
        require(bytes(_symbol).length != 0, 'Oracle: Symbol cannot be empty');
        return prices[_symbol];
    }
}