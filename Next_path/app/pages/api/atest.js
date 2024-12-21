

function str_sanitizer(){
    if (!ID_REGEX.test(query.id)){
        return "not pass"
    }
}

console.log()