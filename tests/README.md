BookmarkingApplication
======================
Outline for Bookmarking Application

> > Please create a small Django(1.6 or higher) application for bookmarking
> > that has the following features.
> >
> > There are 3 types of objects.
> >
> >
> > User object
> >
> > -----------
> >
> > (NOTE: link to contrib.auth for this)
> >
> > Internal ID: Char field of length 25, can be null and blank.
> >
> > verified: Boolean field, not null and cannot be blank. Default is False.
> >
> > approval_date: Datetime field, can be null and blank.
> >
> >
> > List object
> >
> > -----------
> >
> > Name: Char field of length 50, not null and cannot be blank.
> >
> > Date Created: DateTimeField, updated only once at object creation time.
> >
> > Date Modified: DatetimeField, updated every time the object is updated.
> >
> > Links: Many to Many field to Link object(s)
> >
> >
> > Link object
> >
> > -----------
> >
> > Name: Char field of length 50, not null and cannot be blank.
> >
> > Link: URLField, not null and cannot be blank.
> >
> > Date Created: DateTimeField, updated only once at object creation time.
> >
> > Date Modified: DatetimeField, updated every time the object is updated.
> >
> > Tags: Textfield, can be null and blank.
> >
> >
> > Please also create views for:
> >
> > 1. A login page
> >
> > 2. A list of all Lists in the system
> >
> > 2.1 Have a form that allows someone to create a new List object.
> >
> > 3. After clicking on a List from page 2, this page will have all the
> Links
> > on that List.
> >
> > 3.1 Have a form to add a new Link to the List.
> >
> > 3.2 Have a way to delete Links from a List.
> >
