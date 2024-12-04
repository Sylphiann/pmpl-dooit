# Model-Driven Test Design (Input Domain Model and Control Flow Graph)

## ISP Documentation for `get_kategori_nominal` Method

### Input Domain Model

| Characteristics | b1 (Valid)                | b2 (Boundary Condition) | b3 (Invalid)                      |
|-----------------|---------------------------|-------------------------|-----------------------------------|
| Start Date      | Any valid past date       | Same as end date        | Future date or invalid format     |
| End Date        | Any valid date after start date | Same as start date    | Past date or invalid format       |
| User            | Authenticated valid user  | User with no categories or transactions | Invalid or unauthenticated user |

#### Explanation for Choosing this Input Domain Model

- **Start Date and End Date**: These characteristics define the range for filtering transactions. Boundary conditions are critical to ensure the logic handles edge cases (e.g., start date equals end date).
- **User**: It is essential to validate behavior for authenticated users, users with no data, and invalid users to ensure security and proper exception handling.

### IDM Relabeling Table

| Characteristics | b1 (Valid)        | b2 (Boundary Condition) | b3 (Invalid)              |
|-----------------|-------------------|-------------------------|---------------------------|
| A (Start Date)  | Valid past date   | Same as end date        | Future or invalid date    |
| B (End Date)    | Valid future/present date | Same as start date    | Past or invalid date      |
| C (User)        | Authenticated valid user | User with no data     | Invalid/unverified user   |

### Constraints

- **start_date** must precede or equal **end_date** (logical validation).
- **user** must be authenticated and own the category being queried.
- Transactions must belong to the queried **Kategori**.

### Test Values and Example I/O

- **Criteria Used**: Boundary Value Analysis and Equivalence Partitioning

| Test Value | Example Input                                                    | Expected Output                         |
|------------|------------------------------------------------------------------|-----------------------------------------|
| A1B1C1     | `{start_date: "2023-01-01", end_date: "2023-12-31", user: valid_user}` | Total nominal for transactions          |
| A1B2C1     | `{start_date: "2023-01-01", end_date: "2023-01-01", user: valid_user}`  | Total nominal for transactions          |
| A1B3C1     | `{start_date: "2023-01-01", end_date: "2022-12-31", user: valid_user}`  | Error: End date before start date       |
| A3B1C1     | `{start_date: "2025-01-01", end_date: "2023-12-31", user: valid_user}`  | Error: Invalid date range               |
| A1B1C2     | `{start_date: "2023-01-01", end_date: "2023-12-31", user: valid_user_with_no_transactions}` | Nominal: 0 |
| A1B1C3     | `{start_date: "2023-01-01", end_date: "2023-12-31", user: invalid_user}` | Error: User not authenticated           |

### Associate Test Paths with Existing Test Cases

- **Test Value: A1B1C1**
  - **Test Case**: `test_get_kategori_nominal_valid_user_valid_date_range`
  - **Explanation**: This verifies that the method correctly calculates the total nominal for a valid user within a valid date range.

- **Test Value: A1B3C1**
  - **Test Case**: `test_get_kategori_nominal_end_date_before_start_date`
  - **Explanation**: Ensures that invalid date ranges (end date before start date) result in proper error handling.

- **Test Value: A1B1C2**
  - **Test Case**: `test_get_kategori_nominal_no_transactions`
  - **Explanation**: Tests behavior for users with no transactions under the category within the specified range.

- **Test Value: A1B1C3**
  - **Test Case**: `test_get_kategori_nominal_invalid_user`
  - **Explanation**: Ensures that unauthenticated or invalid users are not allowed to query data.

## Control Flow Graph (CFG) for `get_kategori_nominal`

### Test Requirements (Edge-Pair Coverage)

[List test requirements based on the control flow graph]

### Test Paths

[Describe the test paths through the control flow graph]

### Associate Test Paths with Existing Test Cases

[Map the CFG test paths to existing test cases]
