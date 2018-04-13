var strTpl = function(str, fields) {
    for(index in fields) {
        str = str.replace('%s', fields[index])
    }
    return str
}
