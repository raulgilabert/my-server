function next(month, year) {
	location.href = location.href.split("?")[0] + "?control=next&month=" + month + "&year=" + year
}

function back(month, year) {
	location.href = location.href.split("?")[0] + "?control=back&month=" + month + "&year=" + year
}
