const patent=artifacts.require('Patent');

module.exports=function(deployer){
    deployer.deploy(patent);
}