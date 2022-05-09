In the configuration/config.ini please update github_token, assignees and repo with your own TOKEN and credentials.

What concerns would you have from a testing perspective?
The amount of endpoints we need to test.  For example get Emojis, what is the backing of this endpoint?  Is it worth testing this.
Billings and Organizations, do we have the user permission for QA to have?  How much permission for QA account can we have to validate
these permissions.  Meaning do we have different roles to test these access rights of endpoints.

How would you go about tackling the QA for this work?
Work with PM to understand what are the features customer is looking for in order to start.  What are the most interactive/traffic endpoints
that will be use the most in order to start with proper test cases along with negative.


What sort of tests would be worthing describing or worth automating?
What are the most interactive/traffic endpoints.  This is also going to help with performance testing to check the traffic.