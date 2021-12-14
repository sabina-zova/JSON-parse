# JSON-parse
The program, which extracts data from the json file and stores it into sqlite database.  
Tables are created in the beginning of the programm with colums named according to the data which need to be stored.  
`def find_item` method finds an item in a json dictionary.  
`json` library is used to open a json file as a nested list and `jsonpath_ng.ext` library is used to parse json path which leads to the searched value.  
To **run** the program you need a json file ([sample-data.json](https://github.com/sabina-zova/JSON-parse/blob/master/sample-data.json) in this case),
database connection and a program or extention allowing to display an sql table. The table will be created after you run the code.
## Git (Complete)
``` 
git clone https://github.com/sabina-zova/JSON-parse.git
```
