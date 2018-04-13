class Code:
    # for service
    NO_ERR_CODE = 100000
    NO_PARAMS = 100001

    # for db
    NO_DATA = 200000
    TABLE_NOT_EXIST = 200001
    DUPLICATE_KEY = 200002
    VALIDATOR_NOT_FOUND = 200003

    msg = {
        NO_DATA: "NO data found",
        NO_ERR_CODE: "Variable(s) in error_msg",
        NO_PARAMS: "No params",
        TABLE_NOT_EXIST: "Table doesn't exist",
        DUPLICATE_KEY: "Table field value is duplicates",
        VALIDATOR_NOT_FOUND: "Validator not found"
    }
