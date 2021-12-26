i94_table_query =(
'''
create table if not exists fact_i94_records 
(
    cicid int PRIMARY KEY,
    i94yr int,
    i94mon int,
    i94cit int,
    i94res int,
    i94port varchar,
    i94_port_city varchar,
    i94_port_state varchar,
    arrdate date,
    i94mode varchar,
    i94addr varchar,
    depdate date,
    i94bir int,
    i94visa varchar,
    biryear int,
    gender varchar,
    insnum varchar,
    airline varchar,
    visatype varchar
)
diststyle AUTO
;
''')


demographics_table_query=(
'''
create table if not exists dim_us_city_demographics 
(
    City VARCHAR,
    State VARCHAR,
    Median_Age int,
    Male_Population int,
    Female_Population int,
    Total_Population int,
    Number_of_Veterans int,
    Foreign_born int,
    Average_Household_Size int,
    State_Code varchar,
    American_Indian_and_Alaska_Native int,
    Hispanic_or_Latino int,
    White int,
    Asian int,
    Black_or_African_American int,
    primary key(City, State)
)
diststyle ALL
;
''')


time_table_query=('''
create table if not exists dim_time 
(
    date date primary key SORTKEY,
    year int,
    month int,
    day int,
    week int,
    weekday int
)
diststyle ALL
;
''')

temperature_table_query=('''
create table if not exists dim_temperature 
(
    Average_Temperature decimal(10,2),
    Average_Temperature_Uncertainty decimal(10,2),         
    state varchar primary key SORTKEY,     
    Country varchar

)
diststyle ALL
;
''')