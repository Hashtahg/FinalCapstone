# POC dApp

## Compile and Deploy Contract
1) Compile and deploy artwork.sol contract in Remix
2) Add the web3 provider and contract address in the .env file as in below example
 * WEB3_PROVIDER_URI=http://127.0.0.1:7545
 * SMART_CONTRACT_ADDRESS= "0x3Ae4c75756eeD5beE06be3d1Bd4D06bF3157d31F" or deploy new contract and use that address.
3) from command line enter: streamlit run app.py to launch app in browser
4) Enter the URI from IPFS into the field 'URI to the boarding pass token'
 * https://ipfs.io/ipfs/Qmaktte2Wy3gGUvUmTeQFin3xWV3vZmzen1zkANqYiB7Qd?filename=grapes.jpeg
5) click Register token
6) Click 'Display Token'. This is the token image
7) Click the link to receive your boarding pass


## Compile and Deploy Passenger.sol

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
