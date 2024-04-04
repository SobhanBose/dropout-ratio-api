from fastapi import APIRouter
import json
from v1.utils.read_data import get_df, TARGET_COLS, NAME_MAPPING


router = APIRouter(prefix="/getData")


df = get_df("1e5ENZNsD10pWJ0ZxzLngf1N5eh2CfkoT", "data/hackathon_data")
# df = get_df("1e5ENZNsD10pWJ0ZxzLngf1N5eh2CfkoT", "../data/hackathon_data")


@router.get("/byRegion")
def get_data_by_region(region: str) -> dict:
    return df.loc[df["region"]==region].to_dict(orient="records")[0]


@router.get("/byCriterion")
def get_data_by_criterion(criterion: str) -> dict:
    data = {}
    for col in TARGET_COLS:
        data[col] = {"region": df.loc[:, "region"].to_list(), criterion: df.loc[:, criterion].to_list(), col: df.loc[:, col].to_list()}
    
    return data


@router.get("/byCriterionFormatted")
def get_data_by_criterion_formatted(criterion: str) -> dict:
    data = {}
    for col in TARGET_COLS:
        data["title"] = NAME_MAPPING[criterion]
        data[col] = {"label": f'{NAME_MAPPING[criterion]} vs {NAME_MAPPING[col]}', "region": df["region"].to_list(), "data": [{"x": x, "y": y} for x, y in zip(df[criterion].to_list(), df[col].to_list())]}
    
    return data
    