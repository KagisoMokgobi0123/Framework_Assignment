# To RUN The Code

1. Clone the repo to your local machine

   - git clone code_url

2. Install all required packages and required dataset
   - pip install pandas streamlit matplotlit
   - You can download the dataset from Kaggle:
     https://www.kaggle.com/allen-institute-for-ai/CORD-19-research-challenge
   - Includes:
   - Paper titles and abstracts - Publication dates
   - Authors and journals
   - Source information
3. Use Visual Studion Code as your code runner.

4. Select the most recent python environment for running covid_2019.ipynb

5. Make sure to run the covid_2019 file first.

   - To run it:
   - Hover the cell,on your left you'll see an execution button. Click it.
   - Run import pandas cell first. Otherwise the other cells will give an error
   - both import pandas and dataframe cells might take longer to run at first. Be patient.

6. Run the App file
   - Metadata is too large, so for the purpose of avoiding a runtime error. use filtered_df file.
   - open gitbash a run this command
   * streamlit run app.py
