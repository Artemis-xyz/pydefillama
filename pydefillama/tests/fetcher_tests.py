import unittest

import pandas as pd

import pydefillama as llama


class Test(unittest.TestCase):
    def test_fetch_all_protocols(self):
        protocols = llama.fetch_all_protocols()
        self.assertIsInstance(protocols, list)

        uniswap_v3_entry = list(
            filter(lambda protocol: protocol["name"] == "Uniswap V3", protocols)
        )
        self.assertTrue(len(uniswap_v3_entry) == 1)
        uniswap_v3_entry = uniswap_v3_entry[0]
        self.assertTrue(uniswap_v3_entry["symbol"] == "UNI")
        self.assertTrue(uniswap_v3_entry["parentProtocol"] == "parent#uniswap")

    def test_fetch_protocol_tvl(self):
        df = llama.fetch_protocol_tvl("uniswap-v3")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.columns[0] == "date")
        self.assertTrue(df.columns[1] == "tvl")
        self.assertTrue(df.iloc[-1]["tvl"] > 0)

    def test_fetch_chain_tvl(self):
        df = llama.fetch_chain_tvl("ethereum")
        self.assertIsInstance(df, pd.DataFrame)
        self.assertTrue(df.columns[0] == "date")
        self.assertTrue(df.columns[1] == "tvl")
        self.assertTrue(df.iloc[-1]["tvl"] > 0)


# TODO: Add more tests
