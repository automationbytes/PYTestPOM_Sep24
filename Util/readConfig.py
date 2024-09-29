import configparser
import os
config = configparser.RawConfigParser()
config.read("./Config/config.ini")



class readConfig:

    @staticmethod
    def getConfig(header,key):
        print(os.path.abspath("./Config/config.ini"))
        print(config.get(header,key))
        return config.get(header,key)


