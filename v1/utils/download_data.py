import requests

def getGoogleSeetAsCSV(spreadsheet_id: str, outFile: str) -> None:
    url = f'https://docs.google.com/spreadsheets/d/{spreadsheet_id}/export?format=csv'
    response = requests.get(url)
    if response.status_code == 200:
        filepath = f'{outFile}.csv'
        with open(filepath, 'wb') as f:
            f.write(response.content)
            print(f'CSV file saved to: {filepath}')    
    else:
        print(f'Error downloading Google Sheet: {response.status_code}')