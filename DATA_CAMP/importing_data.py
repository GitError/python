""" DataCamp - Importing  Data in Python Part 1 """

import os
import pickle
import sys

import h5py
import numpy as np
import pandas as pd
import scipy.io
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
    """ import corruptred data file with a delimeter, comment = characters that comments occur after in the file, 
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


def import_exel_worksheet_df(file_path, worksheet, skiprows=None):
    """ import content of an excel worksheet as a pandas DataFrame
        worksheet can be an index or a name """
    return pd.ExcelFile(file_path).parse(worksheet, skiprows=skiprows)

# --------------------------------------------------------
# SAS/ Stata Files (sas7bdat, dta)
# --------------------------------------------------------


def import_sas_file(file_path):
    """ import content of a sas file using sas7bdat library """
    with SAS7BDAT(file_path) as file:
        df = file.to_data_frame()
    return df


def import_dta_file(file_path):
    """ import content of a stata file """
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
    # return scipy.io.loadmat(file_path)
    pass


# --------------------------------------------------------
# Relational Databases - SQLite
# --------------------------------------------------------


def query_sqlite(con_str, sql):
    engine = create_engine('sqlite:///'+con_str)
    con = engine.connectr()
    rs = con.execute(sql)
    data = pd.DataFrame(rs.fetchall())
    con.close()
    return data


# --------------------------------------------------------
# Other Helpers
# --------------------------------------------------------


def list_files():
    """ list all files in the working directory """
    wd = os.getcwd()
    print(os.listdir(wd))
