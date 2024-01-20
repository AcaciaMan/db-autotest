function displayJSON() {
    var jsonObject = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    };

    // Convert JSON object to string
    var jsonString = JSON.stringify(jsonObject, null, 2); // 2 spaces of indentation

    // Insert JSON string into HTML element with id 'jsonDisplay'
    document.getElementById('jsonDisplay').textContent = jsonString;
}


function getJSON() {
    var jsonObject = {
        "key1": "value1",
        "key2": "value2",
        "key3": "value3"
    };

    // Convert JSON object to string
    var jsonString = JSON.stringify(jsonObject, null, 2); // 2 spaces of indentation

    console.log('something');
}

// Call the function when the page loads
window.onload = displayJSON;
