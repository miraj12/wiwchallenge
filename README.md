# wiwchallenge

When I Work code challenge:

How to run the program:

Python 3.9.2 is used when developing this program, Python >= 3.7.1 must be installed first to run this program.

First clone this repository to your local environment.

Install the dependencies using pip
pip install -r requirements.txt

Once the dependencies are installed successfully, you can run the code_challenge.py script

python code_challenge.py

You can also provide optional argument for the public root url.

python code_challenge.py https://public.wiwdata.com/engineering-challenge/data/

If the optional public root url is not provided the default url will be used which is set to
https://public.wiwdata.com/engineering-challenge/data/


Approach used:

The program expects a valid path which can be a http or a local file path, and valid csv files from a-z at the root path.
It is assumed that all the csv will have same columns.
To transform the data, I have utilized the pandas library. It will read files one by one from a-z and concat to the dataframe.
Once all the csv files are read, it will pivot the dataframe using user_id column as index, path as columns, and length as value.
It will also sum the length if a duplicated entry is encountered. For example, a same user_id and path.
Using pandas makes it easier to read csv file,pivot and aggregate data for each user_id.

The program will output the result to the user_visits.csv file. The result will have a row for each user_id in the data set, and column for each unique page path. 
The values will be the length of time spend by each user on that path.


Another approach:
If using external library such pandas is not possible, then the alternative approach is to read each file line by line and 
aggregate the data for each user in a python's built in data structure such as dictionary.
The program can read line by line and keep a nested dictionary where first level key is the user_id and the inner level key is the unique paths, and length is the value such as following.
{
'user_id1' : {'path1': 10, 'path2' : 11},
 ...
}

Also another data structure that will be needed is the set of unique paths, this will be used when writing the results to the csv file at end.
After reading all the files, we simply iterate over the dictionary writing each entry to the csv file.