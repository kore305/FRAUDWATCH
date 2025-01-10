# Fraud Detection Platform

This project is a Django-based platform that allows users to report scams and verify suspicious links. It integrates with the **IPQualityScore API** and **VirusTotal API** for enhanced fraud detection.

## Setup Instructions

### 1. Sign Up for API Keys

To enable fraud detection, you’ll need to sign up for **IPQualityScore** and **VirusTotal** to get your API keys.

- **IPQualityScore API**:  
  Go to [IPQualityScore](https://www.ipqualityscore.com/) and sign up for an account. After signing up, you will be able to generate an API key.

- **VirusTotal API**:  
  Go to [VirusTotal](https://www.virustotal.com/) and sign up for an account. Once you’re signed in, you can generate your API key.

### 2. Add API Keys to `settings.py`

Once you have the API keys, add them to your `settings.py` file. Add the following lines:

```python
IPQUALITYSCORE_API_KEY = 'your_ipqualityscore_api_key'
VIRUSTOTAL_API_KEY = 'your_virustotal_api_key'
Replace 'your_ipqualityscore_api_key' and 'your_virustotal_api_key' with the actual keys you received from IPQualityScore and VirusTotal.

3. Add VirusTotal API Key to background.js (for Scam Report Extension)
In addition to the Django backend, you’ll also need to include the VirusTotal API key in your browser extension to enable scam report functionality. Open the background.js file inside the extension folder and add your VirusTotal API key like so:

javascript
Copy code
const VIRUS_TOTAL_API_KEY = 'your_virustotal_api_key';
Replace 'your_virustotal_api_key' with your actual VirusTotal API key.

4. Add the Extension Folder to Chrome
To use the scam report extension, follow these steps to add the extension folder to Chrome:

Open Google Chrome.
Navigate to chrome://extensions/ in the browser’s address bar.
Enable Developer mode by toggling the switch in the top-right corner.
Click on Load unpacked.
In the file dialog, select the folder containing your extension files (including background.js).
Your extension will now be installed and active in Chrome.
5. Run the Application
Once you’ve added the API keys and set up the extension, you can run the Django application using the following commands:

python manage.py migrate
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to start using the fraud detection platform.






