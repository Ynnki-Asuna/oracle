import { network, ethers } from 'hardhat';
import { Contract, ContractFactory, BigNumber, utils } from 'ethers';
import { encodeParameters, wait } from './utils';

async function main() {
    const { provider } = ethers;
    const [ operator ] = await ethers.getSigners();

    const estimateGasPrice = await provider.getGasPrice();
    const gasPrice = estimateGasPrice.mul(3).div(2);
    console.log(`Gas Price: ${ethers.utils.formatUnits(gasPrice, 'gwei')} gwei`);
    const override = { gasPrice };

    console.log(`====================Do your bussiness =======================`)
    const Oracle = await ethers.getContractFactory("Oracle");
    console.log("Deploying Oracle...");
    let oracle = await Oracle.deploy();
    await oracle.deployed();
    console.log("Oracle Address is: ", oracle.address);
    let tx1 = await oracle.setOperator('0x7Dd3Fd126e5D8Ea01BA2188c46C53c5540a36803');
    await wait(ethers, tx1.hash, 'setOperator.....');
    // let tx2 = await oracle.updatePrice('ETH', '1000000000000000');
    // await wait(ethers, tx2.hash, 'updatePrice.....');
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });