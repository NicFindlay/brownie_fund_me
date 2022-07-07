from brownie import FundMe, network, config, MockV3Aggregator
from scripts.helpful_scripts import get_account, deploy_mocks
from web3 import Web3


def deploy_fund_me():
    account = get_account()
    # pass the price feed address to our fundme contract

    # if we are on a persistent network, use associated address
    # otherwise use mocks
    if network.show_active() != "development":
        price_feed_address = config["networks"][network.show_active()][
            "eth_used_price_feed"
        ]
    else:
        deploy_mocks()
        print("Mocks Deployed")

    fund_me = FundMe.deploy(
        price_feed_address,
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"Contract deployed to {fund_me.address}")


def main():
    deploy_fund_me()
