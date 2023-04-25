# pydefillama: a DefiLlama Python client

[![PyPi](https://github.com/Artemis-xyz/pydefillama/actions/workflows/python-package.yml/badge.svg?branch=main)](https://github.com/Artemis-xyz/pydefillama/actions/workflows/python-package.yml)
[![PyPi](https://img.shields.io/pypi/v/pydefillama)](https://pypi.org/project/pydefillama/)

An unofficial DeFiLlama wrapper built for data science workflows.

For detailed instructions on the endpoints, refer to the [API docs](https://defillama.com/docs/api).

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

## Run Tests

```
 python -m unittest discover
```

## Developing Locally

```
# install module without pip
python setup.py develop

# run shell to play around
ipython

# import and use module in python shell
import pydefillama as llama
...
```

## Contributing

If you would like to contribute to this project, please open an issue or submit a PR.
While we are open to all contributions, we would like to keep this project focused on data science workflows, which is why functions often return a pandas dataframe.
If you would like to use this API for other purposes, please consider forking this repo.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

We are thankful for the DefiLlama team for providing this open API. If you would like to support them, consider donating to them [here](https://defillama.com/donations).
