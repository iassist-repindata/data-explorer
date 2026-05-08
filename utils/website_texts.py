from htmltools import TagList, tags


about_text = TagList(
    tags.div(tags.p(tags.a("Representation in Data",href="https://iassistdata.org/community/representation-in-data-ig/",target="_blank"), " aims to identify data sources for minority populations by global region and country. The Data Explorer allows users to explore these sources by keyword, language, resource type, and more."),
    tags.ul(tags.li(tags.strong("'About the data explorer': "),"This tab provides further information on how to use the Explorer."),
            tags.li(tags.strong("'Overview': "), "Use the filters on the left to get a first impression of the data in our database."),        
            tags.li(tags.strong("'Explore resources': "), "View individual entries in the database and download a filtered version of the data as .csv file."),        
                    ),
    tags.p("Report broken links to ",tags.a("repindata@iassistdata.org", href="mailto:repindata@iassistdata.org"))))

