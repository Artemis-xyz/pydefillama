import numpy as np
import pandas as pd
import requests


def convert_df_column_to_date(df, date_column="date", format=None, unit=None):
    if unit is not None:
        df[date_column] = pd.to_datetime(df[date_column], unit=unit)
    elif format is not None:
        df[date_column] = pd.to_datetime(df[date_column], format=format)
    else:
        df[date_column] = pd.to_datetime(df[date_column])
    df[date_column] = df[date_column].dt.date
    return df


def fetch_all_protocols() -> list[dict]:
    def _transform_raw_protocol(raw_protocol):
        return {
            "defillama_id": raw_protocol.get("id"),
            "name": raw_protocol.get("name"),
            "symbol": raw_protocol.get("symbol"),
            "chain": raw_protocol.get("chain"),
            "logo": raw_protocol.get("logo"),
            "twitter": raw_protocol.get("twitter"),
            "url": raw_protocol.get("url"),
            "gecko_id": raw_protocol.get("gecko_id"),
            "category": raw_protocol.get("category"),
            "slug": raw_protocol.get("slug"),
            "parent_protocol": raw_protocol.get("parentProtocol"),
        }

    url = "https://api.llama.fi/protocols"
    r = requests.get(url)
    raw_protocols = r.json()
    protocols_keys_kept = [
        _transform_raw_protocol(raw_protocol) for raw_protocol in raw_protocols
    ]
    return protocols_keys_kept


def fetch_protocol_tvl(protocol_slug: str) -> pd.DataFrame:
    url = f"https://api.llama.fi/protocol/{protocol_slug}"
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame(data["tvl"])
    df = convert_df_column_to_date(df, unit="s")
    return df


def fetch_all_chains() -> list[dict]:
    def _transform_raw_chain(raw_chain):
        return {
            "gecko_id": raw_chain.get("gecko_id"),
            "tokenSymbol": raw_chain.get("tokenSymbol"),
            "cmcId": raw_chain.get("cmcId"),
            "name": raw_chain.get("name"),
            "chainId": raw_chain.get("chainId"),
        }

    url = "https://api.llama.fi/chains"
    r = requests.get(url)
    raw_chains = r.json()
    chains_keys_kept = [_transform_raw_chain(raw_chain) for raw_chain in raw_chains]
    return chains_keys_kept


def fetch_chain_tvl(chain_name):
    url = f"https://api.llama.fi/v2/historicalChainTvl/{chain_name}"
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame(data)
    df = convert_df_column_to_date(df, unit="s")
    return df
