| Requirement Category     | Task Description                                                                                                       | Checkbox |
|--------------------------|------------------------------------------------------------------------------------------------------------------------|----------|
| General Requirements     | Code follows PEP 8 style guide                                                                                        | [ ]      |
|                          | Code is documented with comments                                                                                       | [ ]      |
|                          | Unit tests are created                                                                                                 | [ ]      |
| MQTT Configuration       | **CarPark Class:**                                                                                                     |          |
|                          | Subscribes to MQTT topics                                                                                              | [ ]      |
|                          | Publishes MQTT messages                                                                                                | [ ]      |
|                          | Can parse messages from sensor                                                                          | [ ]      |
|                          | Sends MQTT message that includes available bays, temperature                                                                         | [ ]      |
|                          | **Sensor Class:**                                                                                                      |          |
|                          | Publishes MQTT messages                                                                                                | [ ]      |
|                          | Sends MQTT messages that include temperature, time, and entry/exit                                                                                        | [ ]      |
|                          | **Display Class:**                                                                                                     |          |
|                          | Subscribes to MQTT topics                                                                                              | [ ]      |
|                          | Parses MQTT messages from car park                                                                                        | [ ]      |
| Configuration File       | **CarPark Class:**                                                                                                     |          |
| Management               | Reads initial configuration from a file                                                                                | [ ]      |
|                          | Writes available bays to a configuration class                                                                         | [ ]      |
|                          | **Sensor Class:**                                                                                                      |          |
|                          | Reads initial configuration from a file                                                                                | [ ]      |
|                          | **Display Class:**                                                                                                     |          |
|                          | Reads initial configuration from a file                                                                                | [ ]      |
| Testing Requirements     | At least one test case for CarPark Class                                                                               | [ ]      |
|                          | At least one test case for Sensor or Display Class                                                                     | [ ]      |
| Additional Requirements  | Invent your own protocol for transmitting information; JSON is recommended                                             | [ ]      |
| Git Requirements         | Forked the original project repository                                                                                 | [ ]      |
|                          | At least 3 local commits and 3 remote commits with reasonable messages                                                  | [ ]      |
|                          | Worked in a feature branch and merged the feature branch                                                               | [ ]      |
|                          | Both origin and local copy are synchronized at time of submission                                                      | [ ]      |
| Submission Guidelines    | Code files organized in coherent folder structure                                                                      | [ ]      |
|                          | Unit tests are submitted alongside the main code                                                                       | [ ]      |
|                          | Configuration files used for testing are included in the submission                                                    | [ ]      |
|                          | Submitted a zip file containing your code (excluding `venv/`, but including `.git/`)                                   | [ ]      |
|                          | Ensure your lecturer has access to your GitHub repository                                                              | [ ]      |
|                          | Completed the project journal                                                                                          | [ ]      |

Please use this updated table as a comprehensive guide for the project requirements. Ensure each task is completed and checked off before submitting your project for assessment.
Note there is a high-level (less detailed) checklist in the project journal, which is also used for grading. 
While there are a lot of items here, most items are small and can be addressed with 1-3 lines of code.
