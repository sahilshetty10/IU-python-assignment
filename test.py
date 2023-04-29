from utils import DataBase
import unittest
import pandas as pd

class DataBaseTestCase(unittest.TestCase):
    def setUp(self):
        self.db = DataBase("test.db")

    def tearDown(self):
        self.db.engine.dispose()
    
    def test_push_df_to_db(self):
        # Create a sample dataframe
        data = {'Name': ['John', 'Jane', 'Mike'], 'Age': [25, 30, 35]}
        df = pd.DataFrame(data)

        # Push the dataframe to the database
        self.db.push_df_to_db("users", df)

        # Retrieve the data from the database
        retrieved_df = pd.read_sql_table("users", self.db.engine, index_col='index')

        # Assert that the retrieved dataframe is equal to the original dataframe
        self.assertTrue(df.equals(retrieved_df))

if __name__ == '__main__':
    unittest.main()