'''The file contains all the data quality tests.
It provides a quick and easy way to author and run new data quality tests.
The testing framework provides the following tests:

check_for_nulls - this test will check for nulls in a column
check_for_min_max - this test will check if the values in a column are with a range of min and max values
check_for_valid_values - this test will check for any invalid values in a column
check_for_duplicates - this test will check for duplicates in a column
Each test can be authored by mentioning a minimum of 4 parameters.

testname - The human readable name of the test for reporting purposes
test - The actual test name that the testing micro framework provides
table - The table name on which the test is to be performed
column - The table name on which the test is to be performed
'''
from dataqualitychecks import check_for_nulls
from dataqualitychecks import check_for_min_max
from dataqualitychecks import check_for_valid_values
from dataqualitychecks import check_for_duplicates


test1={
	"testname":"Check for nulls",
	"test":check_for_nulls,
	"column": "monthid",
	"table": "DimMonth"
}


test2={
	"testname":"Check for min and max",
	"test":check_for_min_max,
	"column": "month",
	"table": "DimMonth",
	"minimum":1,
	"maximum":12
}


test3={
	"testname":"Check for valid values",
	"test":check_for_valid_values,
	"column": "category",
	"table": "DimCustomer",
	"valid_values":{'Individual','Company'}
}


test4={
	"testname":"Check for duplicates",
	"test":check_for_duplicates,
	"column": "monthid",
	"table": "DimMonth"
}
