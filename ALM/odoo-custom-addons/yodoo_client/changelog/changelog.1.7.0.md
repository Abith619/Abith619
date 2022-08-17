- Ensure yodoo client is installed after database restored.
- Update modules if necesary after database restored.
- Remove old unused API endpoint `/saas/client/db/users/info`
- Added ability to manage remote admin sessions from managed database.
    - Administrator of database can see when external administrators visit
      his database
    - Administrator can see all active sessions of external adminitrators
    - Administrator can enforce exprie sessions of external administrators
    - Administrator can enable / disable ability to login for
      external administrators
