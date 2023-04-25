import numpy as np
import pandas as pd
import requests

from .utils import FEE_TYPE

# TODO: Add docstrings


def _convert_df_column_to_date(
    df, date_column="date", format=None, unit=None
) -> pd.DataFrame:
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
            "parentProtocol": raw_protocol.get("parentProtocol"),
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
    df.columns = ["date", "tvl"]
    df = _convert_df_column_to_date(df, unit="s")
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


def fetch_chain_tvl(chain_name: str):
    url = f"https://api.llama.fi/v2/historicalChainTvl/{chain_name}"
    r = requests.get(url)
    data = r.json()
    df = pd.DataFrame(data)
    df.columns = ["date", "tvl"]
    df = _convert_df_column_to_date(df, unit="s")
    return df


def fetch_protocol_ids_that_list_fees() -> list[str]:
    url = "https://api.llama.fi/overview/fees?excludeTotalDataChartBreakdown=true&excludeTotalDataChart=true"
    r = requests.get(url)
    # protocols field is a lie - includes chains and protocols
    protocol_ids = [
        protocol["defillamaId"]
        for protocol in r.json()["protocols"]
        if protocol["protocolType"] == "protocol"
    ]
    return protocol_ids


def fetch_chain_names_that_list_fees() -> list[str]:
    url = "https://api.llama.fi/overview/fees?excludeTotalDataChartBreakdown=true&excludeTotalDataChart=true"
    r = requests.get(url)
    # protocols field is a lie - includes chains and protocols
    chain_names = [
        protocol["name"]
        for protocol in r.json()["protocols"]
        if protocol["protocolType"] == "chain"
    ]
    return chain_names


def fetch_protocol_fees(protocol_slug: str, fee_type: FEE_TYPE) -> pd.DataFrame:
    url = f"https://api.llama.fi/summary/fees/{protocol_slug}?dataType={fee_type.value}"
    r = requests.get(url)
    all_fees = r.json()["totalDataChart"]
    df = pd.DataFrame(all_fees, columns=["date", protocol_slug])
    df = df.fillna(np.nan).replace([np.nan], [None])
    df = _convert_df_column_to_date(df, "date", unit="s")
    df.columns = ["date", fee_type.value]
    return df


def fetch_chain_fees(chain_name: str, fee_type: FEE_TYPE) -> pd.DataFrame:
    return fetch_protocol_fees(chain_name, fee_type)


def fetch_protocol_ids_that_list_dex_volumes():
    url = "https://api.llama.fi/overview/dexs?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume"
    r = requests.get(url)
    supported_protocol_and_chain_ids = [
        protocol["defillamaId"] for protocol in r.json()["protocols"]
    ]
    protocols = fetch_all_protocols()
    protocol_ids = [
        protocol["defillama_id"]
        for protocol in protocols
        if protocol["defillama_id"] in supported_protocol_and_chain_ids
    ]
    return protocol_ids


def fetch_chain_names_that_list_dex_volumes() -> list[str]:
    url = "https://api.llama.fi/overview/dexs?excludeTotalDataChart=true&excludeTotalDataChartBreakdown=true&dataType=dailyVolume"
    r = requests.get(url)
    assets = r.json()["allChains"]
    return assets


def fetch_protocol_dex_volumes(protocol_slug: str) -> pd.DataFrame:
    url = f"https://api.llama.fi/summary/dexs/{protocol_slug}?excludeTotalDataChart=false&excludeTotalDataChartBreakdown=true&dataType=dailyVolume"
    r = requests.get(url)
    results = r.json()["totalDataChart"]
    df = pd.DataFrame(results)
    df.columns = ["date", "volume"]
    df = _convert_df_column_to_date(df, unit="s")
    df = df.fillna(np.nan).replace([np.nan], [None])
    return df


def fetch_chain_dex_volumes(chain_name) -> pd.DataFrame:
    url = f"https://api.llama.fi/overview/dexs/{chain_name}?excludeTotalDataChart=false&excludeTotalDataChartBreakdown=true&dataType=dailyVolume"
    r = requests.get(url)
    results = r.json()["totalDataChart"]
    df = pd.DataFrame(results)
    df.columns = ["date", "volume"]
    df = _convert_df_column_to_date(df, unit="s")
    df = df.fillna(np.nan).replace([np.nan], [None])
    return df
