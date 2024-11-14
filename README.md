# Template
 Template repository with default folder structure

# Template
 Template repository with default folder structure


 # Purpose


This project allows you to 

## Prerequisites

Ensure you have the following:
- macOS installed.
- Python 3.x installed on your machine.
- 

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tooh/[project].git
   cd [project folder]
 
2. **Install Python Dependencies**

   Install the required Python libraries

   ```bash
   pip3 install requirements


3. **Configuration**

   INI File Setup

   The script uses a config.ini file for configuration. A template for this file is available in the templates folder. 
   Create this file in the root directory of this project with the following structure:

   ```bash
   [Hue]
   BRIDGE_IP = [IP of your Hue bridge]
   LIGHT_ID = 4 [Light ID of the lap you want to switch]
   USERNAME =[API key]      
   API_KEY = [API key]

   FOCUS_MODE = 'Music Production'


4. **Running the Project**

   After configuring the config.ini file, run the Python script to listen for incoming MIDI signals and connect to the Hue bridge:

   ```bash
   python [project].py


## Additional Setup


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE. See the LICENSE file for details.
