Zope3 Viewlet Demo
==================

Here are a few samples of using zope.viewlet. It has only been tested
on Zope3.3.0b2.

Install as usual by creating $ZOPEINSTANCE/etc/package-includes/zope3demos-configure.zcml::

  <include package="zope3demos" />

 After a restart, you can access demo pages at:

   http://<yourz3server>:<port>/@@vdemo.html

   usually...
   http://localhost:8080/@@vdemo.html


"Bug Tracker":http://code.google.com/p/zope3demos/issues/list
Questions and concerns: y a h o o . c o m / ksmith93940-dev@

To Do
~~~~~~

 * add tests
 * more demos :)


Side note
~~~~~~~~~

Coping with scope creep, as new demos are added, has been a good learning experience 
for me. Kudos for Zope3 for making it easy to refactor.

My apologies for the major rewrites. You can find "stable" versions of the demos
in https://zope3demos.googlecode.com/svn/tags/
