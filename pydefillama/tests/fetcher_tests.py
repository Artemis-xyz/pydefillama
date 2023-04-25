import unittest

import pydefillama as llama


class Test(unittest.TestCase):
    def test_fetch_all_protocols(self):
        protocols = llama.fetch_all_protocols()
        self.assertIsInstance(protocols, list)

        uniswap_v3_entry = list(
            filter(lambda protocol: protocol["name"] == "Uniswap V3", protocols)
        )
        self.assert_(len(uniswap_v3_entry) == 1)
        uniswap_v3_entry = uniswap_v3_entry[0]
        self.assert_(uniswap_v3_entry["symbol"] == "UNI")
        self.assert_(uniswap_v3_entry["parentProtocol"] == "parent#uniswap")
