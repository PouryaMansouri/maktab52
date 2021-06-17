function addData() {
    let table = document.getElementById("table");
    table.innerHTML = "";
    var number = Number(document.getElementById("number").value)


    for (let i = 1; i <= number; i++) {
        var newRow = document.createElement("tr");
        for (let j = 1; j <= number; j++) {
            var newCell = document.createElement("td");
            newCell.innerText = (i * j);
            newRow.append(newCell);
        }

        document.getElementById("table").append(newRow);
    }


    document.getElementById("number").value = '';
}
