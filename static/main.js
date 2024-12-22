document.addEventListener('DOMContentLoaded', () => {

    const insertButton = document.getElementById('insertButton');
    const responseContainer = document.getElementById('responseContainer');

    insertButton.addEventListener('click', async () => {
        try {
            const response = await fetch('http://localhost:5000/init_main_data');
            if (!response.ok) {
                throw new Error(`HTTP error! Status: ${response.status}`);
            }
            const data = await response.text();
            responseContainer.innerHTML = `<p style="color: green ">${data}</p>`;
        } catch (error) {
            responseContainer.innerHTML = `<p style="color: red;">Error: ${error.message}</p>`;
        }
    });
});