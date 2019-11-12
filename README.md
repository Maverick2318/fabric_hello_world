An example of "Hello world" using Python Fabric. I am using Fabric version 2.

C02VQ1S6HTDD:fabric_hello_world nsiddiq$ fab -V

Fabric 2.5.0

Paramiko 2.6.0

Invoke 1.3.0

An example of printing hello world only:

C02VQ1S6HTDD:fabric_hello_world nsiddiq$ fab hello

hello world


An example of reading in the user's name as an argument and greeting him:

C02VQ1S6HTDD:fabric_hello_world nsiddiq$ fab helloname --name=Nasr

hello Nasr!
