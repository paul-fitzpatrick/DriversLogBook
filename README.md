----------------------------------------------------------------------

# Drivers Logbook App

### Read me copied from original 29000 logbook project - images and titles may vary, but functionality remains the same.

This app was coded primarily in Python using the Django framework.
Currently the web-app is hosted on https://render.com/ with the database hosted by https://www.elephantsql.com/
The code has been in a private repository, only made public now in order for allows those involved in the tech review to view this readme file.
As this is a web based app, no permissions/access to the play store or app store is required. The app can be accessed by a user on any device, the reponsive styling/css of the app has been aimed to cater primarily for large PC screen sizes that occupy most IE offices, 10" ipads, ipad mini, and mobile phone downs to 320px, which should cover just about any samsung galaxy and iphone.  

## Background/Demand for App

Management in Drogheda DMU depot have had an ongoing issue with drivers complaining that after fault is reported in the logbook, they hear no more about it. 
The problem this presents for example is; a driver who is about to take a train into service which they reported an issue on previously, finds the same or similar problem, feel as though their issue was not addressed and possibly fails the train or at least delays it's departure while they waited for maintenance staff to attend and essentially provide feedback in person (which I have witnessed happen multiple times over the years as a fitter)
With live feedback provided through this app, the driver could have been informed that; the issue was looked at on a certain date and a work order has been opened, or that this fault had a work order opened, is now closed (which in the app, once a work order is set to closed, depot feedback will be rendered on the reported items info page) but the this part has now failed again for some reason or another etc and is essentially a new issue to report.
Also, apparently some drivers feel that unless the issue safety critical, filling out the paper logbook is a waste of time - because the lack of feedback leads them to think their issues are not addressed.
By providing live feedback, we hope to incentivise driver to report more/all issues and as a result help maintain a more reliable fleet.



You can view the live site here https://logbook-29000.onrender.com/

## How To Use The Web App
Currently drivers can register, then log in to use the app - to prevent anyone outside the business registering I can remove the register option with log in only once I get drivers details in order to register them myself.
+ Once logged in, the options to search a units history or fill out the report form are made visable.

![log in](https://github.com/paulfitzpatrick85/CI-Portfolio-Project-5/assets/121160104/0ea4a288-38a0-42b2-82a5-c071f982ac0f)

![logged in](https://github.com/paulfitzpatrick85/CI-Portfolio-Project-5/assets/121160104/0c422d99-47c5-4728-b437-63863f9f47f5)

### The Report Form

+ From the home page the driver can select 'report issue' and is then presented with the form prepopulated with grade, email and username (in this case, my staff number).
+ The driver then fills out the required information before submitting.

![rb](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/cf8547bd-1ce0-4b0e-911c-ac31bd481c24)

![f1](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/b10f1c5c-59c1-42e1-b757-e684db849cdc)

![f2](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/248b9033-77fc-47d2-aeb9-49b2bc16caa6)

+ Note the defect keyword dropdown in the form. This meant for later use with the fault/car search in the nav bar. 
When filling in the report form, drivers must select from a dropdown, a keyword that relates to their issue, the database can be then searched using these keywords (using the same dropdown list) to help identify problematic trends, e.g. searching main engine will yeild all results where 'main engine' was the defect keyword provided in the form. Any word can be searched for, but by mandating the use of keywords, this eliminates the risk of not finding the desires results due to spelling error or if a driver entered 'm/e' or 'main eng' for 'main engine' in there report - which is one of many common short hands used by drivers and craftworkers.

![k](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/4cdf7570-9e5d-4d87-a0f9-e1668ae33bb9)

+ Upon submission, a pop up (which is more aesthetically pleasing on tablets and phones then is pictured here) is display to the user to explain an email with all the information provided, has been sent to both the driver and DSM in drogheda.

![sp](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/e870ab1b-87b3-406c-a439-e5c1c9449950)

+ Note: the email is a pre-written template created in www.emailJS.com, when submit is clicked, javascript code grabs the information from chosen fields and injects their values into the template as seen below.

![js1](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/d6b7493c-0514-41bf-b07f-994a3f887e5b)


+ Once the form has submitted, it's information will render in the users 'My Profile' page, where the driver can track and review the status of their reports without having to search through the database.
+ Most importantly upon submission, the information is sent to the Django admin panel to be viewed by DSM. The form generates a unique five digit reference number, which is included in the email and the report item in the admin panel. This is provided in the event a driver wants to enquire about the reports status further for whatever reason, rather than quotig the car number or fault description in case there are a few similar reports, the DSM /admin can search the ref number in the admin site.

## Admin Panel

In the admin panel (only accessible by designated superusers), after selecting logbook_reports in the home page, admin can view the report items.

![dh](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/7cb07d48-69a4-45c0-bd07-48b17f43647b)


![rh](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/7f3e7e6b-9ed7-41e6-bb49-9d55da5783cd)

+ The four rows to the left; 'report read', 'work order created', 'work order closed' and 'driver emailed' have two functions.

1. When a report item is selected be reviewed, these points which are boolean values, are display as checks boxes, depending on which box or boxes are checked, the status of the report will update on the frontend for the driver to see.
- 'report read' checked will display in orange text, the status 'Read By Admin/DSM' (also the report will not appear on the logbook entries page until this box is check - though it will appear in the drivers 'my Profile' page)
- 'work order created' checked will display in green text, the status 'W/O created'
- 'work order created' checked will display in red text, the status 'W/O created'
2. They are a quick visual check for the admin user/DSM as what has been read and address etc, driver emailed automatically goes to TRUE (green tick) when the email is sent.

+ Report item view in panel (note; status change seen here was part of testing and will be removed)

![boxes](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/4175b3ee-8aba-4c6b-a426-093ffd088dc8)


+ Report item check boxes

![sapbe](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/aa1a5654-9048-4098-9776-97f159434ead)

### Work Order Information
Work orders are only created after details of a report are passed to a craftworker.
The craftworker investigates the issue reported, creates the work order then the issue is fixed, then the DSM enters the info relating to the job into SAP. Once a work order has been closed or "TECO'd", the longtext can be pasted into the 'depot feedback' text box.
Once the check box 'work order closed' has been ticked, the text within this field will now render on the front end in the report details page for that report item.

![sapbe](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/aa1a5654-9048-4098-9776-97f159434ead)

![sapfe](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/a50e29f0-c053-43cd-b163-626fd78c6398)

### Updating the Driver

When maintenance work has been completed, and the work order closed, the admin user can send and email to the driver inform him/her of the report being addressed and completed.

![sem1](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/a7052c83-87a6-4caf-877f-240844fd5810)

Since django is a python framework, I had an issue trying to include custom javascript (which triggers the email) in the django templates that make up its home pages. So as a result, once a report is selected, then 'send update email to driver' is selected in the dropdown, the information in the report is collected and the admin user is brought to the front end to click a send email button (since I can obviously put any code and language into my html templates)
Although I will keep working to simplify this further, in the mean time, two extra clicks of a mouse are all that is required by sending the email from the front end.

![semfe](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/e38500fb-ad3f-4fba-9cb2-d9b186495df6)

+ Template used for updating driver.

![updatetemp](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/2b22960c-6d8f-420d-ba74-33f7dba760bd)


### Download Functions
+ In the admin panel, a number of results can be selected and downloaded as a CSV file to be viewed in excel.

![csvd](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/dcfbc777-769d-453a-aadc-5c86c4e1e87d)

![csv](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/f880c4ac-80bc-4d82-9d51-85bfef55d73b)

+ Also, a single report can be selected to be downloaded as a PDF - this could possibly be used as a print out to be given to maintenance staff on their intial investigation of the issue.

![pdfd](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/6307b11c-8224-4181-b331-a5221644d989)

![pdf](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/aff9086f-978b-4baa-81d6-019bed4b4bd3)




## Search Functionality
+ From the home page drivers can search by unit to view all open driver reported issues.
The intial results page displays car, date, and status, which uses a traffic light system of sorts; 
- orange - confirms report has been read by the DSM
- green - a work order has been created to address the issue
- red - the work order has been closed on job completion.
When view is clicked, the user is brought to the report details page, where all the details filled out in the form are displayed.

![searchunit1](https://github.com/paulfitzpatrick85/CI-Portfolio-Project-5/assets/121160104/75ba90ee-a257-48c9-8b92-23445dbea913)

![search unit](https://github.com/paulfitzpatrick85/CI-Portfolio-Project-5/assets/121160104/ccb929e1-4f08-40b1-af3d-44a5894c0fa7)

+ In the nav bar, drivers can search by individual car e.g 29111, by keyword provided in the dropdown which corresponds to the keyword in the form, or by any other string of text they wish to use.

![nav](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/58377395-f797-4826-adff-ac2e8cb8eee7)

### Logbook Entries

This page holds all report entries (which have been confirmed as been read by the dsm/admin)
The basic layout is the same here as the 'unit history' search results and 'my reports' pages, car, date reported, status and the view button/link.

![lbe](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/8253ef31-7553-460e-8a0d-61b07fe26467)

And when an item is selected to be viewed:

![i](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/1ead49b9-9874-4b1d-afbc-03e45a7b2c5c)

### My Reports

This page store all reports submitted by the logged in driver, so the driver can quickly check for any status update on there reports, and also to remind them of what reports they have made.

![mr](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/ae9e2199-ed06-421d-9d71-f51c6614c52c)


### Feedback Form

The feedback form was placed here for my own benifit but could be changed to a 'contact us' form 

![fb](https://github.com/paul-fitzpatrick/29000-Log-Book/assets/121160104/31d07241-e40e-4c6d-94d3-eefae9d4ecd3)