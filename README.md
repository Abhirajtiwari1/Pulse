# Pulse

Pulse is an AI platform designed to automate online tasks for visually impaired individuals. The platform leverages advanced AI technologies to assist users in navigating and interacting with digital content, making online activities more accessible and manageable.

## Features

- **Voice Command Integration:** Enables users to control the platform and perform tasks using voice commands.
- **Screen Reader Compatibility:** Works seamlessly with screen readers to provide auditory feedback for on-screen text and elements.
- **Task Automation:** Automates repetitive online tasks such as browsing, form filling, and data retrieval.
- **Personal Assistant:** Acts as a virtual assistant, helping users with daily online activities such as emailing, scheduling, and social media interaction.
- **Accessibility Enhancements:** Provides tools and features to improve the overall accessibility of web content.

## Installation

To install and run Pulse, follow these steps:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/Abhirajtiwari1/pulse.git
    cd pulse
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv env
    source env/bin/activate   # For Windows: env\Scripts\activate
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

5. **Access the platform:**
    Open a web browser and navigate to `http://127.0.0.1:8000/`.

## Usage

1. **Sign Up / Log In:**
    - Create a new account or log in with existing credentials to access the platform.
  
2. **Voice Commands:**
    - Use voice commands to navigate through the platform and perform tasks. Examples of commands can be found in the user manual.

3. **Automated Tasks:**
    - Set up and manage automated tasks through the user interface. Customize task parameters and schedules as needed.

4. **Personal Assistant:**
    - Utilize the personal assistant for various daily activities, including managing emails, setting reminders, and interacting with social media.

## Testing the Voice-Controlled AI Assistant

To test the voice-controlled AI assistant, ensure the following Python libraries are installed:

- `SpeechRecognition`
- `pyttsx3`
- `webbrowser`
- `os`

You can install these libraries using pip:

```sh
pip install SpeechRecognition pyttsx3
