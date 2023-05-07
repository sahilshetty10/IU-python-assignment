Welcome file
Welcome file

This repository contains a Python assignment for IUBH. The assignment is a Python script that uses a conda environment, and it performs data analysis on CSV files provided in the `/data` folder.

## File Structure

The file structure of this repository is as follows:


```bash
├── /data
│   ├── ideal.csv
│   ├── train.csv
│   └── test.csv
├── /test.py
├── /utils.py
├── /main.py
├── /results.db
└── /requirements.txt
```

-   The `/data` directory contains the CSV files that the script uses for data analysis.
-   `test.py` contains a unittest for the script.
-   `utils.py` contains utility functions used in the main script.
-   `main.py` is the main Python script that performs the data analysis.
-   `results.db` is a SQLite database file that stores the results of the script.
-   `requirements.txt` contains the dependencies required for the script to run.

## Running the Script

To run the script, follow these steps:

1.  Clone the repository:

`git clone https://github.com/sahilshetty10/IU-python-assignment.git` 

2.  Navigate to the cloned repository:

`cd IU-python-assignment` 

3.  Create a conda environment with the required dependencies:

`conda create --name <env> --file requirements.txt` 

4.  Activate the conda environment:

`conda activate <env>` 

5.  Run the script:

`python main.py` 

The results of the script will be stored in the `results.db` file.

## Running the Unit Test

To run the unittests, follow these steps:

1.  Navigate to the cloned repository:

`cd IU-python-assignment` 

2.  Activate the conda environment:

`conda activate <env>` 

3.  Run the test:

`python -m unittest test.py` 

This repository contains a Python assignment for IUBH. The assignment is a Python script that uses a conda environment, and it performs data analysis on CSV files provided in the /data folder.

File Structure
The file structure of this repository is as follows:

├── /data
│   ├── ideal.csv
│   ├── train.csv
│   └── test.csv
├── /test.py
├── /utils.py
├── /main.py
├── /results.db
└── /requirements.txt
The /data directory contains the CSV files that the script uses for data analysis.
test.py contains a unittest for the script.
utils.py contains utility functions used in the main script.
main.py is the main Python script that performs the data analysis.
results.db is a SQLite database file that stores the results of the script.
requirements.txt contains the dependencies required for the script to run.
Running the Script
To run the script, follow these steps:

Clone the repository:
git clone https://github.com/sahilshetty10/IU-python-assignment.git

Navigate to the cloned repository:
cd IU-python-assignment

Create a conda environment with the required dependencies:
conda create --name <env> --file requirements.txt

Activate the conda environment:
conda activate <env>

Run the script:
python main.py

The results of the script will be stored in the results.db file.

Running the Unit Test
To run the unittests, follow these steps:

Navigate to the cloned repository:
cd IU-python-assignment

Activate the conda environment:
conda activate <env>

Run the test:
python -m unittest test.py

Markdown selection 7 bytes 1 words 0 lines Ln 9, Col 0HTML 1263 characters 221 words 39 paragraphs
