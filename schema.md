# DevStopwatch Project Schema

```
User (_UserID_, Username)

Language (_LanguageID_, LanguageName)

Project (_ProjectID_, ProjectName, CreatedBy)
Foreign Key CreatedBy references User

ProjectMember (_ProjectID_, _UserID_)
Foreign Key ProjectID references Project
Foreign Key UserID references User

TimeLog (_UserID_, _LogID_, ProjectID, LanguageID, TimeLogged)
Foreign Key UserID references User
Foreign Key ProjectID references Project
Foreign Key LanguageID references Language
```

**User** -- Accounts and usernames created with the application. This table may be expanded to include other user-specific information information.

**Language** -- Programming languages known to the application. This table may be expanded to include further information about each language later on.

**Project** -- Projects created by users. Since multiple users may work on the same project AND since a single project may involve time spent using multiple languages, the following tables express those many-to-many relationships.

**ProjectMember** -- Maps which users have permission to work on which projects.

**TimeLog** -- Time logged by a specific user working either on a given project or with a given language (or both, in which case the logged entry also describes one of the languages used by that project). Since each tuple in this table represents a single event, it still conforms to the fourth normal form.
