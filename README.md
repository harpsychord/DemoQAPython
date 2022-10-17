#  Core Strengths Quality Assurance Evaluation

## 1. Automation task

The API for this project should be https://demoqa.com

For this task you are free to use whatever framework you are comfortable with to automate a couple general scenarios listed below:

Credentials:

User: `quality`
Password: `Password#123`

### Login
```
Given the user has not logged in
When the user loads https://demoqa.com/profile
Then the user is presented with a message instructing them to login or register
```

### Bookstore List
```
Given the user has logged in
When the user loads https://demoqa.com/books
Then the user is presented with a header with their UserName and a list of Books
```

### Bookstore Add To Your Collection
```
Given the user is presented with a list of books
When the user drills into a book from the list and clicks Add To Your Collection
Then the user receives an alert validating the action has been taken
```

### Profile
```
Given the user is logged in
When the user navigates to https://demoqa.com/profile
Then the user should see the seeded book (Git) and the recently added book(s)
```

### Logout
```
Given the user is logged in
When the user clicks Log out
Then the user should be redirected to https://demoqa.com/login
```

## 2. Manual Testing / Verification task

For this task, you are given a FRD (Functional Requirement Doc) from product to start building your testing plan to help understand the feature edges and expected acceptance criteria.

Product is looking to build a new feature on the account settings page.

This feature highlights some changes to what each user role can and cannot see.

**Please identify any holes you see and if you have any questions for product list them as well.**

### The roles are as follows:

- Admin
- Facilitator
- Member
- Sales

### The Features are as follows:

- Self-Paced Learning
- Outlook Integration
- Teams Integration

### The FRD outlines the following Use Cases:

Use Case 1: 
```
As an Admin I should have the ability to toggle all features on and off
```

Use Case 2: 
```
As an Admin I should see further configuration details for the MS Teams Integration when the feature is enabled
```

Use Case 3:
```
As an Facilitator I should only be able to toggle Self-Paced Learning and see the remaining feature toggles as read-only
```

Use Case 4:
``` 
As a Member I should not see any of the feature toggles presented
```

Use Case 5:
``` 
As a Admin + Member I should have the ability to toggle all features on and off
```

### Reporting of issues:

Explain how you would report a permission issue where Account Members can update feature toggles for a given account where the FRD explicitly stated that the members SHOULD NOT be able to change the account feature settings.

- How would you present this to the developer?
- How would you write up a ticket for this bug?
