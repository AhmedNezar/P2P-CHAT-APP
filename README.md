# Peer-to-Peer Multi-User Chatting Application

## Ain Shams University - ChatApp

Welcome to the Peer-to-Peer Multi-User Chatting Application, a project developed by students from Ain Shams University. This application aims to provide a robust text-based communication platform inspired by popular apps like Clubhouse. The project is divided into four phases, focusing on network protocol design, client-server, and peer-to-peer architecture, utilizing Python and sockets, and incorporating TCP and UDP protocols.

## Project Overview

### Backlog of Requirements and User Stories

1. **User Authentication**
   - **Requirement:** Users must authenticate with a unique username and password.
   - **User Story:** Create an account with a unique username and password.
   - **User Story:** Log in using a registered username and password.

2. **Basic Client-Server Setup**
   - **Requirement:** Implement a basic server application to handle multiple client connections.
   - **User Story:** Connect to the server using a client application.
   - **User Story:** View a list of online users.

3. **Chat Room Functionality**
   - **Requirement:** Users can create and join chat rooms.
   - **User Story:** Create a new chat room.
   - **User Story:** Join an existing chat room.
   - **User Story:** View a list of available chat rooms.

4. **Group Messaging in Chat Rooms**
   - **Requirement:** Users can send and receive messages within a chat room.
   - **User Story:** Send a message to everyone in the chat room.
   - **User Story:** View messages from other users in the chat room.
   - **User Story:** Receive notifications for new messages.

5. **One-to-One Chat Functionality**
   - **Requirement:** Users can initiate one-to-one chat sessions.
   - **User Story:** Send a private message to another user.
   - **User Story:** Receive private messages from others.
   - **User Story:** Be notified of new private messages.

6. **Message Formatting and Features**
   - **Requirement:** Support basic text formatting (e.g., bold, italics) in messages.
   - **User Story:** Format messages to emphasize certain words.
   - **Requirement:** Users can share hyperlinks in messages.
   - **User Story:** Click on a hyperlink shared in a message to open a browser.

7. **Error Handling and Resilience**
   - **Requirement:** Implement robust error handling for unexpected scenarios.
   - **User Story:** Receive meaningful error messages for troubleshooting.
   - **Requirement:** Automatically reconnect users in case of a network interruption.

8. **User Interface (UI) Enhancements**
   - **Requirement:** Develop a command-line interface for simplicity.
   - **User Story:** Have a clean and intuitive command-line interface.
   - **Requirement:** Add color-coded messages for better visual distinction.
   - **User Story:** Easily identify different types of messages.

9. **Documentation**
   - **Requirement:** Create user documentation covering installation, configuration, and usage.
   - **User Story:** Have a comprehensive guide to set up and use the application.
   - **Requirement:** Technical documentation detailing system architecture, protocols, and codebase structure.

10. **Testing**
    - **Requirement:** Conduct unit testing for each implemented feature.
    - **User Story:** Ensure each component functions correctly in isolation.
    - **Requirement:** Perform integration testing to ensure seamless interactions between different components.
    - **Requirement:** Conduct stress testing to evaluate system performance under high loads.

11. **Scalability**
    - **Requirement:** Design the system to handle an increasing number of users and chat rooms efficiently.
    - **User Story:** Optimize data structures and algorithms for scalability.

### Project Phases

#### Phase 1: Project Planning and Design

- **Objective:** Define project scope, goals, and functionalities. Create a detailed design document.
- **Deliverables:**
  - Project proposal.
  - Design document.

#### Phase 2: Basic Client-Server Setup

- **Objective:** Implement foundational elements, including basic client-server communication.
- **Deliverables:**
  - Basic client and server applications.
  - TCP connection for user authentication.

#### Phase 3: Peer-to-Peer Architecture and Chat Rooms

- **Objective:** Integrate peer-to-peer architecture and implement chat rooms.
- **Deliverables:**
  - Modified server for peer-to-peer connections.
  - Chat room creation and joining functionalities.

#### Phase 4: One-to-One Chatting and Protocol Optimization

- **Objective:** Enable one-to-one chatting and optimize communication protocols.
- **Deliverables:**
  - One-to-one chat functionality.
  - Optimized TCP and UDP usage.
  - Performance testing results.
  - Finalized user interface.

#### Final Project Presentation and Documentation

- **Objective:** Compile and present the completed project, emphasizing learned concepts.
- **Deliverables:**
  - Finalized codebase.
  - User documentation.
  - Presentation slides or video.

## Technical Details

### Authentication

- User authentication involves a secure username and password exchange over TCP.
- Hashing algorithms used for secure storage and verification of user credentials.

### Communication Protocols

- TCP used for reliable communication, ensuring message delivery and order.
- UDP implemented for real-time interactions, such as broadcasting messages within chat rooms.

### User Interface

- Command-line interface developed for simplicity and ease of use.
- Color-coded messages and user-friendly commands considered for better visual distinction.

### Error Handling

- Robust error handling mechanisms implemented to manage unexpected scenarios.
- Meaningful error messages provided for troubleshooting.

### Documentation

- Comprehensive user documentation covering installation, configuration, and usage instructions.
- Technical documentation detailing system architecture, communication protocols, and codebase structure.

### Testing

- Thorough unit testing for each implemented feature.
- Integration testing to ensure seamless interactions between different components.
- Stress testing conducted to evaluate system performance under high loads.

### Scalability

- System designed to be scalable, accommodating an increasing number of users and chat rooms.
- Data structures and algorithms optimized for efficient resource utilization.

Feel free to customize this README file further based on your project's specific details and requirements. Good luck with your Peer-to-Peer Multi-User Chatting Application!
