from fastapi import APIRouter
import json
from v1.utils.read_data import get_df, TARGET_COLS


router = APIRouter(prefix="/getData")


df = get_df("1e5ENZNsD10pWJ0ZxzLngf1N5eh2CfkoT", "data\\hackathon_data")


@router.get("/byRegion")
def get_data_by_region(region: str) -> dict:
    return df.loc[df["region"]==region].to_dict(orient="records")[0]


@router.get("/byCriterion")
def get_data_by_criterion(criterion: str) -> dict:
    data = {}
    for col in TARGET_COLS:
        data[col] = {"region": df.loc[:, "region"].to_list(), criterion: df.loc[:, criterion].to_list(), col: df.loc[:, col].to_list()}
    
    return data
    