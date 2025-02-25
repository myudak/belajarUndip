

Dear Applicants,

Thankyou on behalf of participating EWS Bascorro Exclusive Recruitment Programming Division. We would like to announce for your selection process and has made a decision.

Congratulations on Successfully Passing All Selection Stages!  

Your journey with us is almost complete. To proceed, you are required to take an Eligibility Test that will assess your readiness and knowledge. This test will cover topics including: 
1. Robot Knowledge: Ubuntu, ROS2, Servo, Mechanisms, and Microcontrollers
2. Commitment: Understanding your dedication to the role
3. Programming Knowledge: Matrix Operations, C Header Files, ROS2 service messages

---

### 1. **Robot Knowledge**

#### Ubuntu Basics
   - **Commands**: Familiarize yourself with essential commands for navigation (`cd`, `ls`, `pwd`), file management (`cp`, `mv`, `rm`, `touch`, `mkdir`), and package management (`apt update`, `apt install`, `apt remove`).
   - **Process and System Management**: Know commands like `ps`, `top`, `kill`, `chmod`, and `chown`.
   - **Expected Questions**:
      - "How do you install a package on Ubuntu?"
      - "How would you list all running processes and terminate one?"

#### ROS2 (Robot Operating System 2)
   - **Core Concepts**:
      - **Nodes**: Independent units of computation in ROS.
      - **Topics**: Channels for asynchronous communication between nodes.
      - **Services**: Synchronous communication with request-response structure.
      - **Actions**: Similar to services but used for long-running tasks.
   - **Commands**: `ros2 node list`, `ros2 topic echo`, `ros2 service call`
   - **Expected Questions**:
      - "What are the differences between topics and services in ROS2?"
      - "How would you create a simple publisher-subscriber system?"

#### Servo Mechanisms
   - **Basics**: Understand PWM (Pulse Width Modulation) signals, used to control the angle or speed of a servo.
   - **Applications**: Servo motors are used in robotics for controlled movement like rotating arms or wheels.
   - **Expected Questions**:
      - "How does PWM control a servo?"
      - "Explain a scenario where you would use a servo in a robot."

#### Mechanisms (Gears, Motors, Actuators)
   - **Types**: Know the difference between motors (DC, stepper) and actuators.
   - **Role in Robotics**: Used for movement, rotation, and power transfer.
   - **Expected Questions**:
      - "What is the difference between a DC motor and a stepper motor?"
      - "How would you choose between a motor and an actuator for a robotic arm?"

#### Microcontrollers (Arduino, Raspberry Pi)
   - **Programming**: Understand the basics of programming in Arduino IDE or Python for Raspberry Pi.
   - **Interfacing**: Know how to connect sensors and actuators, and how to read/write data.
   - **Expected Questions**:
      - "How do you control an LED with an Arduino?"
      - "What are the differences between Arduino and Raspberry Pi in robotics?"

---

### 2. **Commitment**

   - **Dedication and Motivation**: Be prepared to discuss why you're interested in robotics and how you plan to contribute.
   - **Teamwork and Communication**: Think of examples where you worked in a team or resolved conflicts.
   - **Expected Questions**:
      - "Why do you want to join our robotics division?"
      - "How do you handle teamwork in a technical project?"

---

### 3. **Programming Knowledge**

#### Matrix Operations
   - **Basic Operations**:
      - **Addition/Subtraction**: Element-wise operations.
      - **Multiplication**: Row-by-column multiplication rules.
   - **Transformations**: In robotics, matrix transformations are used for movements and rotations.
   - **Expected Questions**:
      - "Explain the process of matrix multiplication."
      - "How would you use matrices to represent a robot's movement?"

#### C Header Files
   - **Structure**: Header files contain declarations, while `.c` files have implementations.
   - **Purpose**: Organize code, provide function declarations, define macros and constants.
   - **Expected Questions**:
      - "Why do we use header files in C?"
      - "How would you declare a function in a header file?"

#### ROS2 Service Messages
   - **Core Concepts**:
      - **Service Definition**: Structure with request and response fields.
      - **Usage**: Services provide a way for nodes to request information from each other.
   - **Expected Questions**:
      - "How do you create a service in ROS2?"
      - "What is the difference between a service and a topic in ROS?"

---

### Cheatsheets

- **Ubuntu Commands**:
  ```bash
  # Basic file commands
  ls -la         # List files in detail
  cd /path       # Change directory
  cp file1 file2 # Copy file1 to file2
  mv file1 file2 # Rename or move file1 to file2
  rm file        # Remove file

  # Package management
  sudo apt update         # Update package list
  sudo apt install <pkg>  # Install a package
  sudo apt remove <pkg>   # Remove a package

  # Process management
  ps aux                  # List all processes
  top                     # Show CPU/memory usage
  kill <PID>              # Terminate process by PID
  ```

- **ROS2 Basic Commands**:
  ```bash
  # Starting ROS2
  ros2 run <package> <executable>    # Run a node
  ros2 topic list                    # List all active topics
  ros2 service list                  # List all services

  # Publishing/Subscribing
  ros2 topic pub <topic> <msg_type>  # Publish a message
  ros2 topic echo <topic>            # Listen to a topic
  ```

---

### Sample Questions and Answers

- **Question**: "Explain the main difference between ROS1 and ROS2."
  - **Answer**: "ROS2 was developed to address limitations in ROS1, especially for multi-robot and real-time applications. ROS2 uses DDS (Data Distribution Service) for communication, improving scalability and reliability. It also supports multiple platforms, including Windows."

- **Question**: "How does a DC motor differ from a servo?"
  - **Answer**: "A DC motor rotates continuously, controlled by adjusting voltage or PWM, making it ideal for wheels. A servo motor provides precise position control, useful in robotic arms where you need specific angle control."

- **Question**: "Describe a scenario where you'd use ROS2 services."
  - **Answer**: "ROS2 services are ideal for synchronous tasks where you need a request-response model, like querying the battery status. Unlike topics, which are continuous streams, services are for discrete interactions."

----

Here are concise answers to the sample questions:

1. **What are the main differences between ROS1 and ROS2?**
   - **Answer**: ROS2 improves upon ROS1 by introducing DDS (Data Distribution Service) for better communication, making it suitable for real-time, multi-robot applications. ROS2 also supports multiple platforms, including Windows, and offers improved scalability and reliability.

2. **How does a DC motor differ from a servo?**
   - **Answer**: A DC motor provides continuous rotation, making it ideal for wheels or movement where continuous speed control is needed, controlled by adjusting voltage or PWM. A servo motor, however, is designed for precise position control over specific angles, commonly used in robotic arms or mechanisms that need to hold a position.

3. **Describe a scenario where you’d use ROS2 services.**
   - **Answer**: ROS2 services are suitable for tasks that need a synchronous, request-response interaction, such as querying the battery status or checking a sensor’s specific value at a given moment. Unlike topics, which are used for continuous data streaming, services provide one-off, discrete responses.

4. **Why do we use header files in C?**
   - **Answer**: Header files in C are used to declare functions, macros, and constants, enabling code organization and reusability across multiple files. They separate interface declarations from implementation, so the main code can reference functions and constants without including full implementation details.

5. **How do you create a service in ROS2?**
   - **Answer**: In ROS2, creating a service involves defining a `.srv` file that specifies request and response fields, generating service code using `colcon build`, and writing a server and client node to handle and send requests.

6. **What is the difference between a service and a topic in ROS?**
   - **Answer**: A topic in ROS is for continuous, asynchronous data streams where multiple nodes can publish and subscribe. Services, however, provide a synchronous, request-response communication model, suitable for discrete actions where one node needs to receive a direct reply from another.

7. **Explain the process of matrix multiplication.**
   - **Answer**: In matrix multiplication, each element of the resulting matrix is the sum of the products of corresponding elements from the rows of the first matrix and columns of the second matrix. Matrix multiplication is only possible if the number of columns in the first matrix matches the number of rows in the second matrix.

8. **How would you use matrices to represent a robot's movement?**
   - **Answer**: Matrices can represent transformations like translation, rotation, and scaling. By applying transformation matrices to a robot's coordinate points, you can calculate its position, orientation, and movement in space, essential for tasks like navigation and arm manipulation.

9. **How does PWM control a servo?**
   - **Answer**: PWM (Pulse Width Modulation) controls a servo by adjusting the duty cycle of the signal, where the width of the pulse determines the angle of the servo. For example, a pulse of 1 ms might move it to 0°, 1.5 ms to 90°, and 2 ms to 180°, allowing precise angular positioning.

10. **What is the difference between Arduino and Raspberry Pi in robotics?**
    - **Answer**: Arduino is a microcontroller ideal for simple, real-time control tasks like sensor reading and actuator control. Raspberry Pi, being a full computer with an operating system, is more powerful and can handle complex tasks, such as vision processing, but is less suited for real-time operations.

11. **How do you install a package on Ubuntu?**
    - **Answer**: To install a package on Ubuntu, you use `sudo apt install <package_name>`, where `<package_name>` is the name of the software package. This command retrieves and installs the package and any dependencies from the Ubuntu repositories.

12. **How would you list all running processes and terminate one?**
    - **Answer**: Use `ps aux` to list all running processes, which shows details like process ID (PID). To terminate a specific process, use `kill <PID>`, where `<PID>` is the process ID of the target process.
