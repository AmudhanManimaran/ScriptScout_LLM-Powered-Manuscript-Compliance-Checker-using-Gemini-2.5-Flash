async function checkCompliance() {
    const fileInput = document.getElementById('paper-file');
    const reportDiv = document.getElementById('report-view');
    const loading = document.getElementById('loading');

    if (fileInput.files.length === 0) return alert("Upload a manuscript!");

    const formData = new FormData();
    formData.append('manuscript', fileInput.files[0]);

    loading.style.display = 'block';
    reportDiv.innerText = "";

    try {
        const response = await fetch('/audit', { method: 'POST', body: formData });
        const data = await response.json();
        reportDiv.innerText = data.report || data.error;
    } catch (e) {
        reportDiv.innerText = "Connection Error.";
    } finally {
        loading.style.display = 'none';
    }
}