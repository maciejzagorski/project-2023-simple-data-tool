# Simple data tool

### Overview:

A simple CLI application that performs specific operations on the provided datasets. The datasets contain information
about individuals, including their first name, telephone number, email, password, role, date of account creation and
a list of children with their names and ages. The application uses data stored as a _pandas_ dataframe (see below) as
well as using an SQL database (_SQLite_).

### Installation (external libraries):

The application uses the following external (not built-in) libraries: _pandas_ and _lmxl_. In order to install them
(assuming that you have pip installed) type this in a terminal: ```pip install pandas``` and ```pip install lxml```.

### Data Specification:

#### General:

The datasets used in the project are provided in different file formats (JSON, XML and CSV), located across different
directories. Each of the datasets contains the following information about the users:

* firstname,
* telephone number,
* e-mail address,
* password (in plain text),
* role (admin / user),
* date of account creation,
* list of user's children, including their names and age.

In the CSV files columns including the above information are delimited by a semicolon, while the information about
individual children are separated by a comma.

#### Validation

The provided datatsets are validated by the application according to the following rules:

* records without provided telephone numer are rejected,
* duplicates (based on telephone number and e-mail address) are removed from the merged dataset (the newer account,
based on its creation date, was preserved),
* e-mail addresses are validated according to the following rules (non-valid e-mails are removed):
    * must contain only one “@” symbol,
    * its part before “@” must be at least 1 character long,
    * its part between “@” and the following “.” must be at least 1 character long,
    * its part after the last “.” must be between 1 and 4 characters long, containing only letters and / or digits,
* telephone numbers are stored as 9 digits number, without any special characters (e.g. spaces) and leading zeros; e.g.
  numbers like +48123456789, 00123456789, (48) 123456789, or 123 456 789, are stored as 123456789.

### Usage:

#### General:

In order to run the application it is necessary to execute ```script.py``` by passing ```--login <login> --password
<password>``` parameters, i.e. ```python script.py <command> --login <login> --password <password>```, followed by a
selected action, e.g. ```print-oldest-account```:

> &gt;python script.py --login ella.b74@example.org --password +vJCXfFLe0 print-oldest-account  
> name: Donna
> email_address: donna.jones@example.org  
> created_at: 2013-03-06 15:46:08

The user's e-mail or 9-digit telephone number may be used as the login. Running the application with the missing login
(```--login```) or password (```--password```) argument or with the incorrect credentials will result in the
```Invalid Login``` output:

> &gt;python script.py --login ella.b74@example.org --password +vJCXfFLe0_ print-oldest-account  
> Invalid Login

Please find below the pair of example logins and passwords (one user with the admin role and one with the user role,
respectively) to test the application (telephone number | e-mail | password):  
361568741 | ella.b74@example.org | +vJCXfFLe0  
876543216 | ronald99@example.com | Q3XWW+Uc*Z

#### Actions:

The application may be executed with the following actions, divided into _Admin Actions_ and _User Actions_. It is
possible to run the application with one action at once, together with the ```create database``` option (see below).
Running one of the admin actions with the user credentials (the user with the user, not the admin, role) will result
in the ```Unauthorized User``` output:

> &gt;python script.py --login 876543216 --password Q3XWW+Uc*Z print-oldest-account  
> Unauthorized User

**Admin Actions:**

- ```print-all-accounts``` – printing the total number of all the valid accounts (total number of the valid users in the
  datasets):

> &gt;python script.py --login ella.b74@example.org --password +vJCXfFLe0 print-all-accounts  
> 81

- ```print-oldest-account``` – printing the selected information about the account with the longest existence (with the
  oldest creation date):

> &gt;python script.py --login ella.b74@example.org --password +vJCXfFLe0 print-oldest-account  
> name: Donna
> email_address: donna.jones@example.org  
> created_at: 2013-03-06 15:46:08

- ```group-by-age``` – printing the information about children grouped by age, with information on the number of
  children of each age; the information is sorted by the number of the children in the specific age group (ascending):

> &gt;python script.py --login ella.b74@example.org --password +vJCXfFLe0 group-by-age
> age: 22, count: 1.0  
> age: 20, count: 1.0  
> age: 16, count: 1.0  
> age: 18, count: 2.0  
> age: 19, count: 4.0  
> age: 4, count: 4.0  
> age: 1, count: 4.0  
> age: 12, count: 5.0  
> age: 6, count: 5.0  
> age: 5, count: 5.0  
> age: 15, count: 6.0  
> age: 11, count: 6.0  
> age: 10, count: 6.0  
> age: 7, count: 6.0  
> age: 13, count: 7.0  
> age: 9, count: 7.0  
> age: 8, count: 7.0  
> age: 14, count: 10.0  
> age: 2, count: 10.0  
> age: 3, count: 12.0

**User Actions:**

- ```print-children``` – printing the information about the logged user children (their names and age); the children
  list is sorted alphabetically, by the children's name:

> &gt;python script.py --login 876543216 --password Q3XWW+Uc*Z print-children  
> Lily, 19  
> Logan, 19  
> Maya, 10

- ```find-similar-children-by-age``` – finding the users with children of the same age as at least one child of the
  logged user; in result, the application prints information about the found user (his/her name and telephone number)
  and
  his/her children (their names and age); the children list is sorted alphabetically, by the children's name:

> &gt;python script.py --login 876543216 --password Q3XWW+Uc*Z find-similar-children-by-age  
> Laura, 504140673: Charlie, 7; Sophie, 10  
> Emma, 401629185: Christopher, 9; Sophia, 10  
> Amanda, 501234567: Courtney, 19; Emma, 3; Ethan, 14  
> Ava, 876543218: Brandon, 19; Carter, 7  
> Leo, 876543220: Oliver, 10  
> Felicia, 551239876: Jennifer, 2; Omar, 10  
> Julia, 441935720: Ethan, 3; Isabel, 10

**Create Database:**

- ```create-database``` – the application may be executed (both by the user with the admin role and the user role) with
  the additional option ```create-database``` which will result in loading the provided data to the SQL database
  (_SQLite_, in-memory database) and, further, executing each of the above-mentioned action using said database and
  corresponding SQL queries (nevertheless, the results of each of the actions will be the same, as the same datasets are
  used):

> python script.py --login 876543216 --password Q3XWW+Uc*Z print-children create-database
> Lily, 19  
> Logan, 19  
> Maya, 10

### Sources:

https://pandas.pydata.org/ (_pandas_ documentation)
