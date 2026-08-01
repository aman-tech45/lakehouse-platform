                    +---------------------+
                    |   Raw CSV Dataset   |
                    +----------+----------+
                               |
                               v
                    +---------------------+
                    |   Bronze Layer      |
                    |---------------------|
                    | Read CSV            |
                    | Infer Schema        |
                    | Add Audit Columns   |
                    | Write Parquet       |
                    +----------+----------+
                               |
                               v
                    +---------------------+
                    |   Silver Layer      |
                    |---------------------|
                    | Remove Duplicates   |
                    | Remove Nulls        |
                    | Filter Bad Records  |
                    | Business Rules      |
                    +----------+----------+
                               |
                               v
                    +---------------------+
                    |    Gold Layer       |
                    |---------------------|
                    | Monthly KPIs        |
                    | Revenue             |
                    | Avg Fare            |
                    | Avg Distance        |
                    +----------+----------+
                               |
                               v
                    +---------------------+
                    | Business Analytics  |
                    +---------------------+