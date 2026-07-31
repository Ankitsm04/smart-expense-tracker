# AI_NOTES.md

## AI Tools Used

* ChatGPT (OpenAI)

## Overview

I used ChatGPT as an AI development assistant during the implementation of this assignment. Rather than generating a complete solution and submitting it directly, I used AI iteratively to discuss design decisions, generate initial implementations, identify issues, and review the code after testing. Every feature was executed and verified locally before being included in the final submission.

---

## 1. AI-assisted work vs. my own work

### AI-assisted

ChatGPT was used to:

* Suggest an appropriate project structure (`src/`, `tests/`, `data/`).
* Recommend FastAPI and Pydantic models suitable for the assignment requirements.
* Generate initial implementations of:

  * Request and response models
  * JSON file storage functions
  * REST API endpoints
  * Automated pytest test cases
* Explain FastAPI and Pydantic features when required.
* Review and improve the README documentation.
* Help diagnose development issues such as dependency configuration and Python import errors.

### Completed by me

I personally:

* Created and configured the project using `uv`.
* Installed and managed project dependencies.
* Created the repository structure and project files.
* Integrated all generated code into the project.
* Executed the application locally throughout development.
* Tested every endpoint manually using the FastAPI Swagger UI.
* Verified that data was correctly persisted in the local JSON file.
* Ran the automated pytest suite repeatedly until all tests passed.
* Investigated and resolved environment and dependency issues encountered during development.
* Performed the final verification that every assignment requirement was satisfied before submission.

---

## 2. What I validated, modified, or corrected

AI-generated code was not accepted without review. I validated and refined it by:

* Running the application after each implementation step.
* Confirming that expense creation generated unique UUIDs.
* Verifying that expenses were correctly written to and loaded from `data/expenses.json`.
* Testing category filtering with different letter casing to ensure case-insensitive matching.
* Verifying total calculations for both all expenses and filtered categories.
* Testing deletion of existing expenses and correct handling of non-existent expense IDs.
* Verifying request validation for invalid amounts, missing fields, and invalid date formats.
* Running the complete pytest suite and fixing issues until all tests passed successfully.
* Resolving project import configuration and dependency issues encountered while setting up the test environment.

---

## 3. AI suggestions I chose not to use

Several suggestions were intentionally not included because they were outside the assignment scope.

### Database integration

AI suggested using SQLite with an ORM for persistence. I chose JSON file storage because the assignment explicitly stated that a database was not required.

### Additional API endpoints

Suggestions such as update (PUT/PATCH), authentication, user management, pagination, and analytics were not implemented because they were not part of the required functionality.

### More complex architecture

AI suggested introducing additional service and repository layers. Given the size of this project, I chose a simpler separation into models, routes, and storage modules to keep the code easier to understand and maintain.

### Alternative data types

Different approaches for representing monetary values (such as `Decimal`) were considered. I retained the current implementation because it satisfies the assignment requirements while keeping the implementation straightforward.

---

## 4. How AI influenced the development process

AI primarily acted as:

* a design reviewer,
* a code generation assistant,
* a debugging assistant,
* and a documentation assistant.

It accelerated development by generating initial implementations and explaining framework features, while I remained responsible for integrating, executing, testing, debugging, and validating the final solution.

---

## Reflection

Using AI reduced the time spent writing boilerplate code and helped explore implementation options more efficiently. However, the final project was produced through an iterative development process in which every generated component was reviewed, tested, and, where necessary, modified before being accepted. The completed submission reflects both AI assistance and my own implementation, testing, debugging, and validation work.
