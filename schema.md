# DevStopwatch Project Schema

---

##### Assignment Description

This will be an individual assignment.

It should consist of a link to the schema produced for your project as a team effort, as stored in GitHub, along with a personal statement of what you contributed, and any personal comments or questions about it.

A schema must be a textual representation and commentary, including the following elements:

* the name of each table\*
* brief explanation of each table name
* what kind of entity each table represents
* how each table relates to other entities/tables
* evidence of normalization
* all column names given\*
* key columns identified\*
* any foreign keys identified\*
* brief explanation of column names present
* The starred\* portions of the above might look something like this:
  
  ```
  Employee (EmployeeID, EmployeeName, EmployeeAddress, EmployeePhone, PositionID, LocationID)
  Foreign Key PositionID references Position
  Foreign Key LocationID references Location
  Position (PositionID, PositionTitle, EducationRequired)
  Location (LocationID, City, State, LocationPhone) 
  ```
  
  So, the format for each table is
  
  ```
  TableName (Column1Name, ... ColumnkName)
  Foreign Key ColumnjName references TablemName
  ```
  
  repeated for each table (with foreign keys listed when there are some)

---

##### DevStopwatch Schema

```
User (_UserID_, Username)

Language (_LanguageID_, LanguageName)

Project (_ProjectID_, ProjectName, CreatedBy)
Foreign Key CreatedBy references User

ProjectMember (_ProjectID_, _UserID_)
Foreign Key ProjectID references Project
Foreign Key UserID references User

TimeLog (_UserID_, _LogID_, ProjectID, LanguageID, timeLogged)
Foreign Key UserID references User
Foreign Key ProjectID references Project
Foreign Key LanguageID references Language
```

**User** -- Accounts and usernames created with the application. This table may be expanded to include other user-specific information information.

**Language** -- Programming languages known to the application. This table may be expanded to include further information about each language later on.

**Project** -- Projects created by users. Since multiple users may work on the same project AND since a single project may involve time spent using multiple languages, the following tables express those many-to-many relationships.

**ProjectMember** -- Maps which users have permission to work on which projects.

**TimeLog** -- Time logged by a specific user working either on a given project or with a given language (or both, in which case the logged entry also describes one of the languages used by that project). Since each tuple in this table represents a single event, it still conforms to the fourth normal form.
