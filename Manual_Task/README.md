## Manual Task Answers

```
Product is looking to build a new feature on the account settings page.

This feature highlights some changes to what each user role can and cannot see.

**Please identify any holes you see and if you have any questions for product list them as well.**

### The roles are as follows:

- Admin
- Facilitator
- Member
- Sales
```

* What is the relationship breakdown of this?  Could there be configurations for one group that another would have disabled?  It's possible that Team A has certain configurations enabled while Team B doesn't.  We'd need to test to ensure that enabling for A doesn't flip the features for B.  This isn't even taking into account the sales roles.
* Could we have more information on the roles?  What are they allowed to access?  What aren't they allowed to access?
* Combinations of roles can happen as Use Case 5 indicates.
* What else do these roles have access to?  There are security & PII implications here if permissions get messed up.

``` 
### The Features are as follows:

- Self-Paced Learning
- Outlook Integration
- Teams Integration
```

* Is there any potential for these new features to interfere with older features?  I am going to assume that there exists a set of regression tests for simplicity.

Use Case 1: 
```
As an Admin I should have the ability to toggle all features on and off
```

* Does this mean that only admin should have this ability?  We have 3 other roles.
     * Use Case 3 and 5 tell us that other users could have the ability if they have combined Member + Admin/Facilitator roles.
* We will need to test that the other roles do not have this ability.
* Should the other roles even be able to see the feature toggles?  Facilitator should have access to Self-Paced Learning.  But what about Sales and Members?
* What impacts does this make to other users/roles?  We should verify that when a particular feature is on or off that it's actually on or off.


Use Case 2: 
```
As an Admin I should see further configuration details for the MS Teams Integration when the feature is enabled
```

* Other features are Self-Paced Learning and Outlook Integration.  Admin should have the ability to see configuration details for these.
* What about other roles?  Should we be showing a "Not Authorized" error when these roles attempt to access this resource?
* What impact do these configurations have on the MS Teams side of things?  If a particular config is changed we should ensure that on MS Teams we should be able to verify it.
    * Ditto on SPL and Outlook.

Use Case 3:
```
As an Facilitator I should only be able to toggle Self-Paced Learning and see the remaining feature toggles as read-only
```

* Is it possible that there are other features that the Facilitator could have access to?
* Sales-only and Members-only users should be tested to ensure they not only cannot see this feature but are given a "Not Authorized" error when attempting to access this.
* Does this mean that the Facilitator should also be able to view and change the configuration details for Self-Paced Learning?
* We should ensure that any Facilitator (without Admin) user ONLY has the ability to change Self-Paced Learning.
* Should also test role combinations involving Facilitator to ensure proper functionality.
    * Facilitator + Member
    * Facilitator + Sales
    * Facilitator + Admin - Admin should overrule and see more than Self-Paced Learning.

Use Case 4:
``` 
As a Member I should not see any of the feature toggles presented
```

* Sales too.
    * Member + Sales combination should be tested as well.
* Should also ensure that Members cannot access the configurations for each feature by simply copy/pasting the URL to said configuration.
* Test all role combinations involving Member to ensure proper behavior:
    * Member + Sales - cannot see feature
    * Member + Facilitator - can only see Self-Paced Learning
    * Member + Admin - should be able to see all toggles.

Use Case 5:
``` 
As a Admin + Member I should have the ability to toggle all features on and off
``` 
* In what situation is an Admin also going to be an Member, or Facilitator, or Sales?
* Should also test the other combinations involving Admin.
    * Admin + Sales
    * Admin + Facilitator absolutely needs to be tested to ensure that Admin role overrides Facilitator role.  Otherwise this combination may result in only being able to see/change the Self-Paced Learning feature.

```
Reporting of issues:

Explain how you would report a permission issue where Account Members can update feature toggles for a given account where the FRD explicitly stated that the members SHOULD NOT be able to change the account feature settings.

    How would you present this to the developer?
    How would you write up a ticket for this bug?
```

* Are the features that the affected user(s) can change the new ones or old ones, or all of them?
* Does this mean they can change configurations too?
* Does this mean they can see the PII of other users?
* Is this only one Member or is this all Members?
* Check their roles and ensure they do not include Admin or Facilitator.

How would you present this to the developer?

* I would present the issue found to the developer via email or Slack/IM to ensure that we're on the same page.  I would also present my backing information.  Ensure that the user(s) in question are do not have roles that allow them access to the feature toggles.  I would also show the Use Case in question that the issue is violating.
* Afterwards I would write up the bug first in JIRA for said developer to attach their work to.

How would you write up a ticket for this bug?

* Title: User account with Member role can see and update feature toggles and should not be able to.
* Steps to Reproduce:
    * Login as specific User with Member role only.  (Member + Admin can change any of them, Member + Facilitator can change the Self-Paced Learning feature.  If multiple users are affected, we should indicate which accounts can do this.)
    * Access feature toggle page.
    * Note that the user can see the feature toggles.
    * Enable/disable any feature and save.
    * Note that the feature should now be enabled/disabled.
    * Login as an Admin and view the feature toggles.
    * Verify the feature was enabled/disabled.
* Expected behavior:
    * Per Use Case #4, Member roles should not be able to see or change feature toggles.

* I would also attach screenshots of the feature toggle being enabled/disabled by the specific user.
* Assuming I can see all roles for that user, I would attach a screenshot showing the user in question is only a Member (or a Member + Sales).
* I would also check the DB and develop a quick SQL query that could pull up the user and all of their assigned roles.  I would include this query along with a screenshot of the query's execution and results.