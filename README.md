# cz4032-bean-mining

Create a local folder with :
------------

  source: Github Repository

    1. setup.py
    2. json_to_csv_converter.py
    3. tox.ini
  
  source: yelp.com/dataset
  
    1. yelp_academic_dataset_business.json
    2. yelp_academic_dataset_user.json
    3. yelp_academic_dataset_review.json

Next, In the directory:
------------

Step 1: Install the dependencies: `$ pip install -e .`
Step 2: Create the csv file for each json: `python json_to_csv_converter.py [abc].json`  #[abc] -> json file name

Your csv file is then ready!
