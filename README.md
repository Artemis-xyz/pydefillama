# pydefillama: a DefiLlama Python client

[![PyPi](https://github.com/Artemis-xyz/pydefillama/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/Artemis-xyz/pydefillama/actions/workflows/python-package.yml)
[![PyPi](https://img.shields.io/pypi/v/pydefillama)](https://pypi.org/project/pydefillama/)

An unofficial DeFiLlama wrapper built for data science workflows. 

For detailed instructions on the endpoints, refer to the [API docs](https://defillama.com/docs/api)

## Installation
`pip install pydefillama`

## Usage 
```
import pydefillama as llama

# fetch all protocols
protocols = llama.fetch_all_protocols()

# fetch TVL for a protocol 
llama.fetch_protocol_tvl(protocols[0]["slug"])

# fetch all chains 
chains = llama.fetch_all_chains()

# fetch TVL for a chain
llama.fetch_chain_tvl(chains["name"])
```

Full list of supported functions [here](https://github.com/Artemis-xyz/pydefillama/blob/main/pydefillama/src/fetcher.py).
