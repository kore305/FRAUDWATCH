function switchTab(tab) {
    const linkTab = document.getElementById('linkTab');
    const phoneTab = document.getElementById('phoneTab');
    const linkInput = document.getElementById('linkInput');
    const phoneInput = document.getElementById('phoneInput');

    if (tab === 'link') {
        linkTab.classList.add('text-white', 'bg-blue-700');
        linkTab.classList.remove('text-gray-500');
        phoneTab.classList.remove('text-white', 'bg-blue-700');
        phoneTab.classList.add('text-gray-500');
        linkInput.classList.remove('hidden');
        phoneInput.classList.add('hidden');
    } else {
        phoneTab.classList.add('text-white', 'bg-blue-700');
        phoneTab.classList.remove('text-gray-500');
        linkTab.classList.remove('text-white', 'bg-blue-700');
        linkTab.classList.add('text-gray-500');
        phoneInput.classList.remove('hidden');
        linkInput.classList.add('hidden');
    }
}

function showPopup(popupId) {
    document.getElementById(popupId).style.display = 'block';
    document.getElementById('overlay').style.display = 'block';
}

function closePopup(popupId) {
    document.getElementById(popupId).style.display = 'none';
    document.getElementById('overlay').style.display = 'none';
}

document.getElementById('verificationForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const formData = new FormData(this);
    fetch('', {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.error_message) {
            document.getElementById('errorMessage').textContent = data.error_message;
            showPopup('errorPopup');
        } else if (data.verification_result) {
            if (data.verification_result.fraud_score !== undefined) {
                // Phone number result
                document.getElementById('phoneFraudScore').textContent = data.verification_result.fraud_score;
                document.getElementById('phoneCountry').textContent = data.verification_result.country;
                document.getElementById('phoneLocation').textContent = `${data.verification_result.city}, ${data.verification_result.region}`;
                document.getElementById('phoneCarrier').textContent = data.verification_result.carrier;
                document.getElementById('phoneLineType').textContent = data.verification_result.line_type;
                document.getElementById('phoneFormat').textContent = data.verification_result.international_format;
                document.getElementById('phoneName').textContent = data.verification_result.name || 'Not available';
                document.getElementById('phoneActive').textContent = data.verification_result.active ? 'Yes' : 'No';
                document.getElementById('phoneDoNotCall').textContent = data.verification_result.do_not_call ? 'Yes' : 'No';
                document.getElementById('phoneSpammer').textContent = data.verification_result.spammer ? 'Yes' : 'No';
                document.getElementById('phoneRisky').textContent = data.verification_result.risky ? 'Yes' : 'No';
                document.getElementById('phoneSafetyMessage').textContent = data.safety_message;
                showPopup('phoneResultPopup');
            } else {
                // Link result
                document.getElementById('linkScanDate').textContent = data.verification_result.scan_date;
                document.getElementById('linkPositives').textContent = data.verification_result.positives;
                document.getElementById('linkTotalScans').textContent = data.verification_result.total;
                document.getElementById('linkMessage').textContent = data.verification_result.verbose_msg;
                document.getElementById('linkSafetyMessage').textContent = data.safety_message;
                showPopup('linkResultPopup');
            }
        }
    })
    .catch(error => {
        document.getElementById('errorMessage').textContent = 'An error occurred while processing your request.';
        showPopup('errorPopup');
    });
});