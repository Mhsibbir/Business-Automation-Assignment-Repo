function validateForm() {
    var name = document.getElementById("name").value;
    var model = document.getElementById("model").value;
    var year = document.getElementById("year").value;
    var carType = document.getElementById("carType").value;

    var isValid = true;

    if (name.trim() === "") {
        document.getElementById("nameError").innerText = "Name is required";
        isValid = false;
    } else {
        document.getElementById("nameError").innerText = "";
    }

    if (model.trim() === "") {
        document.getElementById("modelError").innerText = "Model is required";
        isValid = false;
    } else {
        document.getElementById("modelError").innerText = "";
    }

    if (year.trim() === "") {
        document.getElementById("yearError").innerText = "Year is required";
        isValid = false;
    } else if (!/^\d{4}$/.test(year)) {
        document.getElementById("yearError").innerText = "Invalid year format";
        isValid = false;
    } else {
        document.getElementById("yearError").innerText = "";
    }

    if (carType === "") {
        document.getElementById("carTypeError").innerText = "Fuel Type is required";
        isValid = false;
    } else {
        document.getElementById("carTypeError").innerText = "";
    }

    if (carType === "") {
        document.getElementById("carTypeError").innerText = "Fuel Type is required";
        isValid = false;
    } else {
        document.getElementById("carTypeError").innerText = "";
    }

    if (!isValid) {
        event.preventDefault(); // Prevent form submission if validation fails
    }
};
function defaultCartype(){
    var carType = document.getElementById("carType").value;
    var batteryCapacityDiv = document.getElementById("batteryCapacity");
    var fuelEfficiencyDiv = document.getElementById("fuelEfficiency");
    
    
        fuelEfficiencyDiv.style.display = "none";
        batteryCapacityDiv.style.display = "none";
        }



function showHideBatteryCapacity() {
var carType = document.getElementById("carType").value;
var batteryCapacityDiv = document.getElementById("batteryCapacity");
var fuelEfficiencyDiv = document.getElementById("fuelEfficiency");

if(carType === ""){
    fuelEfficiencyDiv.style.display = "none";
    batteryCapacityDiv.style.display = "none";
    }

if (carType === "electric") {
    batteryCapacityDiv.style.display = "block";
    fuelEfficiencyDiv.style.display = "none";
} 
if(carType === "gas")
 {
    fuelEfficiencyDiv.style.display = "block";
    batteryCapacityDiv.style.display = "none";
}


}
