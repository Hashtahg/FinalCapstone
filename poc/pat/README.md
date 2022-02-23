# POC

## Compile and Deploy Contract

you'll need to open Ganache, Remix and Pinata

1. Upload Passenger.sol to Remix IDE
2. Compile Passenger.sol
3. From left pane select contract: Passenger.sol 
4. Launch metamask
5. For Environment select Injected Web3
6. Deploy contract and MetaMask will open. Press Confirm
7. From the left pane expand the contract
8. Select a second account from Metamask (confirm in metamask its connected). This is the recipient
9. Expand awardItem to expose 3 fields: recipient, hash, metadata
for Recipient enter the recipient metamask account, for hash enter the cid from Pinata (Qmaktte2Wy3gGUvUmTeQFin3xWV3vZmzen1zkANqYiB7Qd)
for metadata you use the gateway plus the cid 
(https://gateway.pinata.cloud/ipfs/Qmaktte2Wy3gGUvUmTeQFin3xWV3vZmzen1zkANqYiB7Qd)
10. confirm the the tokenURI by entering a tokenid value of 1 then press call and the tokenURI is displayed



