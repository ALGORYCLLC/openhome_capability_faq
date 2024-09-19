### Q: What is OpenHome and what are its use cases?
**A:** OpenHome is an open-source AI smart speaker project that aims to create a versatile, adaptive, and personalized voice-based AI companion. Its primary use cases include:
Personal assistance: OpenHome can respond to commands, answer queries, and engage in casual conversations.
Customizable AI interactions: Users can tailor the AI's personality to their preferences, creating a more personalized experience.
Development platform: OpenHome serves as a playground for developers to implement creative ideas and contribute to an evolving AI ecosystem.
Smart home integration: As a smart speaker, it can potentially control and interact with other smart home devices.
Continuous learning: The AI adapts and grows based on user interactions, providing an ever-improving experience.
Accessible AI development: OpenHome offers an easy-to-understand codebase for developers of all skill levels to contribute and learn about AI and smart speaker technology.
OpenHome's vision is to create a world where AI smart speakers become adaptive companions, pushing the boundaries of what's possible in voice-based AI interactions.

### Q: What is a capability in OpenHome?
**A:** Capabilities in OpenHome are modular functions or features that enhance its usability and interactivity. 
They allow you to customize how OpenHome operates by adding or modifying functionalities, such as integrating smart home devices or enabling specific AI-driven responses.
On the Capabilities page, you can manage, view, and configure these capabilities:
- **My Capabilities**: View custom capabilities you have created.
- **Published Capabilities**: See all the capabilities you have published.
- **Installed Capabilities**: Manage the capabilities currently installed in your OpenHome system.
Capabilities can be controlled in various ways:
- **Enable/Disable**: Turn a capability on or off.
- **Agent/System Capability**: Choose whether a capability applies to the AI agent or the broader system.
- **Trigger Words**: Configure words or phrases that will activate a particular capability.
You can also uninstall a capability when no longer needed. Capabilities make OpenHome a highly flexible and personalizable AI experience.

### Q: What is a personality in OpenHome?
**A:** A personality in OpenHome is a customizable AI character profile that defines how the smart speaker interacts with users. Personalities include specific traits, behaviors, and voices that shape the AI's responses and overall interaction style. Users can create, edit, and manage multiple personalities, each with unique characteristics such as:
A name and description
A cold start message (initial greeting)
A defined purpose or intended function
An associated voice ID for text-to-speech interactions
An optional personality image
These personalities allow users to tailor their OpenHome experience, creating diverse and engaging interactions with the AI assistant. Users can switch between different personalities or create new ones to suit various needs or preferences.

### Q: How to add a new capability to OpenHome?
**A:** To add a new capability to OpenHome:
Navigate to the "Add New Capability" section.
Provide basic information:
Enter a name for the capability
Write a description of its function
Upload an icon to represent the capability (optional)
Choose one of two methods to add the capability:
a. Upload a custom file:
Toggle on the "Upload custom File" option
Upload a .zip file containing the capability code (init.py, main.py, and config.json)
b. Use a template:
Keep the toggle off
Select a template from the dropdown
Modify the template's main.py in the live editor
Add trigger words or phrases that will activate this capability
Click "Submit" to add the new capability
This process allows you to extend OpenHome's functionality with either custom-built capabilities or by modifying existing templates.

### Q: How to add a new personality in OpenHome?
**A:** To add a new personality in OpenHome:
Navigate to the "MY PERSONALITIES" page.
Click the "Add New Personality" button.
Fill in the required fields in the form that appears:
Name: Enter a name for the personality
Personality Image: Upload an image to represent the personality (optional)
Cold Start Message: Write an initial greeting or introduction for the personality
Description: Provide a brief description of the personality's characteristics
Additional settings:
Purpose: Define the intended use or function of this personality
Voice ID: Select a voice from the dropdown list for text-to-speech
Text to speech: Enter sample text to test the selected voice
Agent Capabilities: Choose relevant capabilities for this personality (e.g., weather, storytelling)
Click "More Options" to access any additional settings if needed
Click "Save" to create the new personality, or "Cancel" to discard changes
After creating a personality, you can:
Preview it using the play icon
Share it with others
Edit or delete it using the icons next to each personality
Reset its settings to default
The personality will then appear on your "MY PERSONALITIES" page, where you can manage all your created personalities.

### Q: What is the difference between system and agent capabilities in OpenHome?
**A:** System capabilities and agent capabilities in OpenHome differ in their scope and how they are applied to personalities:
System Capabilities:
When a capability is enabled and set as a system capability, it becomes available to all personalities created by the user.
The system capability toggle is represented by an orange switch in the user interface.
System capabilities provide a broader, universal set of functions across all personalities.
Agent Capabilities:
When a capability is set as an agent capability, it is only available to specific personalities for which it was selected during creation or editing.
The agent capability toggle is represented by a black switch in the user interface.
Agent capabilities allow for more tailored functionality for individual personalities.
Key points:
System and agent capabilities are mutually exclusive for a given capability. They cannot both be active at the same time.
When the agent capability is toggled on, the system capability is automatically toggled off, and vice versa.
Users can choose which capabilities to assign to specific personalities during the creation or editing process, as seen in the "Edit Personality" interface where "Agent Capabilities" can be selected.
This system allows for flexible configuration of capabilities, enabling users to have some functions available across all personalities while restricting others to specific personality profiles.

### Q: Can I create custom capabilities on the OpenHome application?
**A:** Yes, you can create custom capabilities on the OpenHome application. Here's how:
Navigate to the "CAPABILITIES" page in the OpenHome dashboard.
Click on "Add Custom Capability" or select an existing capability to edit.
In the capability creation/editing form:
Enter a Capability Name and Description
Optionally upload an image for the capability
Add Trigger Words that will activate this capability
You have two main options for creating a custom capability:
a. Use a template:
Keep the "Upload Custom File" toggle off
Select a template from the dropdown (e.g., "basic")
Click "Open Editor" to modify the template in the live editor
b. Upload a custom file:
Toggle on "Upload Custom File"
Upload your custom Python files
If using the template option, you'll be taken to the "CUSTOMIZE CAPABILITY" page where you can edit the code:
The main functionality is in main.py
You can modify the code inside the call method of the capability class
Don't delete the class definition, call method, or imports as they are necessary for running the capability
In the code editor, you can:
Write custom code using available functions or create new ones
Create multiple versions of your capability by clicking the "Commit" button
Revert to a previous version if needed
Save new changes or discard them using the respective buttons
Start a live test to check your newly added custom functionality
The capability structure includes:
main.py: Contains the main capability class and logic
__init__.py: Likely contains initialization code
config.json: Stores configuration data like the unique name and matching hotwords
By following these steps, you can create, customize, and test new capabilities tailored to your specific needs in the OpenHome application.

### Q: What is the Marketplace in OpenHome?
A:
The Marketplace in OpenHome is a platform where you can explore, install, and manage various AI personalities and capabilities to customize and enhance your experience.
Capabilities Marketplace: You can browse through different capabilities, view their descriptions, triggers, and ratings, and use the search bar to find specific capabilities. You can easily install or uninstall capabilities with a click.
Personalities Marketplace: Discover a variety of AI personalities, each with detailed descriptions, ratings, and key features. You can install new personalities from the Marketplace, and explore featured personalities that are highlighted for their unique attributes.