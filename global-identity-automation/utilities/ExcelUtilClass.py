import os
import unittest
import pandas as pd

import xlrd
from api.noompy import NoomPy
from openpyxl import load_workbook, cell
from utilities.BaseClass import BaseClass


class ExcelUtil(BaseClass):

    def __init__(self, driver):
        self.driver = driver

    def test_getRowCount(self, filepath):
        print("strfile ===", self.filepath)
        wb = xlrd.open_workbook(self.filepath)
        sheet = wb.sheet_by_name("data")
        print("rows --", sheet.nrows)
        return sheet.nrows


    def test_getColCount(self, filepath):
        wb = xlrd.open_workbook(self.filepath)
        sheet = wb.sheet_by_name("data")
        print("cols---", sheet.ncols)
        return sheet.ncols


    filepath = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + "/resourcesOld/IDPData.xlsx"

    def test_getDataForCol(self, filepath, sheetname, coltocompare, colvalue, reqcolname):
        log = self.getLogging()
        noom = NoomPy(excel_path=self.filepath)
        select_query = "SELECT * FROM " + sheetname + " WHERE " + coltocompare + "=" + "{}".format(colvalue) + ""
        print("query ===", select_query)
        res = noom.select_data(select_query)
        get_col_value = noom.get_data(data=res, key=reqcolname)
        print("Fetched Value from sheet is  ======", get_col_value)
        return get_col_value

    def test_updateDataForCol(self, filepath, sheetname, requpdatecolname, requpdatecolvalue, coltocompare, colvalue):
        noom = NoomPy(excel_path=self.filepath)
        update_query = "UPDATE " + self.sheetname + " SET " + self.requpdatecolname + " = '" + self.requpdatecolvalue + "' WHERE " + self.coltocompare + "=" + "{}".format(
            self.colvalue) + ""
        print("update_query ==", update_query)
        res = noom.update_data(update_query)
        print(res)

    def test_getNoomObjectForColumn(self):
        log = self.getLogging()
        noom = NoomPy(excel_path=self.filepath)
        #noom = NoomPy(filepath)
        return noom

    def returnQueryData(self,noom, sheetname, coltocompare, colvalue, reqcolname):
        select_query = "SELECT * FROM " + sheetname + " WHERE " + coltocompare + "=" + "{}".format(colvalue) + ""
        print("query ===", select_query)
        res = noom.select_data(select_query)
        get_col_value = noom.get_data(data=res, key=reqcolname)
        print("Fetched Value from sheet is  ======", get_col_value)
        return get_col_value

    def readExcel(self,rowID, column):
        log = self.getLogging()
        filepath = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + self.readDataProperties().properties.get("LocaleFileCSV")
        data = pd.read_csv(filepath, low_memory=False)
        get_col_value = data._get_value(rowID, column)
        log.info("row == "+str(rowID)+" and header == "+str(column))
        return get_col_value

    def readExcelAuth0(self,rowID, column, file):
        log = self.getLogging()
        filepath = os.path.abspath(os.path.join(os.path.abspath(os.path.dirname(__file__)), "..")) + self.readAuth0DataProperties().properties.get(file)
        data = pd.read_csv(filepath, low_memory=False)
        get_col_value = data._get_value(rowID, column)
        # log.info("row == "+str(rowID)+" and header == "+str(column))
        return get_col_value
