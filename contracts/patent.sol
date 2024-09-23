// SPDX-License-Identifier: MIT
pragma solidity 0.8.19;

contract Patent {
  address admin;
    struct patent {
        uint id;
        string title;
        string description;
        address owner;
        bool isActive;
    }
    constructor() {
     admin=msg.sender;
    }

    mapping(uint => patent)  patents;
    

    // Function to register a patent
    function registerPatent( uint id,string memory _title, string memory _description,address owner) public {
        require(admin==msg.sender);
      
        require(!patents[id].isActive);
        //record create
        patent memory new_patent=patent(id,_title,_description,owner,true);
        //record map
        patents[new_patent.id]=new_patent;
    }

    // Function to transfer ownership of a patent
    function transferOwnership(uint id, address _newOwner) public {
        require(patents[id].isActive);
        // require(msg.sender==patents[id].owner);
        patents[id].owner=_newOwner;

    }

    // Function to verify if a patent exists by patentId
    function verifyPatent(uint id) public view returns (patent memory) {
        return (patents[id]);

    }

   
}
