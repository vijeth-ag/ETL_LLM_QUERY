import os
import streamlit as st
import pandas as pd

import json
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr
import requests
from functools import wraps
from pymilvus import connections, utility, db, MilvusClient, FieldSchema, CollectionSchema, Collection, DataType
from openai import OpenAI

# Set the folder where you want to save the uploaded files
save_folder = "/data/unprocessed"

# Create the folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder)

uploaded_file = st.file_uploader("", type=["csv"])

if uploaded_file is not None:
    # Get the file name and the file content
    file_name = uploaded_file.name
    file_path = os.path.join(save_folder, file_name)

    print("file_name",file_name)    
    print("file_path",file_path)
    
    # Save the file to the specified folder
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    
    st.success(f"File '{file_name}' has been saved to '{save_folder}'.")
