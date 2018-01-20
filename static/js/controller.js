function encender(id) {
	location.href = location.href.split("?")[0] + "?light=" + id + "&function=Turn-on"
};

function apagar(id) {
	location.href = location.href.split("?")[0] + "?light=" + id + "&function=Turn-off"
};

function brightness(value, id) {
	location.href = location.href.split("?")[0] + "?light=" + id + "&value=" + value + "&function=Brightness"
}
