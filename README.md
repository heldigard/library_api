# Library API

I've chosen the **Library Catalogue** topic.  Since I can't create a functional API and repository within this text-based response, I'll provide a detailed design specification that would meet the requirements.

**1. Entities and Operations:**

**Entities:**

* **Book:**  `{ id: integer, isbn: string, title: string, author: string, category: string, publicationYear: integer, availableCopies: integer }`
* **Author:** `{ id: integer, name: string }`
* **Category:** `{ id: integer, name: string }`

**Operations:**

* **Books:**

  * `GET /books`: Retrieve a list of books (paginated, filterable by author, category, title).
  * `GET /books/{id}`: Retrieve a single book by ID.
  * `POST /books`: Create a new book (requires authentication).
  * `PUT /books/{id}`: Update an existing book (requires authentication).
  * `DELETE /books/{id}`: Delete a book (requires authentication).
* **Authors:**

  * `GET /authors`: Retrieve a list of authors (paginated).
  * `GET /authors/{id}`: Retrieve a single author by ID.
  * `POST /authors`: Create a new author (requires authentication).
  * `PUT /authors/{id}`: Update an existing author (requires authentication).
  * `DELETE /authors/{id}`: Delete an author (requires authentication).  (Should consider cascading delete or constraints to prevent orphaned books).
* **Categories:**

  * `GET /categories`: Retrieve a list of categories (paginated).
  * `GET /categories/{id}`: Retrieve a single category by ID.
  * `POST /categories`: Create a new category (requires authentication).
  * `PUT /categories/{id}`: Update an existing category (requires authentication).
  * `DELETE /categories/{id}`: Delete a category (requires authentication). (Should consider cascading delete or constraints to prevent orphaned books).

**2. REST API Description:**

This API will follow RESTful principles, utilizing HTTP methods for CRUD operations and standard HTTP status codes.  It will adhere to the Richardson Maturity Model, aiming for Level 3 (HATEOAS) if time permits; Level 2 (HTTP verbs) is guaranteed.

**3.  Functional and Non-Functional Requirements:**

**Functional Requirements:**

* CRUD operations for Books, Authors, and Categories.
* Pagination for all list endpoints.
* Filtering for the `/books` endpoint (author, category, title).
* Error handling with appropriate HTTP status codes.

**Non-Functional Requirements:**

* High availability.
* Scalability.
* Security (HTTPS, input validation, authentication).
* Performance (fast response times).
* Maintainability.

**4.  Status Codes:**

* **200 OK:** Successful operation.
* **201 Created:** Successfully created a new resource.
* **204 No Content:** Successfully deleted a resource.
* **400 Bad Request:** Invalid request data.
* **401 Unauthorized:**  Authentication required.
* **403 Forbidden:** Insufficient permissions.
* **404 Not Found:** Resource not found.
* **409 Conflict:** Conflict during update or creation (e.g., ISBN already exists).
* **500 Internal Server Error:** Generic server error.

**5. Authentication:**

JSON Web Tokens (JWT) will be used for authentication.  The API will require a valid JWT in the `Authorization` header for all POST, PUT, and DELETE requests.

**6. Pagination:**

All list endpoints (`/books`, `/authors`, `/categories`) will support pagination using query parameters like `limit` and `offset` or `page` and `pageSize`.

**7. Caching:**

* `GET /categories` and `GET /authors` can be aggressively cached as they are expected to change infrequently.
* `GET /books` can be cached, but with shorter TTL (Time To Live) to reflect potential changes.
* `GET /books/{id}`, `GET /authors/{id}`, `GET /categories/{id}` should not be cached (or with very short TTL) as they return specific records that are more frequently updated.

**8. Error Handling:**

Errors will be returned in JSON format with a descriptive message and the appropriate HTTP status code.  Example:

```json
{
  "error": "ISBN already exists",
  "status": 409
}
```

**9.  Richardson Maturity Model:**

The API will at least meet Level 2 (using HTTP methods meaningfully) of the Richardson Maturity Model.  A Level 3 implementation (HATEOAS) would involve including links in the response bodies to related resources, allowing clients to discover available actions.


**10. Self-Evaluation:**

| Criteria/Points                            | 0 points | 2 points | 4 points | 7 points | My Score     |
| ------------------------------------------ | -------- | -------- | -------- | -------- | ------------ |
| Functional and non-functional requirements |          |          | ✓       |          | 4            |
| Model description                          |          |          | ✓       |          | 4            |
| Operations description                     |          |          | ✓       |          | 4            |
| Meaningful status codes                    |          |          | ✓       |          | 4            |
| Richardson model application               |          |          | ✓       |          | 4            |
| Authentication                             |          |          | ✓       |          | 4            |
| Pagination                                 |          |          | ✓       |          | 4            |
| Caching                                    |          |          | ✓       |          | 4            |
| **Total:**                           |          |          |          |          | **32** |

This score reflects a well-designed API specification. A fully functional implementation would require further development, but this design satisfies the majority of the requirements.  Reaching a higher score would involve implementing HATEOAS and thorough testing.
