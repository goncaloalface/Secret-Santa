# Secret-Santa
Python script to run a secret santa for you, your family and friends.

The email address used to send the emails must be a gmail address and the user will need to provide access to least secure apps (https://myaccount.google.com/lesssecureapps).

To run this script, the user needs to change some variables inside the script, namely:

- email_address: the email adress where the emails will be sent from (in this case, it must be a gmail);
- email_pw: the password from the email address;
- value: maximum value of the present;
- data_limit: the date limit to trade the presents;
- subject: subject of the emails to be sent (default value 'Secret Santa ${current_year}!');
- file: file path with the following format and where each row represents a new person:\
  <<email_address>>;<<name_of_the_person>>\
  <<email_address>>;<<name_of_the_person>>
  
After having the changes performed, the user just needs to run the following command in the same directory where the script is:\
`python secret_santa.py`

In case you used the script or have any suggestions, just contact me and thank you very much. 
Any feedback will be welcomed to improve the current script.
