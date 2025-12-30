# ETLA Financial Statements
An ETL pipline and data analysis project for bank and billing statements. Facilitates bank and billing statement transaction queries, and generates reports and visualizations for historical financial transactions.

## Purpose
The intended purpose of this project is to assist in gathering, reporting, and visualizing historical financial transaction data.

## Dependencies
This project relies on the following packages:
* pandas (version 2.3.3)
* matplotlib (version 3.10.7)
* seaborn (version 0.13.2)

This project relies on the [Tabula](https://tabula.technology/) application for custom data extraction of bank and billing statements.

## Version History
* 0.3
    * Introduce environment variables to safeguard PII (personal Identifying Information)
    * Generate CSV payment history report for Toyota vehicle
    * Generate CSV payment history reports for two Tesla vehicles
* 0.2
    * ETL pipeline established for Toyota bank statements
    * ETL pipeline established for Wells Fargo Auto
* 0.1 (Initial Release)
    * ETL pipline established for Chime bank statements
    * ETL pipline established for NFCU bank statements
    * Analysis of transactions
    * Generate CSV totals report
    * Visualization of transfers between accounts

## License
[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)