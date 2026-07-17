// ================================
// Cloud Event Dashboard
// ================================

// Replace this after creating API Gateway
const API_URL = "https://q2rt7pzak7.execute-api.ap-south-1.amazonaws.com/employees";

const tableBody = document.getElementById("tableBody");
const totalRecords = document.getElementById("totalRecords");
const lastUpdated = document.getElementById("lastUpdated");
const loader = document.getElementById("loader");
const refreshBtn = document.getElementById("refreshBtn");
const employeeTable = document.getElementById("employeeTable");

// Hide table initially
employeeTable.style.display = "none";

// -------------------------------
// Load Data
// -------------------------------

async function loadEmployees() {

    loader.style.display = "flex";
    employeeTable.style.display = "none";

    try {

        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Unable to fetch data.");
        }

        const data = await response.json();

        renderTable(data);

    }

    catch (error) {

        console.error(error);

        tableBody.innerHTML = `
            <tr>
                <td colspan="4">
                    Failed to load data.
                </td>
            </tr>
        `;

        totalRecords.textContent = "0";

    }

    finally {

        loader.style.display = "none";
        employeeTable.style.display = "table";

        lastUpdated.textContent =
            new Date().toLocaleTimeString();

    }

}

// -------------------------------
// Render Table
// -------------------------------

function renderTable(data) {

    tableBody.innerHTML = "";

    totalRecords.textContent = data.length;

    data.forEach(emp => {

        const row = document.createElement("tr");

        row.innerHTML = `

            <td>${emp.id}</td>

            <td>${emp.name}</td>

            <td>${emp.department}</td>

            <td>₹ ${Number(emp.salary).toLocaleString()}</td>

        `;

        tableBody.appendChild(row);

    });

}

// -------------------------------
// Refresh Button
// -------------------------------

refreshBtn.addEventListener("click", loadEmployees);

// -------------------------------
// Auto Refresh Every 30 Seconds
// -------------------------------

setInterval(loadEmployees, 30000);

// -------------------------------
// Initial Load
// -------------------------------

loadEmployees();
