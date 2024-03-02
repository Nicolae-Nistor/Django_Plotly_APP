# **Data Visualization of GDP Growth in Europe, using EUROSTAT API, Django, and Plotly**

# Overview
This is a web application built with Django and Plotly for visualizing GDP growth data from the EUROSTAT API. The application allows users to select a range of years and countries, and it displays a line graph of the GDP growth percentage over time.

# Features

User authentication system
CRUD operations for GDP data
Data visualization using Plotly
Integration with the EUROSTAT API

# Setup

To run this project, you'll need Python installed on your machine.

#Clone the repository:

git clone `https://github.com/Nicolae-Nistor/Django_Plotly_APP.git`

#Windows commands:
1. Open the project folder in File Explorer, then right-click and select "Open in Terminal" or "Open PowerShell Window Here" depending on the version of Windows you are using.

2. Create a Virtual Environment
`py -m venv myenv`

3. Activate the Virtual Environment
`myenv\Scripts\activate.bat`

4. Install the required libraries
`pip install -r requirements.txt`

5. Migrate the database
`py manage.py migrate`

6. Load data into database
`py manage.py load_indicator`

7. Run the server
`py manage.py runserver`

8. Open the project in your web browser by navigating to the following URL: 
`http://127.0.0.1:8000/`


# How to interact with the chart:
1. Double-click on any country name to isolate the data for that country
2. Then single-click on other country names to add them to the chart
3. Once added to the chart, single-click on that country name to remove it from the chart
4. Double-click again on any country name to reset the charts to include all the countries
5. Click and drag the chart area to focus on a particular period
6. Double-click on the chart area to reset the time periods


# Technologies Used
Python
Django
Plotly
EUROSTAT API

# Contributing

Contributions are welcome! To contribute to this project, follow these steps:

1. Fork the repository: `https://github.com/Nicolae-01001110/Django_Plotly_APP.git`
2. Create a new branch: `git checkout -b my-feature-branch`
3. Make your changes and commit them: `git commit -am "Add new feature"`
4. Push your changes to your fork: `git push origin my-feature-branch`
5. Create a new pull request on GitHub.

 
