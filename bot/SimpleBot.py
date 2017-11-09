#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from entities.Fund import Fund
from Config import Config
from TRTApi import TRTApi


import os
import pickle
import logging

class SimpleBot:
    def __init__(self, dbManager, configurationFilePath):
        self.dbManager = dbManager
        self.configurationFilePath = configurationFilePath
        self.status = {}

        self.orderManager = False

        try:
            self.configuration = Config.readFile(self.configurationFilePath)
        except Exception as e:
            print("cannot find configuration file %s " % self.configurationFilePath)
            exit()

        logging.basicConfig(
            filename=self.configuration["logFilePath"],
            format='%(asctime)s - %(levelname)s:%(message)s',
            datefmt='%Y-%m-%d %H:%M:%S',
            level=logging.DEBUG
        )


        try:
            self.loadStatus()
            logging.info("status loaded")
            logging.debug(self.status)
        except FileNotFoundError as e:
            logging.info("creating default status")
            self.createStartingStatus()
            self.saveStatus()


    def createStartingStatus(self):
        self.status = {
            "configuration": self.configuration,
            "positions":[]
        }

# position: {
#     price: xxx,
#     amount: xxx,
#     buying_fee: xxx,
#     fee_percentage:
# }

    def sendSellOrder(self, position, price):
        logging.info("sending selling order")
        try:
            self.orderManager.sell(position["amount"], price)
        except Exception as e:
            raise e

    def sendBuyOrder(self, amount, price):
        logging.info("sending selling order")
        try:
            self.orderManager.buy(amount, price)
        except Exception as e:
            raise e

    def closePositions(self):
        current_bid = self.lastRecord["bid"] # da prendere il primo elemento dell'orderbook!!

        for p in self.status["positions"]:

            # fare filter nel for:
            if(p["delete"] == True):
                continue

            selling_price = p["amount"] * current_bid
            selling_fee = selling_price * p["fee_percentage"]

            buying_total = p["amount"] * p["price"] + p["buying_fee"]

            gain = selling_price - selling_fee - buying_total


            if gain > self.status["configuration"]["min_gain_eur"]:
                # evado l'ordine per intero;
                # @todo: verificare top N record per invio più ordini, oppure evasione parziale
                if current_bid["amount"] >= p["amount"]:
                    logging.info("min_gain_eur reached (%s)!" % gain)
                    try:
                        result = sendSellOrder(p, current_bid)
                        p["delete"] = True

                    except Exception as e:
                        logging.info("closing position conditions met but could not complete SELL order")

        #cancella tutte le posizioni con "delete" a true


    def openPositions(self):

        firstOrderBookAsk = {}


        if(condizioni_di_apertura_relativa_alla_media):
            calculated_amount = self.status["configuration"]["position_eur"] / firstOrderBookAsk["ask"]
            rounded_amount = float("{0:.4f}".format(calculated_amount))
            if firstOrderBookAsk["quantity"] >= rounded_amount:
                logging.info("open position condition met. opening at %s * %s" % (self.lastRecord["ask"], rounded_amount))

                try:
                    new_position = sendBuyOrder(rounded_amount, firstOrderBookAsk["ask"])
                except Exception as e:
                    logging.info("open position met but could not complete BUY order")

                    raise e

        else:
            logging.info("open position condition NOT met. skipping.")


    def setOrderManager(self, orderManager):
        self.orderManager = orderManager



# STATUS HANDLING

    def saveStatus(self):
        try:
            pickle.dump( self.status, open(self.configuration["statusFilePath"], "wb"))
        except Exception as e:
            logging.error("cannot save status to %s" % self.configuration["statusFilePath"])
            raise e

        logging.info("saved status file to %s" % self.configuration["statusFilePath"])
        return

    def loadStatus(self):
        statusFilePath = self.configuration["statusFilePath"]
        logging.info("loading status file from: %s " % statusFilePath)

        try:
            self.status = pickle.load(open(statusFilePath, "rb"))
        except FileNotFoundError as e:
            logging.warning("cannot find status file: %s " % statusFilePath)
            raise e

        return


        def updateStatus(self):
            pass
# MAIN

    def run(self):

        if not self.orderManager:
            raise Exception("OrderManager not set! use setOrderManager() to setup the bot")

        self.lastRecord = self.dbManager.getLastFund(Fund.ID_BTCEUR)

        closePositions()
        updateStatus()

        if len(self.status["positions"]) < self.status["configuration"]["max_positions"]:
            logging.info("found %s positions, checking to open new one..." % len(self.status["positions"]))
            openPositions()
            updateStatus()
        else:
            logging.info("max_positions reached: %s, skipping new positions check", self.status["configuration"]["max_positions"])
