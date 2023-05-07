# IUBH Python Assignment

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

```bash
git clone https://github.com/sahilshetty10/IU-python-assignment.git
``` 

2.  Navigate to the cloned repository:

```bash
cd IU-python-assignment
```

3.  Create a conda environment with the required dependencies:

```bash
conda create --name <env> --file requirements.txt
```

4.  Activate the conda environment:

```bash
conda activate <env>
```

5.  Run the script:

```bash
python main.py
```

The results of the script will be stored in the `results.db` file.

## Running the Unit Test

To run the unittests, follow these steps:

1.  Navigate to the cloned repository:

```bash
cd IU-python-assignment
```
2.  Activate the conda environment:

```bash
conda activate <env>
```

3.  Run the test:

```bash
python -m unittest test.py
```
