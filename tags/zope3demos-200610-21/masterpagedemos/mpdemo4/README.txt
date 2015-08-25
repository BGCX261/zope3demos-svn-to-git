Master Template Test 4
======================

This is a live demo of the masterpage templating system as outlined by
Stephan Richter

http://blogs.lovelysystems.com/srichter/2006/09/20/the-skin-browser-and-lovely-systems-new-development-workflow/



Here is a final example at how we work the configuration::

	<!-- And example of a page. You really only need the class to have a
	     registration point. -->
	<browser:page
	    name="blog.html"
	    for="myproject.interfaces.IBlog"
	    class="myproject.browser.blog.BlogPage"
	    layer="myproject.browser.IProjectLayer"
	    permission="zope.Public"
	    />

	<!-- The main template used by all pages. It only contains the very basic
	     structure and a bunch of viewlet managaer calls. -->
	<browser:template
	    template="main.pt"
	    layer="myproject.browser.skin.IProjectSkin"
	    for="myproject.browser.IProjectPage"
	    />

	<!-- This is a typical main content viewlet that actually implements
	     functionality for the blog page. -->
	<browser:viewlet
	    name="z3d.mpdemo4.viewlet"
	    for="myproject.interfaces.IBlog"
	    manager="myproject.browser.interfaces.IContent"
	    view="myproject.browser.blog.BlogPage"
	    class="myproject.browser.blog.BlogList"
	    layer="myproject.browser.IProjectLayer"
	    permission="zope.Public"
	    />

	<!-- This is the template is registered for the blog list viewlet. -->
	<browser:template
	    template="z3d.mpdemo4.viewlet.pt"
	    layer="myproject.browser.skin.IProjectSkin"
	    for="myproject.browser.blog.BlogList"
	    />
