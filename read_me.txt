Version details:
Python – 3.7.9
Brownie – 1.19.3
Ganache CLI - v6.12.2 (ganache-core: 2.13.2)
Brownie uses Ganache cli for command line interface and is heavily dependent on it.[7]
Development setup:
1) Clone the git repository into the local.[8]
2) Create a virtual environment within brownie local.
3) Installed wheel, ganache-cli and all required dependencies.
4) Follow requirements-dev.txt 

Project structure:
Root folder
-
Brownie
o Test folder
▪ __init__.py – The custom strategy created must be imported here to make it available in the test script.
▪ Strategies.py (Wrapper implementation for the strategies)
-
Test script (Where test functions are written to test the functionality)
