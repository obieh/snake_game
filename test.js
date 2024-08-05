import React, { useState } from 'react';

function ScheduleAppointment() {
  const [date, setDate] = useState('');
  const [time, setTime] = useState('');
  
  function handleSubmit(e) {
    e.preventDefault();
    // Send a post request to the back-end to schedule the appointment
    // with the selected date and time
    fetch('/schedule', {
      method: 'POST',
      body: JSON.stringify({ date, time }),
      headers: { 'Content-Type': 'application/json' },
    })
      .then(response => {
        if (!response.ok) {
          throw new Error('Failed to schedule appointment');
        }
        return response.json();
      })
      .then(data => {
        // Show a success message or redirect to the appointment confirmation page
        console.log(data);
      })
      .catch(error => {
        // Show an error message
        console.error(error);
      });
  }

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Select a date:
        <input
          type="date"
          value={date}
          onChange={e => setDate(e.target.value)}
        />
      </label>
      <label>
        Select a time:
        <input
          type="time"
          value={time}
          onChange={e => setTime(e.target.value)}
        />
      </label>
      <button type="submit">Schedule Appointment</button>
    </form>
  );
}

export default ScheduleAppointment;
