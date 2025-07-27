const rows = ['A', 'B', 'C', 'D', 'E', 'F', 'G'];
const seatsPerRow = 10;
const seatPrice = 200;
const bookedSeats = ['A3', 'B5', 'C1', 'D7', 'F4'];

const layout = document.getElementById("seatsLayout");
const seatCount = document.getElementById("seat-count");
const totalPrice = document.getElementById("total-price");
const confirmBtn = document.getElementById("confirm-btn");

function createSeats() {
  rows.forEach(row => {
    const rowDiv = document.createElement('div');
    rowDiv.classList.add('row');

    const label = document.createElement('div');
    label.classList.add('row-label');
    label.textContent = row;
    rowDiv.appendChild(label);

    for (let i = 1; i <= seatsPerRow; i++) {
      const seat = document.createElement('div');
      const seatID = `${row}${i}`;
      seat.classList.add('seat');
      seat.dataset.id = seatID;

      if (bookedSeats.includes(seatID)) {
        seat.classList.add('booked');
      }

      rowDiv.appendChild(seat);
    }

    layout.appendChild(rowDiv);
  });
}

function updateSummary() {
  const selected = document.querySelectorAll('.seat.selected');
  seatCount.textContent = selected.length;
  totalPrice.textContent = selected.length * seatPrice;
}

layout.addEventListener('click', e => {
  if (e.target.classList.contains('seat') && !e.target.classList.contains('booked')) {
    e.target.classList.toggle('selected');
    updateSummary();
  }
});

confirmBtn.addEventListener('click', () => {
  const selected = document.querySelectorAll('.seat.selected');
  if (selected.length === 0) {
    alert("Please select at least one seat.");
    return;
  }

  const selectedSeats = [...selected].map(seat => seat.dataset.id);
  alert(`🎉 Booking Confirmed!\nSeats: ${selectedSeats.join(', ')}`);
  selected.forEach(seat => {
    seat.classList.remove('selected');
    seat.classList.add('booked');
  });
  updateSummary();
});

createSeats();
updateSummary();
