""" DataCamp - Importing  Data in Python Part 1 (up to sql) and Part 2 (from web files) """

import json
import pickle
import sys
from urllib.request import Request, urlopen, urlretrieve

import h5py
import numpy as np
import pandas as pd
import requests
import scipy.io
from bs4 import BeautifulSoup
from sas7bdat import SAS7BDAT
from sqlalchemy import create_engine

# --------------------------------------------------------
# Flat Files - Python I/O
# --------------------------------------------------------


def import_text(file_path):
    """ read entire text file into an object """
    with open(file_path) as file:
        data = file.readlines()
    return data


def import_text_chunk(file_object, chunk_size=1000):
    """ lazy load file piece by piece using generator function 
        usage: as a reader function with open() file """
    while True:
        data = file_object.read(chunk_size)
        if not data:
            break
        yield data

# --------------------------------------------------------
# Flat Files - NumPy
# --------------------------------------------------------


def import_numeric_text(file_path, delimiter, skiprows=0):
    """ load numeric data into numpy series """
    return np.loadtxt(file_path, delimiter, skiprows)


def import_mixed_type_text(file_path, delimiter, has_header=True, dtype=None):
    """ load mix data type file into numpy structured array """
    return np.genfromtxt(file_path, delimiter=',', names=has_header, dtype=dtype)


def import_mixed_type_text_csv(file_path):
    """ load mixed data type csv file into numpy structured array """
    return np.recfromcsv(file_path)

# --------------------------------------------------------
# Flat Files - Pandas
# --------------------------------------------------------


def import_cvs_df(file_path, delimiter=','):
    """ import a csv file into pandas DataFrame """
    return pd.read_csv(file_path, sep=delimiter)


def import_corrupted_csv_df(file_path, delimiter=',', comment="#", na_values='Nothing'):
    """ import corruptred data file with a delimeter, comment = characters that comments occur after, 
        na_values is a list of strings to recognize as NA/ NaN """
    return pd.read_csv(file_path, sep=delimiter, comment=comment, na_values=na_values)

# --------------------------------------------------------
# Binary Files - Pickle
# --------------------------------------------------------


def import_bin_file(file_path):
    """ import content of a pickled file """
    with open(file_path, 'rb') as file:
        data = pickle.load(file)
    return data

# --------------------------------------------------------
# Excel Files - Pandas
# --------------------------------------------------------


def import_excel_file_df(file_path):
    """ import content of an excel file as a pandas DataFrame """
    return pd.ExcelFile(file_path)


def import_excel_worksheet_df(file_path, worksheet, skiprows=None):
    """ import content of an excel worksheet as a pandas DataFrame
        worksheet can be an index or a name """
    return pd.ExcelFile(file_path).parse(worksheet, skiprows=skiprows)

# --------------------------------------------------------
# SAS/ Stata Files (sas7bdat, dta)
# --------------------------------------------------------


def import_sas_file(file_path):
    """ import content of a sas file as a pandas DataFrame """
    with SAS7BDAT(file_path) as file:
        df = file.to_data_frame()
    return df


def import_dta_file(file_path):
    """ import content of a stata file as a pandas DataFrame """
    return pd.read_stata(file_path)

# --------------------------------------------------------
# HDF5 Files - [meta, quality, strain]
# --------------------------------------------------------


def import_hdf5_file(file_path):
    """ import content of a HDF5 file """
    return h5py.File(file_path, 'r')

# --------------------------------------------------------
# MATLAB Files - [matrix laboratory; .mat]
# --------------------------------------------------------


def import_matlab_file(file_path):
    """ import content of a MATLAB file """
    # return scipy.io.loadmat(file_path) - LINT ISSUE?
    pass 

# --------------------------------------------------------
# Relational Databases - SQLite
# --------------------------------------------------------


def query_sqlite(con_str, sql_query):
    """ import result of a sql query as a pandas DataFrame, long """
    engine = create_engine('sqlite:///'+con_str)
    con = engine.connectr()
    rs = con.execute(sql_query)
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()
    con.close()
    return df


def query_sqlite_df(con_str, sql_query):
    """ import result of a sql query as a pandas DataFrame, short """
    engine = create_engine('sqlite:///'+con_str)
    return pd.read_sql_query(sql_query, engine)

# --------------------------------------------------------
# Web files, html, parsed html text - urlretrieve
# --------------------------------------------------------


def import_and_save_web_df(url, local_file_path):
    """ import web (csv) file locally and as a pandas DataFrame """
    return pd.DataFrame(urlretrieve(url, local_file_path))


def import_web_df(url, delimiter):
    """ import web (delimited) file as a pandas DataFrame """
    return pd.DataFrame(pd.read_csv(url, sep=delimiter))


def import_web_excel_df(url):
    """ import web excel file as a pandas DataFrame """
    return pd.DataFrame(pd.read_excel(url, sheetname=None))


def import_web_excel_worksheet_df(url, sheetname):
    """ import web excel file (a single worksheet) as a pandas DataFrame """
    return pd.DataFrame(pd.read_excel(url, sheetname=None)[sheetname])


def import_request_txt(url):
    """ import html from a web  request """
    return requests.get(url)


def import_request_html(url):
    """ import html from a web request """
    return BeautifulSoup(requests.get(url).text).prettify()


def import_request_text(url):
    """ import clean text from a web request """
    return BeautifulSoup(requests.get(url).text).get_text()


def import_request_text_urls(url):
    """ import links (as a text) from a web request """
    return BeautifulSoup(requests.get(url).text).find_all('a').get('href')

# --------------------------------------------------------
# WebAPI (json)
# --------------------------------------------------------


