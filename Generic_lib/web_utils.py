import xlrd
from config import *
# c_path = r"C:\Users\AS064243\OneDrive - Cerner Corporation\Documents\Learning\demo_FW\testData\registerPage.xlsx"

class Generic():
    def read_excel(self):
        wb = xlrd.open_workbook(testdata_path)
        ws = wb.sheet_by_name("credentials")
        data = ws.get_rows()
        login_credentials={}
        for item in data:
            login_credentials[item[0].value] = item[1].value
        return (login_credentials)


