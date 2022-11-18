# Instructions for Running Census Housing Values Pipeline

The pipeline requires **three** raw census data files and outputs a single cleaned and merged csv data set of median housing values in the US

Here are the instructions to download the necessary files and edit pipeline script before running:

## 1. Median Housing Value Dataset

* Go to [Census Bureau Data](https://data.census.gov/) website and type “Housing Value and Purchase Price” in the search box.
* The search will return multiple results from the American Community Survey (ACS). Select *“B25077 | MEDIAN VALUE (DOLLARS)”* from the list.
* Making a selection will generate a table. Now select the year and ACS estimates based on the number of years. We used 2020: ACS 5-years estimates.
* Click “Transpose” to generate a long table instead of wide.
* Now filter using “Geo” tab. Click Geo > County > All counties in the US.
* After applying filters, it will show a message “Table is too large to display” with a download button. Click the “Download Table” button.
* Make sure the appropriate box is checked and click download .csv.
* It will download a compressed zip file containing raw data file and metadata file.
* Extract and rename the data file to **“median_housing_value_2020.csv”**

## 2. Detailed Property Value Dataset

* Go to [Census Bureau Data](https://data.census.gov/) website and type “Housing Value and Purchase Price” in the search box.
* The search will return multiple results from the American Community Survey (ACS). Select *“B25075 | VALUE”* from the list.
* Making a selection will generate a table. Now select the year and ACS estimates based on the number of years. We used 2020: ACS 5-years estimates.
* Click “Transpose” to generate a long table instead of wide.
* Now filter using “Geo” tab. Click Geo > County > All counties in the US.
* After applying filters, it will show a message “Table is too large to display” with a download button. Click the “Download Table” button.
* Make sure the appropriate box is checked and click download .csv.
* It will download a compressed zip file containing raw data file and metadata file.
* Extract and rename the data file to **“detailed_housing_value_2020.csv”**

## 3. Occupancy Status Dataset

* Go to [Census Bureau Data](https://data.census.gov/) website and type “Housing” in the search box and select housing.
* Select *Decennial Census H1 | OCCUPANCY STATUS* from the list.
* We used “2020: DEC Redistricting Data (PL 94-171)” data.
* Click “Transpose” to generate a long table instead of wide.
* Now filter using “Geo” tab. Click Geo > County > All counties in the US.
* After applying filters, it will show a message “Table is too large to display” with a download button. Click the “Download Table” button.
* Make sure the appropriate box is checked and click download .csv.
* It will download a compressed zip file containing raw data file and metadata file.
* Extract and rename the data file to **“occupancy_status_2020.csv”**

## 4. Instruction for the Pipeline:

Before running the airflow pipeline. Make these changes in the pipeline script **“housing_value_airflow_pipeline.py”** in the “dag” directory:

* Inside the function **“cleanCensusData”** edit the correct path of input census files at **lines 22 to 24** that we created above.
* Edit **line 61** and add correct path to your output directory.
* Edit **line 72** and add the correct path to your directory outside of the airflow directory where you want the output file to be copied.


