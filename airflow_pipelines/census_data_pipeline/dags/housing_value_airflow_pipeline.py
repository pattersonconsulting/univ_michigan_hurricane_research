
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
import pandas as pd


default_args = {
    'owner': 'm_ghous',
    'start_date': dt.datetime(2022, 9, 27),
    'retries': 1,
    'retry_delay': dt.timedelta(minutes=5),
}

def cleanCensusData():
    '''Reads the raw census housing values data files, cleans, merge, and export
    a clean csv file
    '''
    #enter correct file path
    df1 = pd.read_csv("/c/Users/Ghous/airflow_linux/input/detailed_housing_value_2020.csv", header=1)
    df2 = pd.read_csv("/c/Users/Ghous/airflow_linux/input/occupancy_status_2020.csv", header=1)
    df3 = pd.read_csv("/c/Users/Ghous/airflow_linux/input/median_housing_value_2020.csv", header=1)

    df1 = df1.drop(df1.filter(regex='Margin').columns, axis=1)
    df1.drop('Geographic Area Name', axis=1, inplace=True)
    df1.columns=df1.columns.str.replace('[#,@,&,$,!,:]','')
    df1.columns=df1.columns.str.replace('EstimateTotal','usd_')
    df1.columns=df1.columns.str.replace(' ','_')
    dict1 = {'id': 'fips_code'}
    df1.rename(columns=dict1,
          inplace=True)
    df1.rename(columns={'usd_':'total_owner_occupied_houses', 'usd_Less_than_10000':'usd_less_than_10000'},
          inplace=True)
    df1['fips_code'] = df1['fips_code'].str[-5:]


    df2.drop('Geographic Area Name', axis=1, inplace=True)
    df2.columns = df2.columns.str.strip()
    dict2 = {'id': 'fips_code',
            '!!Total:': 'total_houses',
            '!!Total:!!Occupied': 'total_occupied',
            '!!Total:!!Vacant': 'total_vacant'}
    df2.rename(columns=dict2, inplace=True)
    df2['fips_code'] = df2['fips_code'].str[-5:]


    df3.drop('Margin of Error!!Median value (dollars)', axis=1, inplace=True)
    df3.rename(columns={'Estimate!!Median value (dollars)':'median_2020_housing_value_usd',
                        'Geographic Area Name':'geo',
                        'id':'fips_code'}, inplace=True)
    df3[['county','state']] = df3.geo.str.split(", ",expand=True)
    df3.drop('geo', axis=1, inplace=True)
    df3['fips_code'] = df3['fips_code'].str[-5:]

    #Joining
    joined_df = df3.merge(df1, how='left').merge(df2, how='left')

    #enter correct absolute/relavive path before running
    joined_df.to_csv('/c/Users/Ghous/airflow_linux/output/us_housing_values_cleaned.csv', encoding='utf-8', index=False)


with DAG('Clean_housing_Census_Data',
         default_args=default_args,
         schedule_interval=timedelta(days=1),
         ) as dag:
    cleanData = PythonOperator(task_id='clean',
                                 python_callable=cleanCensusData)
    #enter correct absolute/relavive path before running
    copyFile = BashOperator(task_id='copy',
                                 bash_command='cp /c/Users/Ghous/airflow_linux/output/us_housing_values_cleaned.csv /c/Users/Ghous/Desktop/cleaned_data/')

cleanData >> copyFile


