// empty list for the products
let products = [];
let tableElement;
let inputElement; 
let selectElement;


document.addEventListener("DOMContentLoaded", () => {
    // fetch the inputElement
    inputElement = document.getElementById("search");
    // add event listener to inputElement
    inputElement.addEventListener("input", () => {
        filterProducts();
    });
    // fetch the selectElement
     selectElement = document.getElementById("sort");
     // create options for selectElement
     // first option
     const nameAsc  = document.createElement("option");
     // set the value
     nameAsc.value = "asc";
     // set the text content
     nameAsc.textContent = "Name (A-Z)"
     // add option to selectElement
     selectElement.appendChild(nameAsc);

     // second option
     const nameDesc = document.createElement("option");
     // set the value
     nameDesc.value = "desc";
     // set the textcontent
     nameDesc.textContent = "Name (Z-A)"
     // add option to selectElement
     selectElement.appendChild(nameDesc);

     //addEventListener to selectElement
     selectElement.addEventListener("change", () => {
        sortProducts();
     })


    // fetch the tableElement
     tableElement = document.getElementById("products");
});


// fetch the products from warehouse.json.
fetch("warehouse.json")
  .then(res => res.json())
  .then(data => {
    products = data.products;
    console.log(products);
    createTable(products);
});


// function that creates table
function createTable(data) {
    // empty the table
    tableElement.innerHTML = "";
    // create row 
    const headerRow = document.createElement("tr");
    // Loop the keys in data [0] to get the keys in headlines
    for (let key in data[0]) {
        // Create <th>
        const th = document.createElement("th");
        // set the key as textcontent in th
        th.textContent = key;
        // add the created th to headerRow
        headerRow.appendChild(th);
    }
    // add the row to the table  
    tableElement.appendChild(headerRow);
    
    // Loop the data
    data.forEach(item => {
        // create <tr> 
        const dataRow = document.createElement("tr");
        // Loop the data keys to create <td>
        for (let key in item) {
            const cell = document.createElement("td");
            // set the textContent to cells (= <td>)
              if (key === "unit_price") {
                cell.textContent = item[key] + " €";
            } else {
            cell.textContent = item[key];
            }
            // add the cells to row (= in <tr>)
            dataRow.appendChild(cell);
        }
    // add the datarow to the table
    tableElement.appendChild(dataRow)
});
}


  // function that filters products
  function filterProducts(){
    // 
    const searchTerm = inputElement.value.toLowerCase().trim();
    let filtered;
    // If user typed %-mark and wrote searchterm, filter the product list by checking if the product name includes the user's search text
    if (searchTerm[0] === "%") {
        // remove %-mark
        const term = searchTerm.slice(1);
        filtered = products.filter(item => 
            item.name.toLowerCase().includes(term)
        );
    }
    else {
        filtered = products.filter(item =>
            item.name.toLowerCase().startsWith(searchTerm)
        );
    }    
    // update the table with filtered results
    createTable(filtered);   

  }

  // funktion that sorts by name asc or desc
  function sortProducts () {
    // order = "asc" or "desc"
    const order = selectElement.value;
    let sorted = Array.from(products);
    
    sorted.sort((a,b) => {
        const nameA = a.name.toLowerCase();
        const nameB = b.name.toLowerCase();

        // if A before B
        if (nameA < nameB) {
            if (order === "asc") {
                // A-Z
                return -1;
                // else the order is "desc"
            } else {
                // Z-A
                return 1;
            }
        }
        // if A is after b
        if (nameA > nameB) {
            if (order === "asc") {
                // A-Z
                return 1;
            // else the order is "desc"
            } else {
                // Z-A
                return -1;
            }
        }
        // if the names are same
        return 0;
    });
    // create table from the sorted names
    createTable(sorted);


   
  }



   


    