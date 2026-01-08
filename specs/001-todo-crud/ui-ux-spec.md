# TaskMastery – Full-Stack Todo Web Application
## Phase II: UI & UX Specification

### 1. Overview

This document specifies the user interface and user experience requirements for TaskMastery Phase II, a responsive web application with dashboard-style layout. The specification defines all UI components, user flows, and interaction patterns that must be implemented while adhering to the constraints established in the Phase II Constitution.

### 2. Application Architecture

**Application Type**: Responsive Web Application
**Framework**: Next.js 16+ (App Router) with React
**Layout Style**: Dashboard-style with responsive design
**Design Philosophy**: Professional, clean, modern UI with intuitive user experience

### 3. Public Landing Page (Before Login)

#### 3.1 Navigation Bar
- **Logo/Title**: "TaskMastery" - prominently displayed on the left
- **Navigation Links** (left to right):
  - AI Chat (leads to placeholder UI)
  - Dashboard (leads to login)
- **Authentication Links** (right-aligned):
  - Login (modal/popup)
  - Sign Up (modal/popup)

#### 3.2 Hero Section
- **Headline**: 
  - Primary: "🚀 The Future of Productivity"
  - Secondary: "Transform Your Tasks Into Accomplishments"
- **Description**: 
  - "Harness the power of AI to organize, prioritize, and execute your tasks with precision. Join thousands of professionals who have revolutionized their workflow."
- **Primary Call-to-Action Buttons**:
  - "Get Started" (primary button style)
  - "Try AI Chat" (secondary button style)

#### 3.3 Statistics Section
- Displayed in three columns:
  - "95% Task Completion"
  - "4.8/5 User Rating" 
  - "10K+ Active Users"
- Each statistic includes an icon and brief description

#### 3.4 Features Section
- Grid layout showcasing six features with icons:
  - AI-Powered Insights
  - Smart Organization
  - Focus Mode
  - Real-time Sync
  - Advanced Analytics
  - Team Collaboration
- **Note**: These are UI-level representations only. No backend functionality is implemented in Phase II.

#### 3.5 How It Works Section
- Three-step process with visual indicators:
  1. "Add Your Tasks"
  2. "AI Organizes" (conceptual only)
  3. "Execute & Track"
- Each step includes an icon and brief description

#### 3.6 Sample Task Preview
- Visual representation of a task card:
  - Task title
  - Due date
  - Priority indicator
  - Mark-complete icon
  - Static AI suggestion text (example only)
- **Note**: This is a visual representation only, not functional in Phase II

#### 3.7 Testimonials Section
- Three professional user testimonials in card format
- Each includes user photo, name, title, and testimonial text

#### 3.8 Final CTA and Footer
- **Call-to-Action**:
  - "Start Free Trial" button
  - "Sign In" link
- **Footer**:
  - Copyright: "© 2025 TaskMastery. Precision tools for productive minds."
  - Navigation links to important pages

### 4. Authentication UI

#### 4.1 Login Modal/Popup
- **Trigger**: "Login" link in navigation bar
- **Components**:
  - Email input field
  - Password input field
  - "Forgot Password" link
  - "Login" button
  - "Don't have an account? Sign Up" link
- **Behavior**: 
  - Appears as modal/popup overlay
  - Closes when user clicks outside or presses ESC
  - On successful authentication, redirects to Dashboard

#### 4.2 Signup Modal/Popup
- **Trigger**: "Sign Up" link in navigation bar
- **Components**:
  - Name input field
  - Email input field
  - Password input field
  - Confirm Password input field
  - "Sign Up" button
  - "Already have an account? Login" link
- **Behavior**:
  - Appears as modal/popup overlay
  - Closes when user clicks outside or presses ESC
  - On successful registration, redirects to Dashboard

#### 4.3 Authentication Flow
- **Unauthenticated Access**: 
  - Dashboard and protected routes redirect to login
  - Authentication modals appear as needed
- **Successful Authentication**:
  - User session established
  - Redirect to Dashboard
  - Navigation bar updates to show user-specific options

### 5. Dashboard (After Login)

#### 5.1 Layout Structure
- **Three-column layout**:
  - Left Sidebar (navigation)
  - Main Content Area (task management)
  - Right Panel (AI Chat placeholder)

#### 5.2 Left Sidebar
- **Navigation Items**:
  - Dashboard (active state indicator)
  - My Tasks (with task count badge)
  - Completed Tasks (with task count badge)
  - Logout
- **Behavior**:
  - Active state clearly indicated
  - Task counts update dynamically when tasks are added/removed/completed

#### 5.3 Main Content Area

##### 5.3.1 Todo List Display
- **Task Card Components**:
  - Task title (editable)
  - Due date (optional)
  - Priority indicator (low/medium/high)
  - Mark-complete checkbox/icon
  - Edit/delete buttons (visible on hover)
- **Visual States**:
  - Pending tasks: standard appearance
  - Completed tasks: strikethrough, faded appearance
  - High priority: highlighted or colored indicator

##### 5.3.2 CRUD Operations
- **Add Task**:
  - "Add Task" button at top of list
  - Opens form with fields: title, due date, priority
  - Task appears immediately in list upon submission
- **Edit Task**:
  - Edit icon appears on task hover
  - Opens inline editor or modal
  - Updates task immediately upon save
- **Delete Task**:
  - Delete icon appears on task hover
  - Confirmation dialog before deletion
  - Removes task immediately from list
- **Mark Complete**:
  - Checkbox or icon to mark task as complete
  - Visual change to task appearance upon completion
  - Updates sidebar task counts

##### 5.3.3 Filtering System
- **Filter Options** (displayed as tabs/buttons):
  - "All" (shows all tasks)
  - "Pending" (shows incomplete tasks only)
  - "Completed" (shows completed tasks only)
- **Behavior**:
  - Active filter clearly indicated
  - Task list updates immediately when filter changes
  - Filter selection persists during session

#### 5.4 Right Panel - AI Chat (Placeholder)

##### 5.4.1 Chat Interface
- **Visual Components**:
  - Chat history area (displays placeholder messages)
  - Text input field
  - Send button
- **Behavior**:
  - When user submits text in input field:
    - Message appears in chat history
    - Task is added visually to the main task list
    - No real AI processing occurs (Phase III deferred)
  - Placeholder messages provide example interactions

##### 5.4.2 Placeholder Functionality
- **Note**: This is a visual placeholder only
- No actual AI processing or intelligence
- Messages and responses are predetermined examples
- Task creation from chat is visual demonstration only

### 6. User Experience Guidelines

#### 6.1 Interaction Patterns
- **Immediate Feedback**: 
  - CRUD actions update UI immediately without waiting for server response
  - Visual indicators for loading states when appropriate
- **Consistent Navigation**:
  - Clear breadcrumbs and navigation paths
  - Consistent placement of common elements
- **Responsive Design**:
  - Adapts to desktop, tablet, and mobile screens
  - Touch-friendly elements on mobile devices

#### 6.2 Visual Design Standards
- **Typography**:
  - Professional, readable fonts
  - Clear visual hierarchy with appropriate sizing
  - Consistent font weights and styles
- **Spacing**:
  - Consistent padding and margins
  - Adequate white space for readability
- **Color Scheme**:
  - Professional color palette
  - Consistent use of colors for different states
  - Accessibility-compliant contrast ratios

#### 6.3 Accessibility Requirements
- **Keyboard Navigation**:
  - All interactive elements accessible via keyboard
  - Clear focus indicators
- **Screen Reader Support**:
  - Proper ARIA labels and roles
  - Semantic HTML structure
- **Color Independence**:
  - Information not conveyed by color alone

### 7. Technical Constraints

#### 7.1 Prohibited Functionality
- No AI logic or decision-making capabilities
- No agents, MCP, or automation systems
- No analytics computation or reporting
- No team collaboration logic
- No real-time synchronization
- No advanced authentication beyond Better Auth
- No containers, Kubernetes, or cloud orchestration

#### 7.2 Allowed Technologies
- Next.js 16+ with App Router
- React for component-based UI
- Tailwind CSS or similar for styling
- Better Auth for authentication
- Standard JavaScript/TypeScript

### 8. Quality Standards

#### 8.1 Performance Requirements
- Page load times under 3 seconds on standard broadband
- Responsive interactions with minimal lag
- Optimized rendering of task lists

#### 8.2 Cross-Browser Compatibility
- Support for modern browsers (Chrome, Firefox, Safari, Edge)
- Consistent experience across supported browsers

#### 8.3 Mobile Responsiveness
- Fully functional on mobile devices
- Touch-friendly interface elements
- Adaptive layouts for different screen sizes

### 9. Validation Criteria

#### 9.1 UI Completeness
- All specified UI components implemented
- Navigation flows work as specified
- Authentication modals function correctly

#### 9.2 UX Consistency
- Consistent design language throughout application
- Intuitive user flows
- Immediate feedback for user actions

#### 9.3 Compliance with Constitution
- No prohibited functionality implemented
- All features within Phase II scope
- Technology stack adheres to specified constraints