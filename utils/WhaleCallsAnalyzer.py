import re

# liquidated long
# Okcoin $BTCUSD Quarterly futures has liquidated a long position of 985 contract at 5,865.45 - 2017-10-22 10:27:12

# contract holder decrease
# OKcoin top #3 $BTCUSD contract holder has decreased their position by 4787 contracts

# contract holder increase
# OKcoin top #1 $BTCUSD contract holder has increased their position by 40164 contracts

# matchObj = re.match( r'(.*) are (.*?) .*', text, re.M|re.I)

class WhaleCallsAnalyzer:
    def __init__(self):
        self.text = ""

    def BTCUSDRelated():
        return "BTCUSD" in self.text

    def checkLiquidateLong(self, text):
        liquidatedLongRE = re.match(r'(.*) has liquidated a long position of (.*?) contract at (.*) - (.*)', text, re.M|re.I)


        if liquidatedLongRE:
            result = {}
            result["who"] = liquidatedLongRE.group(1)
            result["amount"] = int(liquidatedLongRE.group(2))
            result["action"] = "liquidated"
            # result["value"] = liquidatedLongRE.group(3)
            return result

        return False

    def checkContractHolder(self, text):
        checkContractHolderRE = re.match(r'(.*) contract holder has (increased|decreased) their position by (.*?) contracts', text, re.M|re.I)


        if checkContractHolderRE:
            result = {}
            result["who"] = checkContractHolderRE.group(1)
            result["action"] = checkContractHolderRE.group(2)
            result["amount"] = int(checkContractHolderRE.group(3))
            if result["action"] == "decreased":
                result["amount"] = -result["amount"]

            return result

        return False

    def analyze(self, text):
        self.text = text

        result = self.checkLiquidateLong(self.text)
        if result:
            return result

        result = self.checkContractHolder(self.text)
        if result:
            return result

        return False



