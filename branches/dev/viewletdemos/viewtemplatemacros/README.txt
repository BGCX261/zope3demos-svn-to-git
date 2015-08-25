Example of macros usage with ViewTemplate 
=========================================

This example is based on a masterpage templating system as outlined by Stephan Richter

http://blogs.lovelysystems.com/srichter/2006/09/20/the-skin-browser-and-lovely-systems-new-development-workflow/

Sample use case from the above post:
------------------------------------

Eventually the template designer
came back saying that he would like to define multiple viewlets in one page
template. But how to select snippets in a template? Aha! The revival of
macros. So eventually we have the following:

<!-- This is the template contains all possible blog views, and we just
     select the blog list. -->
<browser:template
    template="blog.pt"
    macro="bloglist"
    layer="myproject.browser.skin.IProjectSkin"
    for="myproject.browser.blog.BlogList"
    />
    
