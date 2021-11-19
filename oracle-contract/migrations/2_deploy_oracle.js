const oracle = artifacts.require('Oracle');

// ++++++++++++++++  Main Migration ++++++++++++++++ 
const migration = async (deployer, network, accounts) => {
  await Promise.all([
      deploy(deployer, network, accounts)
  ]);
}

// ++++++++++++++++  Deploy Functions ++++++++++++++++ 
module.exports = migration;

async function deploy(deployer, network, accounts) { 
  console.log("[Oracle] Start deploy on Network= " + network);

  let deployer_account = accounts[0];

  console.log("[Oracle] Begin to deploy Oracle")
  await deployer.deploy(oracle);
  //set setOperator
  let oracleImpl = await new web3.eth.Contract(oracle.abi, oracle.address); 
  await oracleImpl.methods.setOperator('0x7Dd3Fd126e5D8Ea01BA2188c46C53c5540a36803').send({from:deployer_account});

  console.log("[Oracle] End");
}