// Modal Event Listener

$('#exampleModal').on('shown.bs.modal', function () {
    $('#myInput').trigger('focus')
  })

$('#exampleModal').on('shown.bs.modal', function () {
  $('#myInput').trigger('focus')
})

// Calculate Daily Exposure

$('#calc-daily-exposure').click(function () {

  console.log("Calc Daily Exposure Clicked")

  // Calculate Daily Exposure

  let partialExposure = [];

  // Source: https://stackoverflow.com/questions/50850109/create-array-from-specific-classes-texts

  $('.partial-exposure').each(function(){
    partialExposure.push($(this).text())
  });

  let dailyExposure = 0

  for (let i = 0; i < partialExposure.length; i++) {
    dailyExposure += Math.pow(partialExposure[i], 2);
  };

  dailyExposure = Math.sqrt(dailyExposure);
  dailyExposure = Math.round(dailyExposure * 10) / 10;

  $('#daily-exposure').text(dailyExposure);

  // Calculate Total Exposure Points

  let partialExposurePts = [];

  $('.partial-exposure-pts').each(function(){
    partialExposurePts.push($(this).text())
  });

  let dailyExposurePts = 0;

  for (let i = 0; i < partialExposurePts.length; i++) {
    dailyExposurePts += Number(partialExposurePts[i]);
  };

  $('#daily-exposure-pts').text(dailyExposurePts);

  // Update Exposure Warning and Specific Controls to Consider

  let belowEAVWarning = "Exposure likely to be below 2.5m/s² A(8) EAV (100 Points).";
  let aboveEAVWarning = "WARNING: Exposure at or above 2.5m/s² A(8) EAV (100 Points).";
  let aboveELVWarning = "WARNING: Exposure above 5m/s² A(8) ELV (400 Points).";

  let belowEAVControls = 
  `Where there is a risk to the health of an employee who is, or is liable to be, exposed to vibration, but their exposure is below the EAV, the employer must:

  (a) Ensure that the employee is placed under suitable health surveillance.
  (b) Provide the employee with suitable and sufficient information, instruction and training.`;
  let aboveEAVControls = 
  `Where the daily personal HAV exposure is likely to equal or exceed the EAV the employer must:

  (a) Reduce exposure to as low a level as is reasonably practicable by establishing and implementing a programme of organisational and technical measures which is appropriate to the activity.
  (b) Ensure that the employee is placed under suitable health surveillance.
  (c) Provide the employee with suitable and sufficient information, instruction and training.`;
  let aboveELVControls = 
  `Where the daily personal HAV exposure is likely to exceed the ELV the employer must take immediate action to:

  (a) Reduce exposure to vibration below the limit value.
  (b) Identify the reason for the limit being exceeded.
  (c) Modify the measures taken to prevent it being exceeded again.`;

  if (dailyExposure > 5) {
    $('#exposure-warning').text(aboveELVWarning);
    $('#exposure-warning').css("background-color", "red");
    $('#specific-controls').text(aboveELVControls);
  } else if (dailyExposure > 2.5) {
    $('#exposure-warning').text(aboveEAVWarning);
    $('#exposure-warning').css("background-color", "yellow");
    $('#specific-controls').text(aboveEAVControls);
  } else if (dailyExposure < 2.5) {
    $('#exposure-warning').text(belowEAVWarning);
    $('#exposure-warning').css("background-color", "lime");
    $('#specific-controls').text(belowEAVControls);
  }

  // Dont forget to reset the info when equipment list changes
  // Consider seperating the above into functions
});

