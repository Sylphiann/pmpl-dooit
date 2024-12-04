# Model-Driven Test Design (Input Domain Model and Control Flow Graph)

## ISP Documentation for `get_list_catatan_transaksi` Method

### Input Domain Model

| Characteristics  | b1 (Valid)                  | b2 (Boundary Condition)             | b3 (Invalid)                    |
|------------------|-----------------------------|-------------------------------------|---------------------------------|
| User             | Authenticated valid user    | User with no associated kategori    | Unauthenticated/invalid user    |
| Category Name    | Existing valid category name | Category name with no transactions | Invalid category name           |

#### Explanation for Choosing this Input Domain Model

- **User**: Tests must ensure the method correctly handles valid users, users without any matching categories, and invalid or unauthenticated users.
- **Category Name**: The primary input for this method is the `nama` field, which identifies the associated category. Boundary and invalid cases test the absence of data or misuse of the field.

### IDM Relabeling Table

| Characteristics  | b1 (Valid)                | b2 (Boundary Condition)           | b3 (Invalid)             |
|------------------|---------------------------|-----------------------------------|--------------------------|
| A (User)         | Valid user                | Valid user with no categories     | Invalid/unverified user  |
| B (Category Name)| Valid category name       | Name with no transactions         | Invalid category name    |

### Constraints

- **User** must be authenticated and associated with the given category.
- **Category Name** must exist in the database and belong to the user.
- The method should return an empty list if no transactions exist.

### Test Values and Example I/O

- **Criteria Used**: Boundary Value Analysis and Equivalence Partitioning

| Test Value | Example Input                                           | Expected Output                |
|------------|---------------------------------------------------------|--------------------------------|
| A1B1       | `user=valid_user, nama="Test Kategori"`                 | List of matching transactions  |
| A1B2       | `user=valid_user, nama="Kategori Tanpa Transaksi"`      | Empty list                     |
| A1B3       | `user=valid_user, nama="Invalid Kategori"`              | Error: Category not found      |
| A2B1       | `user=valid_user_with_no_categories, nama="Test Kategori"` | Error: Category not found  |
| A3B1       | `user=unauthenticated_user, nama="Test Kategori"`       | Error: Authentication required |

## Associate Test Paths with Existing Test Cases

- **Test Value: A1B1**
  - **Test Case**: `test_get_list_catatan_transaksi_valid_user_valid_category`
  - **Explanation**: Verifies correct retrieval of transactions for a valid user and category.

- **Test Value: A1B2**
  - **Test Case**: `test_get_list_catatan_transaksi_no_transactions`
  - **Explanation**: Confirms the method returns an empty list when no transactions exist for the category.

- **Test Value: A1B3**
  - **Test Case**: `test_get_list_catatan_transaksi_invalid_category`
  - **Explanation**: Ensures the method raises an error for invalid or non-existent categories.

- **Test Value: A2B1**
  - **Test Case**: `test_get_list_catatan_transaksi_user_no_categories`
  - **Explanation**: Validates the behavior when the user has no associated categories.

- **Test Value: A3B1**
  - **Test Case**: `test_get_list_catatan_transaksi_unauthenticated_user`
  - **Explanation**: Checks that an unauthenticated user cannot access the method.

## Control Flow Graph (CFG) for `get_list_catatan_transaksi`

### Test Requirements (Edge-Pair Coverage)

[List test requirements based on the control flow graph]

### Test Paths

[Describe the test paths through the control flow graph]

### Associate Test Paths with Existing Test Cases

[Map the CFG test paths to existing test cases]
