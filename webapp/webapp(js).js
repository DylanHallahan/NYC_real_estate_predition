function getBathValue() {
    var uiBathrooms = document.getElementsByName("uiBathrooms"); //get ba value from html
    for (var i in uiBathrooms) {
        if (uiBathrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1;
}

function getBedroomsValue() {
    var uiBedrooms = document.getElementsByName("uiBedrooms"); //get bds value from html
    for (var i in uiBedrooms) {
        if (uiBedrooms[i].checked) {
            return parseInt(i) + 1;
        }
    }
    return -1;
}

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked"); //get mod var
    var sqft = document.getElementById("uiSqft");
    var bds = getBedroomsValue();
    var ba = getBathValue();
    var area = document.getElementById("uiarea");
    var estPrice = document.getElementById("uiEstimatedPrice");

    var url = "http://127.0.0.1:5000/predict_home_price"; //server must be running

    $.post(url, {
        sqft: parseFloat(sqft.value),
        bds: bds,
        ba: ba,
        area: area.value
    }, function (data, status) {
        console.log(data.estimated_price);
        estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + "$ </h2>";
        console.log(status);
    });
}

function onPageLoad() {
    console.log("document loaded"); //get val for drop down
    var url = "http://127.0.0.1:5000/get_area"; 
    $.get(url, function (data, status) {
        console.log("got response for get_area_names request");
        if (data) {
            var area = data.area;
            var uiarea = document.getElementById("uiarea");
            $('#uiarea').empty();
            for (var i in area) {
                var opt = new Option(area[i]);
                $('#uiarea').append(opt);
            }
        }
    });
}

window.onload = onPageLoad;