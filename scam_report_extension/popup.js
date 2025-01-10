document.addEventListener('DOMContentLoaded', function() {
  document.getElementById('scamReportForm').addEventListener('submit', function(event) {
      event.preventDefault();
      
      const formData = new FormData(this);
      
      fetch('http://127.0.0.1:8000/scam_report/report/', {  // Update this URL to match your Django URL configuration
          method: 'POST',
          body: formData,
          headers: {
              'X-Requested-With': 'XMLHttpRequest'  // This header indicates an AJAX request
          }
      })
      .then(response => response.json())
      .then(data => {
          if (data.errors) {
              // Display form errors
              let errorMessage = 'Please correct the following errors:\n';
              for (let field in data.errors) {
                  errorMessage += `${field}: ${data.errors[field].join(', ')}\n`;
              }
              document.getElementById('responseMessage').textContent = errorMessage;
          } else {
              document.getElementById('responseMessage').textContent = data.message;
              this.reset();  // Reset the form
          }
      })
      .catch(error => {
          console.error('Error:', error);
          document.getElementById('responseMessage').textContent = 'Failed to submit report. Please try again.';
      });
  });
});