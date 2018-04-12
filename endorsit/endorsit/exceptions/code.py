class Code:
    # for service
    NO_ERR_CODE = 100000
    NO_PARAMS = 100001

    # for db
    TABLE_NOT_EXIST = 200001
    DUPLICATE_KEY = 200002

    msg = {
        NO_ERR_CODE: "Variable(s) in error_msg",
        NO_PARAMS: "No params here",
        TABLE_NOT_EXIST: "Table doesn't exist",
        DUPLICATE_KEY: "Table field value is duplicates"
    }
