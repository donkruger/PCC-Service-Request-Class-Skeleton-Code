// JavaScript Form Submission
document.getElementById("serviceRequestForm").addEventListener("submit", function(event) {
  event.preventDefault(); // Prevent form from submitting by default
  
  const name = document.getElementById("name").value;
  const mobile = document.getElementById("mobile").value;
  const service = document.getElementById("service").value;
  const date = document.getElementById("date").value;

  // Simple form validation to ensure no fields are empty
  if (!name || !mobile || !service || !date) {
    alert("Please fill in all the fields.");
    return;
  }

  alert("Service Request Submitted Successfully!");

  // Form reset
  this.reset();
});
