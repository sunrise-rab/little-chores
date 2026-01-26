# Little-chores

Little Chores is a child-friendly task and reward web application designed to help parents encourage positive habits through age-appropriate chores.
The application supports parents in managing tasks for their children while motivating children through positive reinforcement using stickers and encouraging feedback.

![Little chores](docs/responsive.png)
## Contents
- [Little-chores](#little-chores)
  * [Project Goals](#project-goals)
  * [User Roles](#user-roles)
  * [Wireframes](#wireframes)
  * [Design Choices](#design-choices)
    + [Typography](#typography)
    + [Colour Palette](#colour-palette)
    + [Images](#images)
    + [Responsiveness](#responsiveness)
    + [Case Diagram](#case-diagram)
    + [Database schema](#database-schema)
  * [Features](#features)
    + [Existing Features](#existing-features)
    + [Future Features](#future-features)
  * [Tests](#tests)
    + [User Story](#user-story)
    + [HTML validation Results](#html-validation-results)
    + [W3C CSS Validator results](#w3c-css-validator-results)
    + [Wave](#wave)
  * [Technologies Used](#technologies-used)
  * [Deployment](#deployment)

<small><i><a href='http://ecotrust-canada.github.io/markdown-toc/'>Table of contents generated with markdown-toc</a></i></small>


## Project Goals

Little Chores was inspired by my earlier project Bond. While researching child-friendly printables, I came across several chore charts and reward trackers. That made me realise how useful a digital version could be for families. I decided to create an application that keeps the simplicity of a chore chart but adds features like assigning tasks by age group, marking chores as completed, and rewarding children with stickers and positive feedback.

- The application is designed to help parents understand the importance of involving children in everyday chores in an age-appropriate way, while learning about the benefits these activities have on children’s development.
- It also allows parents to safely suggest new tasks without immediate public visibility, helping to keep parents engaged in their children’s physical learning journey.
- All shared tasks are reviewed and approved by an admin to ensure they remain safe and appropriate.
- The application supports children through positive reinforcement of good habits.
- A simple and accessible interface is maintained to support daily family use.

## User Roles

As a Parent / Guardian, I want to: 

- Manages children and their tasks
- Chooses tasks from an approved task library
- Suggests new tasks for admin approval
- Marks tasks as completed and views rewards

As a Child, I want to:

- Views tasks in clear, child-friendly language
- Receives stickers and positive feedback for completed tasks

As an Admin, I want to:

- Manages users via Django admin
- Reviews and approves parent-submitted task suggestions
- Controls which tasks appear in the public task library

## Wireframes

Low-fidelity, hand-drawn wireframes were created during the planning phase to map out: Home page layout, parent dashboard, task management flow, sticker reward views and mobile adaptations.
Wireframes were intentionally kept low-fidelity to focus on structure and user flow rather than visual styling.
![Desktop Home](docs/desktop-home.png)
![Desktop Dashboard](docs/desktop-dashboard.png)
![Phone](docs/phone-wireframe.png)

## Design Choices
### Typography

To create a design that feels friendly and engaging for children while remaining clear and accessible for parents, two Google Fonts were selected:

- Baloo 2 (used for headings and section titles)
Baloo 2 has rounded, playful letterforms that feel warm and approachable without sacrificing readability. Its soft curves help create a welcoming tone that suits a child-focused reward system while still appearing polished and professional.

- Poppins (used for body text, buttons, and form elements)
Poppins is a clean, modern sans-serif font that ensures excellent readability across all screen sizes. Its simple structure balances the playful nature of Baloo 2, making it ideal for longer text, labels, and user interactions.

### Colour Palette
The Little Chores colour palette was designed to create a calm, supportive, and child-friendly environment while remaining clear and trustworthy for parents. Soft pastel tones are used for backgrounds to reduce visual strain, while brighter accent colours highlight rewards, actions, and positive feedback.
I used ![Color Scheme](docs/color-palette.png) to explore harmonious colour combinations and [Contrast Grid](https://contrastgrid.com/?xAxisData=%255B%257B%2522color%2522%253A%2522%2523F9FAF7%2522%257D%252C%257B%2522color%2522%253A%2522%2523FFFFFF%2522%257D%252C%257B%2522color%2522%253A%2522%2523AF31AF%2522%257D%252C%257B%2522color%2522%253A%2522%25232F3A44%2522%257D%252C%257B%2522color%2522%253A%2522%2523C5DFFC%2522%257D%252C%257B%2522color%2522%253A%2522%2523F7ECC9%2522%257D%252C%257B%2522color%2522%253A%2522%25238BC8A5%2522%257D%255D)to ensure sufficient contrast between text and background elements.



| CSS Variable Name     | HEX      | Usage & Purpose                                               |
| --------------------| ------- | ---------------------------------------------------------------- |
| --soft-cream        | #F3E2F3 | Main page background – calm, clean, and easy on the eyes         |              
| --calm-sky-blue     | #519EF6 | Dashboard elemets background                                     |
| --soft-growth-green | #16B690 | Dashboard elemets background                                     |
| --soft-yellow       | #F4C430| Dashboard elemets background                                     |
| --charcoal-text     | #2F3A44 | Main text colour softer than black for improved readability      |
| --brand-purple      | #B045B0 | Navbar, footer backgroundcolour and titles                                  |

### Images

Icons used throughout the application were sourced from Font Awesome.  

### Responsiveness

My website is responsive to different layouts depending on the size of the viewport have been included in the CSS media queries. This allows visitors to experience the website as I intended on device types and screen sizes. The breakpoints I am using are from Bootstrap.

![Breakpoints](docs/break-in-point.png)

### Case Diagram
![Use Case Diagram](docs/little_chores.png)

### Database schema

![Database Schema](docs/database-schema.png)

## Features

### Existing Features

| Feature                      | Description                                                                                                            | Screenshot                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- |
| **User Authentication**      | Users can register, log in, and log out securely. Only logged-in parents can manage children and chores.               | ![Screenshot](docs/features/login.png)           |
| **Add Child**                | Parents can add children by entering the child’s name and date of birth. Each child is linked to the logged-in parent. | ![Screenshot](docs/features/add_child.png)       |
| **Children Management**      | The dashboard displays a list of the parent’s children with options to edit or delete them.                            | ![Screenshot](docs/features/dashboard.png)   |
| **Children Management(delete child)**      | The dashboard displays a list of the parent’s children with options to edit or delete them.                            | ![Screenshot](docs/features/delete_child.png)   |
| **Children Management(edit child)**      | The dashboard displays a list of the parent’s children with options to edit or delete them.                            | ![Screenshot](docs/features/edit_child.png)   |
| **Assign Chores**            | Parents can select a child and assign only age-appropriate chores using checkboxes.                                    | ![Screenshot](docs/features/assign_chores.png)   |
| **Mark Chores as Complete**  | Parents can mark one or more chores as completed using checkboxes.                                                     | ![Screenshot](docs/features/todo_completed.png)   |
| **Delete Assigned Chores**   | Assigned chores can be deleted from the To Do list if added by mistake.                                                | ![Screenshot](docs/features/delete-assign-chores.png)    |
| **Daily Chore Tracking**     | Parents can track which chores are completed and which remain pending.                                                 | ![Screenshot](docs/features/todo_completed.png)  |
| **Responsive Dashboard**     | The dashboard provides clear cards for Children, Assign Chores, To Do & Completed, and Rewards.                        | ![Screenshot](docs/features/dashboard.png)       |

### Future Features
Allow children to log in to their own dashboard to view assigned chores and track progress independently
Allow parents to create rewards like (screen time, treats) that children can “buy” using earned stars.
Reset “To Do” chores each day while keeping reward history.
Full log of completed chores with dates and rewards.
Allow parents to create their own chores with descriptions and star values.

## Tests
### User Story
| User Story                                                                           | Acceptance Criteria (What “Done” Looks Like)                                                    | Tested? | Result            | Notes / Evidence                                                   |
| ------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------- | ------- | ----------------- | ------------------------------------------------------------------ |
| **As a Parent/Guardian, I want to manage children and their tasks**                  | Parent can add/edit/delete children and view assigned chores per child                          | Yes   |  Pass            | Add Child form works; Edit/Delete child available from dashboard   |
| **As a Parent/Guardian, I want to choose tasks from an approved task library**       | Parent can view chore library (age-group tasks) and assign chores to a selected child           |  Yes   | Pass            | Task library page displays chores; Assign chores form works        |
| **As a Parent/Guardian, I want to suggest new tasks for admin approval**             | Parent can submit a suggested task; admin can approve/reject; approved tasks appear in library  |  No    | Not Implemented | Feature not built in this version (planned for future iteration)   |
| **As a Parent/Guardian, I want to mark tasks as completed and view rewards**         | Parent can mark chores as completed; completed chores move to “Done”; rewards/stickers increase | Yes   | Pass            | Todo/Completed page updates status; stickers awarded on completion |
| **As a Child, I want to view tasks in clear, child-friendly language**               | Tasks show simple title + description + “what I will learn”                                     |  Yes   | Pass            | Task cards include child-friendly descriptions and benefits        |
| **As a Child, I want to receive stickers and positive feedback for completed tasks** | Completing a chore awards stickers and shows encouraging success messages                       |  Yes   | Pass            | Stickers are awarded; success message shown after marking done     |
| **As an Admin, I want to manage users via Django admin**                             | Admin can manage users, children, tasks, assigned tasks using Django admin panel                | Yes   | Pass            | Admin panel enabled for user and model management                  |
| **As an Admin, I want to review/approve parent-submitted task suggestions**          | Admin can view suggestions and approve/reject them                                              |  No    | Not Implemented | Depends on parent “suggest task” feature (not built yet)           |
| **As an Admin, I want to control which tasks appear in the public task library**     | Only tasks marked active/approved appear in library                                             | Yes   |  Pass            | Library filters tasks by `status=1` in TaskList view               |

### HTML validation Results

| Page                  | URL / Template                             | Validation Issues                                                                                          | Status      | Notes                                                                                                                     |
| --------------------- | ------------------------------------------ | ---------------------------------------------------------------------------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------- |
| **Home**              | ![Screenshot](docs/home-html-checker.png)  | • Duplicate `id="task-list"`<br>• Heading level skipped (`h1` → `h4`)<br>• Trailing slash on void elements |  Not fixed | Attempted refactor caused loss of styling on the home page after deployment. Issue documented for future improvement.     |
| **To-Do / Completed** | ![Screenshot](docs/todo-html-checker.png) | • `<div>` used inside `<label>` (invalid HTML structure)<br>• Trailing slash on void elements              | Not fixed | Issue caused by form layout structure. Left unchanged to preserve functionality and styling. Planned for future refactor. |
| **Dashboard**         | ![Screenshot](docs/dachboard-html-checker.png)         | • Initial duplicate IDs<br>• Heading hierarchy issues                                                      |  Fixed     | Duplicate IDs removed and heading structure corrected. Page now passes validation checks where applicable.                |

### W3C CSS Validator results

![Screenshot](docs/css-checker.png)

### JavaScript
I have used the recommended JShint Validator to validate all of my JS files.
![Screenshot](docs/js-test.png)

### Wave
Accessibility testing using the [WAVE](https://wave.webaim.org/) tool identified no critical errors; some contrast and heading structure alerts were noted and documented, but these do not affect usability or core functionality and will be addressed in future iterations
![Screenshot](docs/wave-test.png)

| **Bug**                                                         | **Cause**                                               | **Fix / Solution**                                                                                   |
| --------------------------------------------------------------- | ------------------------------------------------------- | ---------------------------------------------------------------------------------------------------- |
| `NameError: name 'date' is not defined`                         | `date` was used without being imported                  | Imported `date` from `datetime`                                                                      |
| `ImportError: cannot import name 'assign_tasks'`                | Function name mismatch between `views.py` and `urls.py` | Ensured the function name and import matched correctly                                               |
| `TemplateDoesNotExist` error                                    | Incorrect template path or filename                     | Corrected folder structure and template name                                                         |                                                         |
| Chores not filtered by child age                                | Chores queryset was not filtered dynamically            | Filtered chores using the selected child’s `age_group()`                                             |
| Chores not updating when selecting another child                | No refresh logic for form selection                     | Handled using javascript to  refresh queryset                                               |                                             |
| Duplicate chores appearing in To-Do list                        | Assigned tasks were created without uniqueness checks   | Prevented duplicate assignments per child and task                                                   |
| Completed chores not adding rewards                             | Stickers not incremented on completion                  | Updated logic to increment `stickers_awarded` when status changed to `done`                          |
| Rewards not showing total stars                                 | Rewards were not aggregated per child                   | Used `Sum("stickers_awarded")`.                                                     |
| Mark-as-complete not updating status                            | Status field not updated correctly                      | Set `status="done"` and added `completed_at` timestamp                                               |
| Assigned chores couldn’t be deleted                             | No delete functionality implemented                     | Added delete logic using selected task IDs                                                           |
| Styling looked different on Heroku                              | Static files cache and missing collectstatic            | When I change Debug to False the Styles does not load(still working on this)                                                    |

## Technologies Used

- [HTML](https://developer.mozilla.org/en-US/docs/Glossary/HTML5 "HTML")
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS "CSS")
- [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript "JS")
- [Google Fonts](https://fonts.google.com/ "Google Fonts")
- [GitHub](https://github.com/ "GitHub")
- [Color Contrast](https://contrastgrid.com/)
- [Python](https://www.python.org/)
- [Colour Palette](https://coolors.co/)
- [W3C HTML Validation Service](https://validator.w3.org/ "W3C HTML")
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/ "W3C CSS")
- [JSHint](https://jshint.com/ "JSHint")
- [TOC Generator](https://ecotrust-canada.github.io/markdown-toc/ "TOC Generator")
- [Am I Responsive](https://ui.dev/amiresponsive "Am I responsive")
- [Responsive Design Checker](https://responsivedesignchecker.com/ "Responsive Design Checker")
- [WAVE Accessibility Tool](https://wave.webaim.org/ "WAVE Accessibility Tool")
- [Color Contrast Accessibility Validator](https://color.a11y.com/ "Color Contrast Accessibility Validator")


## Deployment

The site was deployed to Heroku. The steps to deploy are as follows:

- After pushing all content to the repository, navigate to Heroku.
- In the [Heroku Dashboard](https://heroku.com/dashboard), navigate to the Project that you're working on.
- Click on the 'Deploy' button located near the top left of the page.
- Deployment method: Github > then select the repository to connect to.
- Enable automatic deploys.
- Deploy branch.

The live link can be found [here](https://little-chores-d53d2ee92787.herokuapp.com/).

## Credits

| Source | Purpose | Notes |
| --- | --- | --- |
| [Code Institute](https://codeinstitute.net) | Main Application | Walkthrough used as a guide to create application. |
| [Georgina90-x](https://github.com/Georgina90-x/Final-Project-3/tree/main) | README and TESTING| Used as a template for README and TESTING 
| [Github](https://www.github.com) | Repository | Used to store work in repository. |
| [Gitpod](https://www.gitpod.io) | Code Creation | Used to develop and write the application. |
| [Heroku](https://www.heroku.com) | Deployment | Used to deploy the application. |
| [PostgreSQL](https://www.postgresql.org/) | Database | Used database to store, add, edit and update data. |
| [ChatGPT](https://chatgpt.com/) | Bugs, Text content|was used as a learning and support tool to help explain errors, clarify Django concepts, and assist with debugging during development.| |
| [Diagrams](https://app.diagrams.net/) | README | Used to create a Use Case & Database Schema Diagram. |



