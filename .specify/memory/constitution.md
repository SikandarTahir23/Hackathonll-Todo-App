<!-- SYNC IMPACT REPORT
Version change: 1.0.0 → 2.0.0 (Phase II transition)
Modified principles: All principles (complete rewrite for Phase II)
Added sections: All Phase II sections
Removed sections: Phase I specific sections
Templates requiring updates:
- .specify/templates/plan-template.md: ⚠ pending
- .specify/templates/spec-template.md: ⚠ pending
- .specify/templates/tasks-template.md: ⚠ pending
- .specify/templates/commands/*.md: ⚠ pending
- README.md: ⚠ pending
Follow-up TODOs: None
-->

# TaskMastery – Full-Stack Todo Web Application (Hackathon II) – Phase II Constitution

## Purpose of Phase II

This constitution governs the development of TaskMastery Phase II, establishing clear principles, constraints, and guidelines for AI behavior during the implementation of a professional, responsive, full-stack web application with authentication and persistent storage. This document ensures clean, focused evolution from Phase I while maintaining architectural integrity and preventing scope creep into advanced features.

## Role & Responsibility (AI + Human)

**AI Responsibilities:**
- Implement only features explicitly defined in Phase II specifications
- Enforce architectural boundaries and constraints between Phase I and Phase II
- Maintain code quality according to established standards
- Follow spec-driven development practices without deviation
- Alert when requested features violate Phase II scope or introduce Phase III+ complexity
- Ensure clean migration from Phase I console application to Phase II web application

**Human Responsibilities:**
- Define clear, testable Phase II specifications
- Approve all architectural decisions for Phase II
- Verify implementation matches Phase II specifications
- Maintain project direction within Phase II boundaries
- Ensure smooth transition from Phase I to Phase II

## Phase II Scope & Boundaries

**IN SCOPE:**
- Web application using Next.js 16+ (App Router)
- Professional, responsive UI with dashboard-style interface
- Login & Signup (popup/modal based authentication)
- User-specific Todo management
- Full CRUD operations on Todos (Create, Read, Update, Delete)
- Mark task as completed via icon
- Filtering (All / Pending / Completed)
- Persistent database storage using Neon Serverless PostgreSQL
- REST API using Python FastAPI
- SQLModel ORM for database operations
- Better Auth for authentication
- Migration from Phase I data structures (if applicable)
- Responsive design for desktop and mobile
- Session management and security best practices

**OUT OF SCOPE:**
- AI logic or decision-making capabilities
- Agents, MCP, or automation systems
- Analytics computation or reporting
- Team collaboration logic
- Realtime synchronization
- Role-based access control beyond basic user authentication
- Containers, Kubernetes, or cloud orchestration
- Third-party integrations
- Email notifications or communication
- File uploads or attachments
- Advanced search or filtering beyond basic requirements
- Offline functionality
- Progressive Web App (PWA) features
- WebSockets or real-time communication

## Allowed Technologies

**Frontend Technology Stack:**
- Next.js 16+ with App Router as the primary framework
- React for component-based UI development
- TypeScript for type safety
- Tailwind CSS or similar for styling
- Modern JavaScript (ES2020+) features
- Standard build tools and bundlers included with Next.js

**Backend Technology Stack:**
- Python 3.9+ as the primary backend language
- FastAPI for REST API development
- SQLModel as the ORM
- Neon Serverless PostgreSQL for persistent storage
- Better Auth for authentication and session management
- Standard Python libraries for utility functions

**Development Tools:**
- Git for version control
- Standard Python testing frameworks (pytest, unittest)
- Standard JavaScript/TypeScript testing frameworks (Jest, Vitest)
- Standard linters and formatters (flake8, black, eslint, prettier)
- Docker for local development (optional, not for deployment)

## Forbidden Technologies

**Explicitly Prohibited:**
- Any AI/ML libraries or frameworks for business logic
- Agent frameworks or MCP systems
- Real-time communication libraries (Socket.io, WebSockets)
- Container orchestration tools (Kubernetes)
- Cloud deployment platforms beyond Neon PostgreSQL
- Third-party analytics services
- Email delivery services
- File storage services beyond database storage
- Blockchain or distributed ledger technologies
- Advanced authentication methods beyond Better Auth
- Microservices architecture (must remain monolithic)
- GraphQL (REST API only)
- NoSQL databases (PostgreSQL only)
- Serverless functions beyond Next.js API routes

## UI & UX Governance Rules

**I. Responsive Design Priority**
All UI components must be fully responsive across desktop, tablet, and mobile devices. Mobile-first approach with progressive enhancement. All interactive elements must meet accessibility standards (WCAG 2.1 AA).

**II. Dashboard-Style Interface**
Primary interface must follow dashboard design patterns with clear information hierarchy. Navigation must be intuitive and consistent. Visual feedback for all user interactions is mandatory.

**III. Authentication UX**
Login and signup flows must be implemented as non-intrusive modals or popups. Session persistence must be secure and user-friendly. Password requirements and validation must follow security best practices.

**IV. Todo Management UX**
CRUD operations must be intuitive with clear visual feedback. Filtering controls must be prominently placed and easily accessible. Completed tasks must be visually distinct from pending tasks.

## Backend & API Governance Rules

**I. REST API Design**
All backend endpoints must follow REST principles with proper HTTP methods and status codes. API responses must be consistent and well-structured. Proper error handling and meaningful error messages are required.

**II. FastAPI Implementation**
All API endpoints must be implemented using FastAPI with proper type hints and validation. Request/response models must be defined using Pydantic. API documentation must be automatically generated.

**III. Database Operations**
All database interactions must use SQLModel ORM. Proper database connection management and transaction handling are mandatory. Database queries must be optimized to prevent performance issues.

**IV. API Security**
All API endpoints must implement proper authentication and authorization checks. Input validation must prevent injection attacks. Rate limiting should be considered for public endpoints.

## Authentication & Security Principles

**I. Better Auth Implementation**
Authentication must be implemented using Better Auth library only. Session management must follow security best practices. Password hashing and storage must be handled by the authentication library.

**II. User Data Isolation**
Each user's data must be properly isolated from other users. No user should be able to access another user's todos. Proper authorization checks must be implemented on all data access operations.

**III. Secure Communication**
All authentication-related communication must use HTTPS. Sensitive data must not be exposed in client-side code. Authentication tokens must be stored securely.

**IV. Session Management**
Proper session lifecycle management must be implemented. Sessions must expire appropriately. Remember me functionality should be optional and secure.

## Data Consistency & Integrity Rules

**I. Database Transaction Management**
All database operations that modify data must be wrapped in transactions when necessary. Data consistency must be maintained across related operations. Proper error handling for database failures is required.

**II. Data Validation**
All data must be validated before storage. Input validation must occur at both API and database levels. Data integrity constraints must be enforced at the database level.

**III. Migration from Phase I**
If migrating data from Phase I, data transformation must preserve all essential information. Migration process must be tested and reversible. Data loss during migration is strictly prohibited.

**IV. Error Handling**
Database errors must be properly handled without exposing internal details to users. Fallback mechanisms must be in place for critical operations. Data recovery procedures must be considered.

## Migration Rules from Phase I

**I. Architecture Evolution**
Phase I console application architecture must be completely replaced with Phase II web architecture. No console-based components should remain in the final Phase II application. Migration must preserve core business logic concepts.

**II. Data Structure Evolution**
Data models must evolve from in-memory structures to persistent database models. Schema design must accommodate user-specific data isolation. Migration scripts must be provided if applicable.

**III. Feature Mapping**
Core todo functionality from Phase I must be preserved in Phase II with enhanced capabilities. User experience must be significantly improved through the web interface. All Phase I functionality must have equivalent or improved Phase II implementations.

**IV. Code Reuse Constraints**
Only business logic concepts may be reused from Phase I; implementation code must be rewritten for the web architecture. No direct code copying between phases without proper adaptation.

## Quality, Performance & Maintainability Standards

**I. Performance Requirements**
Page load times must be under 3 seconds on standard broadband connections. API response times must be under 500ms for simple operations. Database queries must be optimized to prevent performance bottlenecks.

**II. Test Coverage Requirements**
All backend API endpoints must have corresponding integration tests. All frontend components must have unit tests. Critical paths must have end-to-end tests. Minimum 80% code coverage for acceptance.

**III. Code Quality Standards**
All code must follow established style guides for both Python and JavaScript/TypeScript. Proper documentation must be maintained for all public interfaces. Code complexity must be kept to a minimum.

**IV. Security Standards**
All security best practices must be followed. Input validation must prevent injection attacks. Authentication and authorization must be properly implemented. Security audits should be performed before deployment.

---

**Version**: 2.0.0 | **Ratified**: 2026-01-06 | **Last Amended**: 2026-01-06