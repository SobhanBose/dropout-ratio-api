import pandas as pd
import os
from v1.utils.download_data import getGoogleSeetAsCSV

TARGET_COLS = ['dr_primary_girls', 'dr_primary_boys', 'dr_primary_overall',
       'dr_upper_primary_girls', 'dr_upper_primary_boys',
       'dr_upper_primary_overall', 'dr_secondary_girls', 'dr_secondary_boys',
       'dr_secondary_overall']

NAME_MAPPING = {"region": "State/UT",
                  "lit_rate": "Literacy rate(2011)",
                  "pci": "Per capita income",
                  "schools_urban": "Schools (urban)",
                  "schools_rural": "Schools (rural)",
                  "schools_total": "Schools (total)",
                  "gpi_primary": "Gender Parity Index (primary)",
                  "gpi_upper_primary": "Gender Parity Index (upper primary)",
                  "gpi_secondary": "Gender Parity Index (secondary)",
                  "hdi": "Human Development Index",
                  "unemp_rate": "Unemployment Rate",
                  "life_exp_girls": "Life Expectency (girls)",
                  "life_exp_boys": "Life Expectency (boys)",
                  "num_teachers_primary": "No of teachers (primary)",
                  "num_teachers_upper_primary": "No of teachers (upper primary)",
                  "num_teachers_secondary": "No of teachers (secondary)",
                  "num_teachers_total": "No of teachers (total)",
                  "num_students_primary": "No of students (primary)",
                  "num_students_upper_primary": "No of students (upper primary)",
                  "num_students_secondary": "No of students (secondary)",
                  "num_students_total": "No of students (total)",
                  "ptr_primary": "PTR (primary)",
                  "ptr_upper_primary": "PTR (upper primary)",
                  "ptr_secondary": "PTR (secondary)",
                  "ptr_overall": "PTR (overall)",
                  "enrol_rate_primary": "Enrollment rate(primary)",
                  "enrol_rate_upper_primary": "Enrollment rate(upper primary)",
                  "enrol_rate_secondary": "Enrollment rate(secondary)",
                  "elec": "Availability of electricity",
                  "lib": "Availability of library with books",
                  "water": "Availability of drinking water",
                  "med": "Availability of medical facility",
                  "dr_primary_girls": "Dropout Ratio (primary) (girls)",
                  "dr_primary_boys": "Dropout Ratio (primary) (boys)",
                  "dr_primary_overall": "Dropout Ratio (primary) (overall)",
                  "dr_upper_primary_girls": "Dropout Ratio (upper primary) (girls)",
                  "dr_upper_primary_boys": "Dropout Ratio (upper primary) (boys)",
                  "dr_upper_primary_overall": "Dropout Ratio (upper primary) (overall)",
                  "dr_secondary_girls": "Dropout Ratio (secondary) (girls)",
                  "dr_secondary_boys": "Dropout Ratio (secondary) (boys)",
                  "dr_secondary_overall": "Dropout Ratio (secondary) (overall)"
                }

def get_df(spreadsheet_id: str, outFile: str) -> pd.DataFrame:
#     getGoogleSeetAsCSV(spreadsheet_id, outFile)
    filepath = f'{os.getcwd()}/v1/{outFile}.csv'
#     filepath = f'{outFile}.csv'
    print(filepath)
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
                  "Human Development Index": "hdi",
                  "Unemployment Rate": "unemp_rate",
                  "Life Expectency (girls)": "life_exp_girls",
                  "Life Expectency (boys)": "life_exp_boys",
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
