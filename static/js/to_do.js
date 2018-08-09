function checked(obj) {
    if (obj.checked) {
    	location.href = location.href.split("?")[0] + "?checked=" + obj.id
    }
}
