# file_tools

Module to make it easier to handle files and data

## data_converter:

* converts to pandas.DataFrame from csv, xlsx, json, and html

  -df(path) -> pandas.DataFrame

- converts from pandas.DataFrame to csv, xlsx, json, and html

-df(path, df) -> destination file path  
  
- converts to str from txt, sql, py, and html

-string(path) -> str

- converts from str to txt, sql, py, and html

-string(path, string) -> destination file path

-converts from one file type to another
  
  -supported file extensions(csv, xlsx, json)

  -file(src, dest) -> destination file path
