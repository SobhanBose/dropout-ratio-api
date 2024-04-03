import pandas as pd
from v1.utils.download_data import getGoogleSeetAsCSV

TARGET_COLS = ['dr_primary_girls', 'dr_primary_boys', 'dr_primary_overall',
       'dr_upper_primary_girls', 'dr_upper_primary_boys',
       'dr_upper_primary_overall', 'dr_secondary_girls', 'dr_secondary_boys',
       'dr_secondary_overall']

def get_df(spreadsheet_id: str, outFile: str) -> pd.DataFrame:
    getGoogleSeetAsCSV(spreadsheet_id, outFile)
    filepath = f'{outFile}.csv'
    df = pd.read_csv(filepath, index_col="id")

    rename_mapping = {"State/UT": "region",
                    "Literacy rate(2011)": "lit_rate",
                    "Per capita income": "pci",
                    "Schools (urban)": "schools_urban",
                    "Schools (rural)": "schools_rural",
                    "Schools (total)": "schools_total",
                    "Gender Parity Index (primary)": "gpi_primary",
                    "Gender Parity Index (upper primary)": "gpi_upper_primary",
                    "Gender Parity Index (secondary)": "gpi_secondary",
                    "No of teachers (primary)": "num_teachers_primary",
                    "No of teachers (upper primary)": "num_teachers_upper_primary",
                    "No of teachers (secondary)": "num_teachers_secondary",
                    "No of teachers (total)": "num_teachers_total",
                    "No of students (primary)": "num_students_primary",
                    "No of students (upper primary)": "num_students_upper_primary",
                    "No of students (secondary)": "num_students_secondary",
                    "No of students (total)": "num_students_total",
                    "PTR (primary)": "ptr_primary",
                    "PTR (upper primary)": "ptr_upper_primary",
                    "PTR (secondary)": "ptr_secondary",
                    "PTR (overall)": "ptr_overall",
                    "Enrollment rate(primary)": "enrol_rate_primary",
                    "Enrollment rate(upper primary)": "enrol_rate_upper_primary",
                    "Enrollment rate(secondary)": "enrol_rate_secondary",
                    "Availability of electricity": "elec",
                    "Availability of library with books": "lib",
                    "Availability of drinking water": "water",
                    "Availability of medical facility": "med",
                    "Dropout Ratio (primary) (girls)": "dr_primary_girls",
                    "Dropout Ratio (primary) (boys)": "dr_primary_boys",
                    "Dropout Ratio (primary) (overall)": "dr_primary_overall",
                    "Dropout Ratio (upper primary) (girls)": "dr_upper_primary_girls",
                    "Dropout Ratio (upper primary) (boys)": "dr_upper_primary_boys",
                    "Dropout Ratio (upper primary) (overall)": "dr_upper_primary_overall",
                    "Dropout Ratio (secondary) (girls)": "dr_secondary_girls",
                    "Dropout Ratio (secondary) (boys)": "dr_secondary_boys",
                    "Dropout Ratio (secondary) (overall)": "dr_secondary_overall"}
    
    df.rename(columns=rename_mapping, inplace=True, copy=False)

    return df
