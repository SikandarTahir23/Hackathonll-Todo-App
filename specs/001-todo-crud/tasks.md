---

description: "Task list for Todo Task CRUD – Phase I (Console, In-Memory) implementation"
---

# Tasks: Todo Task CRUD – Phase I (Console, In-Memory)

**Input**: Design documents from `/specs/001-todo-crud/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/

**Tests**: The feature specification includes validation requirements, so test tasks are included.

**Organization**: Tasks are grouped by user story to enable independent implementation and testing of each story.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (e.g., US1, US2, US3)
- Include exact file paths in descriptions

## Path Conventions

- **Single project**: `src/`, `tests/` at repository root
- Paths shown below assume single project - adjust based on plan.md structure

## Phase 1: Setup (Shared Infrastructure)

**Purpose**: Project initialization and basic structure

- [ ] T001 Create project structure per implementation plan in src/
- [ ] T002 [P] Create src/models/, src/services/, and src/cli/ directories
- [ ] T003 [P] Create tests/unit/, tests/integration/ directories

---

## Phase 2: Foundational (Blocking Prerequisites)

**Purpose**: Core infrastructure that MUST be complete before ANY user story can be implemented

**⚠️ CRITICAL**: No user story work can begin until this phase is complete

- [x] T004 Create Task model in src/models/task.py with id, description, completed fields
- [x] T005 Create TaskList collection in src/models/task.py with all required operations
- [x] T006 [P] Create main.py entry point with basic command loop structure
- [x] T007 [P] Create command_handler.py skeleton in src/cli/ for command parsing
- [x] T008 [P] Create todo_service.py skeleton in src/services/ for business logic
- [x] T009 Implement basic validation and error handling infrastructure

**Checkpoint**: Foundation ready - user story implementation can now begin in parallel

---

## Phase 3: User Story 1 - Add New Tasks (Priority: P1) 🎯 MVP

**Goal**: Enable users to add new tasks to their todo list through the console

**Independent Test**: Can be fully tested by entering the add command and verifying the task appears in the list, delivering the core value of capturing tasks.

### Tests for User Story 1 ⚠️

> **NOTE: Write these tests FIRST, ensure they FAIL before implementation**

- [x] T010 [P] [US1] Unit test for Task creation in tests/unit/test_task.py
- [x] T011 [P] [US1] Unit test for TaskList.add_task() in tests/unit/test_tasklist.py
- [x] T012 [P] [US1] Integration test for add command flow in tests/integration/test_add_task.py

### Implementation for User Story 1

- [x] T013 [US1] Implement add_task command validation in src/cli/command_handler.py
- [x] T014 [US1] Implement add_task business logic in src/services/todo_service.py
- [x] T015 [US1] Connect command handler to service for add operation
- [x] T016 [US1] Implement success response formatting for add operation
- [x] T017 [US1] Implement error handling for empty description validation

**Checkpoint**: At this point, User Story 1 should be fully functional and testable independently

---

## Phase 4: User Story 2 - View All Tasks (Priority: P1)

**Goal**: Enable users to view all their tasks in the console to see what they need to do

**Independent Test**: Can be fully tested by adding tasks and then viewing them, delivering the core value of task visibility.

### Tests for User Story 2 ⚠️

- [x] T018 [P] [US2] Unit test for TaskList.get_all_tasks() in tests/unit/test_tasklist.py
- [x] T019 [P] [US2] Integration test for view/list command flow in tests/integration/test_view_tasks.py

### Implementation for User Story 2

- [x] T020 [US2] Implement view/list command validation in src/cli/command_handler.py
- [x] T021 [US2] Implement view tasks business logic in src/services/todo_service.py
- [x] T022 [US2] Connect command handler to service for view operation
- [x] T023 [US2] Implement output formatting for task list display
- [x] T024 [US2] Handle empty list scenario with appropriate message

**Checkpoint**: At this point, User Stories 1 AND 2 should both work independently

---

## Phase 5: User Story 3 - Mark Task Complete (Priority: P2)

**Goal**: Enable users to mark tasks as complete through the console to track progress

**Independent Test**: Can be fully tested by marking a task as complete and verifying its status changes, delivering value in progress tracking.

### Tests for User Story 3 ⚠️

- [x] T025 [P] [US3] Unit test for TaskList.mark_complete() in tests/unit/test_tasklist.py
- [x] T026 [P] [US3] Integration test for mark complete command flow in tests/integration/test_mark_complete.py

### Implementation for User Story 3

- [x] T027 [US3] Implement complete command validation in src/cli/command_handler.py
- [x] T028 [US3] Implement mark complete business logic in src/services/todo_service.py
- [x] T029 [US3] Connect command handler to service for mark complete operation
- [x] T030 [US3] Implement success response formatting for mark complete operation
- [x] T031 [US3] Implement error handling for invalid task ID validation

**Checkpoint**: At this point, User Stories 1, 2 AND 3 should all work independently

---

## Phase 6: User Story 4 - Update Task Description (Priority: P3)

**Goal**: Enable users to update task descriptions through the console to modify tasks if plans change

**Independent Test**: Can be fully tested by updating a task and verifying the description changes, delivering value in task management flexibility.

### Tests for User Story 4 ⚠️

- [x] T032 [P] [US4] Unit test for TaskList.update_task() in tests/unit/test_tasklist.py
- [x] T033 [P] [US4] Integration test for update command flow in tests/integration/test_update_task.py

### Implementation for User Story 4

- [x] T034 [US4] Implement update command validation in src/cli/command_handler.py
- [x] T035 [US4] Implement update task business logic in src/services/todo_service.py
- [x] T036 [US4] Connect command handler to service for update operation
- [x] T037 [US4] Implement success response formatting for update operation
- [x] T038 [US4] Implement error handling for invalid task ID and empty description validation

**Checkpoint**: At this point, User Stories 1, 2, 3 AND 4 should all work independently

---

## Phase 7: User Story 5 - Delete Tasks (Priority: P3)

**Goal**: Enable users to delete tasks through the console to remove tasks they no longer need

**Independent Test**: Can be fully tested by deleting a task and verifying it's removed from the list, delivering value in list management.

### Tests for User Story 5 ⚠️

- [x] T039 [P] [US5] Unit test for TaskList.delete_task() in tests/unit/test_tasklist.py
- [x] T040 [P] [US5] Integration test for delete command flow in tests/integration/test_delete_task.py

### Implementation for User Story 5

- [x] T041 [US5] Implement delete command validation in src/cli/command_handler.py
- [x] T042 [US5] Implement delete task business logic in src/services/todo_service.py
- [x] T043 [US5] Connect command handler to service for delete operation
- [x] T044 [US5] Implement success response formatting for delete operation
- [x] T045 [US5] Implement error handling for invalid task ID validation

**Checkpoint**: All user stories should now be independently functional

---

## Phase 8: Polish & Cross-Cutting Concerns

**Purpose**: Improvements that affect multiple user stories

- [x] T046 [P] Add help command implementation in src/cli/command_handler.py
- [x] T047 [P] Add exit/quit command implementation in src/cli/command_handler.py
- [x] T048 [P] Implement consistent error message formatting across all operations
- [x] T049 [P] Add input sanitization to prevent injection attacks
- [x] T050 [P] Add performance validation to ensure <1 second response time
- [x] T051 [P] Documentation updates in README.md
- [x] T052 [P] Additional unit tests in tests/unit/ for edge cases
- [x] T053 Run quickstart.md validation

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies - can start immediately
- **Foundational (Phase 2)**: Depends on Setup completion - BLOCKS all user stories
- **User Stories (Phase 3+)**: All depend on Foundational phase completion
  - User stories can then proceed in parallel (if staffed)
  - Or sequentially in priority order (P1 → P2 → P3)
- **Polish (Final Phase)**: Depends on all desired user stories being complete

### User Story Dependencies

- **User Story 1 (P1)**: Can start after Foundational (Phase 2) - No dependencies on other stories
- **User Story 2 (P1)**: Can start after Foundational (Phase 2) - May integrate with US1 but should be independently testable
- **User Story 3 (P2)**: Can start after Foundational (Phase 2) - May integrate with US1/US2 but should be independently testable
- **User Story 4 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3 but should be independently testable
- **User Story 5 (P3)**: Can start after Foundational (Phase 2) - May integrate with US1/US2/US3/US4 but should be independently testable

### Within Each User Story

- Tests (if included) MUST be written and FAIL before implementation
- Models before services
- Services before endpoints
- Core implementation before integration
- Story complete before moving to next priority

### Parallel Opportunities

- All Setup tasks marked [P] can run in parallel
- All Foundational tasks marked [P] can run in parallel (within Phase 2)
- Once Foundational phase completes, all user stories can start in parallel (if team capacity allows)
- All tests for a user story marked [P] can run in parallel
- Models within a story marked [P] can run in parallel
- Different user stories can be worked on in parallel by different team members

---

## Parallel Example: User Story 1

```bash
# Launch all tests for User Story 1 together:
Task: "Unit test for Task creation in tests/unit/test_task.py"
Task: "Unit test for TaskList.add_task() in tests/unit/test_tasklist.py"
Task: "Integration test for add command flow in tests/integration/test_add_task.py"

# Launch implementation tasks for User Story 1:
Task: "Implement add_task command validation in src/cli/command_handler.py"
Task: "Implement add_task business logic in src/services/todo_service.py"
```

---

## Implementation Strategy

### MVP First (User Story 1 Only)

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (CRITICAL - blocks all stories)
3. Complete Phase 3: User Story 1
4. **STOP and VALIDATE**: Test User Story 1 independently
5. Deploy/demo if ready

### Incremental Delivery

1. Complete Setup + Foundational → Foundation ready
2. Add User Story 1 → Test independently → Deploy/Demo (MVP!)
3. Add User Story 2 → Test independently → Deploy/Demo
4. Add User Story 3 → Test independently → Deploy/Demo
5. Add User Story 4 → Test independently → Deploy/Demo
6. Add User Story 5 → Test independently → Deploy/Demo
7. Each story adds value without breaking previous stories

### Parallel Team Strategy

With multiple developers:

1. Team completes Setup + Foundational together
2. Once Foundational is done:
   - Developer A: User Story 1
   - Developer B: User Story 2
   - Developer C: User Story 3
   - Developer D: User Story 4
   - Developer E: User Story 5
3. Stories complete and integrate independently

---

## Notes

- [P] tasks = different files, no dependencies
- [Story] label maps task to specific user story for traceability
- Each user story should be independently completable and testable
- Verify tests fail before implementing
- Commit after each task or logical group
- Stop at any checkpoint to validate story independently
- Avoid: vague tasks, same file conflicts, cross-story dependencies that break independence