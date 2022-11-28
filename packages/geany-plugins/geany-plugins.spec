%global geany_plug_docdir %{?_pkgdocdir}%{!?_pkgdocdir:%{_docdir}/%{name}-%{version}}
%global req_geany_ver 1.37

Name:           geany-plugins
Version:        1.37
Release:        1%{?dist}
Summary:        Plugins for Geany

License:        GPLv3+
URL:            http://plugins.geany.org/
Source0:        http://plugins.geany.org/geany-plugins/geany-plugins-%{version}.tar.bz2

BuildRequires:  geany-devel >= %{req_geany_ver} geany-libgeany >= %{req_geany_ver}
BuildRequires:  gettext intltool pkgconfig
BuildRequires:  enchant-devel >= 1.3 gtkspell3-devel >= 2.0
BuildRequires:  libxml2-devel >= 2.6.27
BuildRequires:  ctpl-devel >= 0.3
BuildRequires:  gpgme-devel
BuildRequires:  vte291-devel
#BuildRequires:  libtool cppcheck
BuildRequires:  vala
BuildRequires:  gtk3-devel, libwnck3-devel, GConf2-devel, glib2-devel

%description
Plugins for Geany. Plugins included are:
* Addons (Various small Addons)
* Autoclose (intellectually helps you to write code)
* Automark (highlights all words that match current word)
* Code navigation (Navigate through your source code easily)
* Commander (Control Geany using commands from a command panel)
#* Debugger (Enables debugging in Geany)
* Defineformat (Write multiline defines with aligned backslash)
* Devhelp (API documentation browser in Geany)
* GeanyGDB (Integration with GDB)
* GeanyGenDoc (Automatically generate documentation source code)
* GeanyLaTeX (Improved Support for LaTeX documents)
* GeanyMacro (User defined Macros for Geany)
* GeanyNumberedBookmarks (Provide users with 10 numbered Bookmarks)
* GeanyPG (Encrypt, decrypt and verify signatures with GnuPG)
* GeanyVC (Support for various Version Control Systems)
* Geanyctags (Generate and query ctags files for a Geany project)
* Geanydoc (Call specific documentation from within Geany)
* Geanyextrasel (Additional features for selecting code)
* Geanyinsertnum (Insert huge number ranges with small efforts)
* Geanylua (Support for Scripting with Lua)
* Geanyminiscript (Geany Mini-Script filter plugin)
* Geanyprj (Alternate project management for Geany)
#* Geanypy (Python Bindings for Geany)
* Geniuspaste (Use nopaste services directly from within Geany)
* Git-changebar (Highlights uncommitted changes, and allows navigation through hunks)
* KeyRecord (record a sequence of keystrokes and to replay it several times)
* Latex (Add LaTeX support to Geany)
* LineOperations (Assortment of simple line functions that can be applied to an open file)
* Lipsum (Generate random Text)
* Markdown (Real time preview for Markdown documents)
#* Multiterm (Multiple terminals inside of Geany)
* Overview (Overview over the code in a sidebar)
* PairTagHighlighter (Find and highlight matching opening/closing HTML tags)
* Pairtaghighlighter (Extension of Geany's project management)
* Pohelper (Improves Support for GetText translation files)
* Pretty-Print (XML Pretty Printer)
* ProjectOrganizer (Extension of Geany's Project Management)
* Scope (Graphical GDB front-end)
* SendMail (Sending of documents from within Geany)
* Shiftcolumn (Moving blocks of text horizontally)
* Spellcheck (Spell checking of documents or marked text)
* Tableconvert (Helps on converting a tabulator separated selection into a table)
* Treebrowser (Alternate file browser with tree view of folders)
* Updatechecker (Automatically check for Geany updates)
* Vimode: The plugin you always waited for
#* Webhelper (Provides some web development facilities for Geany)
* Workbench (Manage multiple projects in Geany)
* XMLSnippets (Extends XML/HTML tag autocompletion provided by Geany)


%package common
Summary:   Common files used by all geany plugins
Requires:  geany >= %{req_geany_ver} geany-libgeany >= %{req_geany_ver}
Obsoletes: geany-plugins-debugger <= 1.31
Obsoletes: geany-plugins-geanylua < 1.25
Obsoletes: geany-plugins-geanypy <= 1.31
Obsoletes: geany-plugins-markdown <= 1.29
Obsoletes: geany-plugins-multiterm <= 1.31
Obsoletes: geany-plugins-scope <= 1.31
Obsoletes: geany-plugins-webhelper <= 1.30


%description common
This package contains some common files which are used by every Geany plugin,
e.g. language translations.


%package addons
Summary:   Miscellaneous Addons for Geany
Requires:  geany-plugins-common = %{version}-%{release}

%description addons
This plugins consists of various small addons too small to justify their own
plugin, but are useful to have. The following functionality is implemented:
* Document list: This addon places a new item in the toolbar and when clicked
  offers a menu listing all open files plus the 'Close All' and 'Close Other
  Documents' menu items. This can be useful to quickly access open files and
  switch to them.
* Open and Copy URI: Adds 'Open URI' and 'Copy URI' menu items to the editor
  menu when the word under the cursor looks like a URI. 'Open URI' uses the
  browser command configured in Geany to open it.
* Tasks: The tasks plugin goes through a file being edited and picks out
  lines with configurable keywords (e.g. "TODO" or "FIXME") in them. It
  collects the text after those words and puts them in a new "Tasks" tab in
  the message window. Clicking on a task in that tab takes you to the line in
  the file where the task was defined.
* Systray: Adds a status icon to the notification area (systray) and provides
  a simple popup menu with some basic actions. It can also be used to
  quickly show and hide the Geany main window.
* Bookmark list: Add a list of defined bookmarks (line markers) to the sidebar.
  This list contains all bookmarks defined in the current file
  for faster overview and access.
* Mark Word: When double-clicking a word, all occurrences of this word are
  searched and then highlighted (similar to Geany's 'Mark All' Find option).
* Strip trailing blank lines: This addon removes excessive trailing blank
  lines from the document when it is saved. If you have 'Ensure new line at
  file end' option checked in Preferences, one trailing newline will be left.
* XML tagging: XML tagging allows to easy tag a selected text, by checking for a
  selection, offering a little dialog for inserting a tag and
  replacing a selection.


%package autoclose
Summary:   Intellectually helps you to write code
Requires:  geany-plugins-common = %{version}-%{release}

%description autoclose
This plugin enables auto-closing features. Auto-closing works while you typing
and intellectually helps you to write code.


%package automark
Summary:   Highlights all words that match current word
Requires:  geany-plugins-common = %{version}-%{release}

%description automark
This simple plugin highlights all words that match the current word.


%package codenav
Summary:    Navigate through your source code easily
Requires:   geany-plugins-common = %{version}-%{release}

%description codenav
This plugin adds some facilities for navigating in the code.
Actually, it will make it possible to:
- switch between header and implementation
- go to a file by typing its name


%package commander
Summary:    Control Geany using commands from a command panel.
Requires:   geany-plugins-common = %{version}-%{release}

%description commander
Commander is a plugin for Geany that provides a command panel for rapid
access to any action.


%package debugger
Summary:    Enables debugging in Geany
Group:      Development/Tools
Requires:   geany-plugins-common = %{version}-%{release}
Requires:   vte291 >= 0.24
Provides:   geany-plugins-debugger >= 1.36

%description debugger
Plugin enables debugging in Geany. Currently supports GDB only, but was
developed with multiple debuggers support in mind, so the other backends
support is planned as well.


%package defineformat
Summary:    Write multiline defines with aligned backslash
Requires:   geany-plugins-common = %{version}-%{release}

%description defineformat
On-the-fly #define prettyprinter. This plugin will help you to
write multiline defines with aligned backslash. After installed successfully,
load the plugin in Geany's plugin manager. Try it: open C/C++ file and type:

    #define A() do {


%package geanyctags
Summary:    Generate and query ctags files for a Geany project
Requires:   geany-plugins-common = %{version}-%{release}
Requires:   ctags

%description geanyctags
Even though Geany supports symbol definition searching by itself within the
open files (and with a plugin support within the whole project), tag
regeneration can become too slow for really big projects. This is why this
plugin was created. It makes it possible to generate the tag file only once and
just query it when searching for a particular symbol definition/declaration.
This approach is fine for big projects where most of the codebase remains
unchanged and the tag positions remain more or less static.


#%package devhelp
#Summary:   API documentation browser in Geany
#Group:     Development/Tools
#Requires:  geany-plugins-common = %{version}-%{release}
#
#%description devhelp
#This plugin embeds an API documentation browser and search functionality
#directly into Geany's user interface.  In case you didn't know, Devhelp is an
#API documentation browser mainly aimed at GNOME-related libraries, although
#there are Devhelp books for a wide range of library APIs.  Check your package
#manager and/or Google and you should have no trouble finding books that can
#be viewed with Devhelp.


%package geanydoc
Summary:   Call documentation from within Geany
Requires:  geany-plugins-common = %{version}-%{release}

%description geanydoc
Geanydoc allows you to execute specific commands on the word under the cursor.
This word is passed as an argument to the command. The output of the command
can either be placed into a special buffer called "DOC" or can be used to
execute an external program. Geanydoc is intended to be used for searching
through API documentation.


%package geanyextrasel
Summary:   Additional features for selecting code
Requires:  geany-plugins-common = %{version}-%{release}

%description geanyextrasel
Geanyextrasel provides some special features for selecting code, e.g. from
opening brace to closed brace and so on. This plugin will be very useful for
you if you're a programmer and working with much sourcecodes.


%package geanygendoc
Summary:   Automatically generate documentation source code
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  ctpl-libs >= 0.3
#Requires:  /usr/bin/rst2html

%description geanygendoc
GeanyGenDoc is a plugin for Geany that aims to automatically generate
documentation comment basis from the source code.

You may also want to install the following packages which enable
some extra features:
 - Docutils (http://docutils.sourceforge.net/) -- or another implementation of
   rst2html -- is needed to (re)generate the HTML manual.


%package geanyinsertnum
Summary:   Insert huge number ranges with small efforts
Requires:  geany-plugins-common = %{version}-%{release}

%description geanyinsertnum
Geanyinsertnum replaces a (possibly zero-width) rectangular selection with
integer numbers, using start/step/base etc. specified by the user. For
practical reasons, the number of lines is limited to 500000.


%package latex
Summary:   LaTeX support for Geany
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geany-plugins-geanylatex <= 1.32
Provides:  geany-plugins-geanylatex >= 1.33
%if 0%{?rhel}
Requires:  tex(latex)
%else
Recommends: tex(latex)
%endif


%description latex
This plugin improves LaTeX support in Geany. It provides several templates for
new documents, help with adding labels and inserting special characters,
and much more.


%package lipsum
Summary:   Lorem Ipsum generator for Inserting Placeholder Text
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geany-plugins-geanylipsum <= 1.28
Provides:  geany-plugins-geanylipsum >= 1.29


%description lipsum
Lipsum is a Lorem Ipsum generator for inserting placeholder text into a
document.


#%package geanylua
#Summary:   Lua Scripting for Geany
#Group:     Development/Tools
#Requires:  geany-plugins-common = %{version}-%{release}
#Requires:  lua < 5.2
#
#%description geanylua
#This plugin provides extensive support for developing in the lua programming
#language.


%package geanymacro
Summary:   User defined Macros for Geany
Requires:  geany-plugins-common = %{version}-%{release}

%description geanymacro
GeanyMacro is a plugin to provide user defined macros for Geany. It started
out as part of the ConText feature parity plugin, which was split into
individual plugins to better suit Geany's ethos of being as light as
possible while allowing users to select which features they want to add to
the core editor. The idea was taken from a Text Editor for Windows called
ConText.

This plugin alows you to record and use your own macros. Macros are
sequences of actions that can then be repeated with a single key
combination. So if you had dozens of lines where you wanted to delete the
last 2 characters, you could simple start recording, press End, Backspace,
Backspace, down line and then stop recording. Then simply trigger the macro
and it would automaticaly edit the line and move to the next. You could then
just repeatedly trigger the macro to do as many lines as you want.


%package geanyminiscript
Summary:   Geany Mini-Script filter plugin
Requires:  geany-plugins-common = %{version}-%{release}

%description geanyminiscript
The GeanyMiniScript plugin is a tool to apply a script filter on:

* the text selection
* the current document
* all documents of the current session.


The filter type can be:

* Unix shell script
* perl script
* python script
* sed commands
* awk script


The output can be:

* the selection of the current document
* all the current document
* or a new document


%package geanynumberedbookmarks
Summary:   Provide users 10 numbered Bookmarks
Requires:  geany-plugins-common = %{version}-%{release}

%description geanynumberedbookmarks
GeanyNumberedBookmarks is a plugin to provide users with 10 numbered
bookmarks (in addition to the usual bookmarks). It started out as part of
the ConText feature parity plugin, which was split into individual plugins
to better suit Geany's ethos of being as light as possible while allowing
users to select which features they want to add to the core editor. The idea
was taken from a Text Editor for Windows called ConText.

Normally if you had more than one bookmark, you would have to cycle through
them until you reached the one you wanted. With this plugin you can go
straight to the bookmark that you want with a single key combination.


%package geanypg
Summary:   encrypt, decrypt and verify signatures with GnuPG
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  gpgme

%description geanypg
GeanyPG is a plugin for Geany that allows the user to encrypt, decrypt and
verify signatures with GnuPG.


%package geanyprj
Summary:   Provides an alternate project management tool for Geany
Requires:  geany-plugins-common = %{version}-%{release}

%description geanyprj
Geanyprj provides an alternate project management approach to Geany's built-in
project facility. The idea is to be less a "session manager" as the built-in
project management does: It allows/requires you to manually open and close
project and allows you to store project files in different locations from
project sources.

Geanyprj takes a different approach:
It never saves session information, so that project files can be stored in
version control without constant noise from changes of opened files or cursor
position. You also will never have to open/close projects manually. If a
*.geanyprj file is found somewhere up in path it will be opened automatically.


#%package geanypy
#Summary:   Provides Python bindings for Geany
#Group:     Development/Tools
#Requires:  geany-plugins-common = %{version}-%{release}
#
#%description geanypy
#GeanyPy is based on the upstream at https://github.com/codebrainz/geanypy which
#is still under development, however it is useful as is. Parts of the existing
#API which mirror the Geany C API will probably not change unless the Geany API
#changes, however new API may be added. Also documentation is needed, contributions
#are welcome.
#
#Detailed information can be found in the documentation directory and at
#http://plugins.geany.org/geanypy.html


%package sendmail
Summary:   Send E-Mails from within Geany
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geany-plugins-geanysendmail < 1.28

%description sendmail
GeanySendMail is a little plugin to send a document as attachment using the
preferred mail client from inside Geany. It is similar to the envelope symbol
of most office tools and requires a mail client that supports remote calls.


%package geanyvc
Summary:   Version Control for Geany
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geanyvc <= 0.5
Provides:  geanyvc = %{version}-%{release}

%description geanyvc
Geanyvc is a plugin that provides a uniform way of accessing different version
control systems from within the Geany IDE. Currently, support for the following
version control systems is provided:

* Bazaar
* Git
* Mercurial
* Subversion
* SVK
* CVS


%package git-changebar
Summary:   Highlights uncommitted changes, and allows navigation through hunks
Requires:  geany-plugins-common = %{version}-%{release}
#BuildRequires:  libgit2-devel

%description git-changebar
This plugin highlights uncommitted changes to files tracked with Git, and allows to navigate through the hunks.


%package geniuspaste
Summary:   Use nopaste services directly from within Geany
Requires:  geany-plugins-common = %{version}-%{release}

%description geniuspaste
This plugin allows the user to paste the code from Geany into five different
pastebins. At the moment it supports this services:

* codepad.org
* tinypaste.com
* pastebin.geany.org
* dpaste.de
* sprunge.us

GeniusPaste detects automatically the syntax of the code and paste it with
syntax highlighting enabled. It can also display the pasted code opening a new
browser tab.


%package keyrecord
Summary:   Records and replays a sequence of keystrokes
Requires:  geany-plugins-common = %{version}-%{release}

%description keyrecord
This plugin allows you to record a sequence of keystrokes and to replay it
several times.


%package lineoperations
Summary:   Assortment of simple line functions that can be applied to an open file
Requires:  geany-plugins-common = %{version}-%{release}

%description lineoperations
Line Operations is an assortment of simple line functions that can be applied to an open file.


%package projectorganizer
Summary:   Extension of Geany's project management
Requires:  geany-plugins-common = %{version}-%{release}
Obsoletes: geany-plugins-gproject < 1.25
Provides:  geany-plugins-gproject >= 1.25

%description projectorganizer
ProjectOrganizer is an extension of Geany's project management displaying a tree of
files belonging to the project in the sidebar. In addition, it enables quick
swapping between header and source files, searching project files by name
and more. The plugin was created with big projects in mind so everything
works fast enough even with projects consisting of hundreds of thousands of
files.


%package markdown
Summary:       Real time preview for Markdown documents
Requires:      geany-plugins-common = %{version}-%{release}
#BuildRequires: webkit2gtk3-devel
Provides:      geany-plugins-markdown >= 1.34

%description markdown
The Markdown plugin provides a real-time preview of rendered Markdown, that is,
Markdown converted to HTML and inserted into an HTML template and loaded
into a WebKit view.


#%package multiterm
#Summary:   Multiple terminals inside of Geany
#Group:     Development/Tools
#Requires:  geany-plugins-common = %{version}-%{release}
#
#%description multiterm
#MultiTerm is similar to Geany's built-in VTE terminal except that it
#supports multiple terminals in tabs and supports different shells in each of
#the terminal tabs.


%package overview
Summary:   Overview over the code in a sidebar
Requires:  geany-plugins-common = %{version}-%{release}

%description overview
This plugin provides overview over the code from bird perspective in a sidebar.


%package pairtaghighlighter
Summary:   Extension of Geany's project management
Requires:  geany-plugins-common = %{version}-%{release}

%description pairtaghighlighter
Find and highlight matching opening/closing HTML tags by clicking or moving the
cursor inside a tag.


%package pohelper
Summary:   Extension of Geany's project management
Requires:  geany-plugins-common = %{version}-%{release}

%description pohelper
A plugin for Geany that improves the support for GetText translation files, by
providing various features specific to this format and to translators.

Features:

* Navigation between all, untranslated or fuzzy messages;
* Reformatting of the translation (reflow);
* Toggling the fuzziness of a translation;
* Pasting of the untranslated string to the translation;
* Automatic updating of the translation metadata.


%package pretty-printer
Summary:   XML pretty printing plugin for Geany
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  libxml2 >= 2.6.27
Obsoletes: geany-plugins-pretty-print <= 1.23
Provides:  geany-plugins-pretty-print >= 1.23

%description pretty-printer
Plugin for Geany to easily beautify XML code.


%package scope
Summary:   Graphical GDB front-end
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  gdb >= 7.3
Provides:  geany-plugins-scope >= 1.32

%description scope
Scope is a graphical GDB front-end with the normal functions you would
expect (stepping, breakpoints...), and a few notable features:

* The communication between Scope and GDB is asynchronous
* You can enter any GDB command, at any time
  (of course, for the command to be executed, GDB must be[come] available)
* All GDB I/O (along with some other messages) is displayed in a terminal-like
  "Debug Console". Whenever you find the GUI lacking, simply switch to that
  console and work directly with GDB
* 7-bit/Locale/UTF-8 support for values.


%package shiftcolumn
Summary:   Move Blocks of Text horizontally
Requires:  geany-plugins-common = %{version}-%{release}

%description shiftcolumn
Shiftcolumn allows you to move blocks of text horizontally in Geany.


%package spellcheck
Summary:   Spellcheck Text in Geany using the Enchant Library
Requires:  geany-plugins-common = %{version}-%{release}
Requires:  enchant

%description spellcheck
Spellcheck checks the selected text (or the whole document) with the spellcheck
library Enchant


%package tableconvert
Summary:   Helps on converting a tabulator separated selection into a table
Requires:  geany-plugins-common = %{version}-%{release}

%description tableconvert
Tableconvert is a plugin which helps on converting a tabulator separated
selection into a table.


%package treebrowser
Summary:   Alternate file browser plugin providing a tree view of directories
Requires:  geany-plugins-common = %{version}-%{release}

%description treebrowser
The tree browser plugin for Geany provides an alternate way to browse through
your files. It displays files and directories in a tree view and has more
features than the file browser plugin delivered with Geany itself.


%package updatechecker
Summary:   Automatically check for Geany updates
Requires:  geany-plugins-common = %{version}-%{release}
BuildRequires: libsoup-devel

%description updatechecker
UpdateChecker is a plugin for Geany, which is able to check whether there is
a more recent version of Geany available.


%package vimode
Summary:   Vim-mode plugin for Geany
Requires:  geany-plugins-common = %{version}-%{release}
BuildRequires: libsoup-devel

%description vimode
Vimode is a Vim-mode plugin for Geany written by a guy who does not use Vim.
Expect problems unexpected by a Vim user and, please, report them.

Despite the limited Vim knowledge of the author, the plugin tries to be a
reasonably complete Vim mode implementation featuring:

* normal mode, insert/replace mode, visual mode, line visual mode
* repeated commands (e.g. 10dd - delete 10 lines)
* "motion" commands (e.g. d10l - delete 10 characters to the right)
* "text object" commands (e.g. di( - delete inner contents of parentheses)
* visual mode commands (e.g. ~ to swap case of the selected text)
* basic ex mode commands like :s, including range specifications
* most basic navigation, selection and text manipulation commands
* command repetition using "." and repeated insert


#%package webhelper
#Summary:   Preview and Debug Web documents from within Geany using WebKit
#Group:     Development/Tools
#Requires:  geany-plugins-common = %{version}-%{release}
#BuildRequires: webkit2gtk3-devel
#
#%description webhelper
#WebHelper is a plugin for Geany that provides some web development
#facilities, such as a web page preview and some debugging tools (web
#inspector).
#
#Prominent features:
#
#* A basic web view, allowing to display any web page (using WebKit)
#* Possible automatic reloading of the web view upon document saving
#* A web inspector/debugging tool for the web view's content (including a
#  JavaScript console, a viewer and editor of processed HTML and CSS, a network
#  usage analysis tool and many more, thanks to WebKit).


%package workbench
Summary:   Manage multiple projects in Geany
Requires:  geany-plugins-common = %{version}-%{release}

%description workbench
The Workbench plugin is an extension that makes it possible to manage multiple
projects in geany. You can add geany projects to a workbench. From there you
can add directories to the project to manage the files belonging to the
project.


%package xmlsnippets
Summary:   Extends XML/HTML tag autocompletion provided by Geany
Requires:  geany-plugins-common = %{version}-%{release}

%description xmlsnippets
This plugin extends XML/HTML tag autocompletion provided by Geany. It
automatically inserts a matching snippet after you type an opening tag.


%prep
%autosetup -p1


%build
%configure --docdir=%{geany_plug_docdir}
%make_build


%install
%make_install

# Remove static library *.la files
find $RPM_BUILD_ROOT -name '*.la' -delete

# Remove zero-length files
find $RPM_BUILD_ROOT -type f -empty -delete


%find_lang %{name}


%files common -f %{name}.lang
#%doc NEWS README
%dir %{_datadir}/%{name}/
%dir %{_datadir}/doc/geany-plugins/
%doc %{_datadir}/doc/geany-plugins/README
%doc %{_datadir}/doc/geany-plugins/NEWS
%doc %{_datadir}/doc/geany-plugins/AUTHORS
%doc %{_datadir}/doc/geany-plugins/COPYING
%{_libdir}/libgeanypluginutils.so*

%files addons
%doc %{geany_plug_docdir}/addons
%{_libdir}/geany/addons.so

%files autoclose
%doc %{geany_plug_docdir}/autoclose
%{_libdir}/geany/autoclose.so

%files automark
%doc %{geany_plug_docdir}/automark
%{_libdir}/geany/automark.so

%files codenav
%doc %{geany_plug_docdir}/codenav
%{_libdir}/geany/codenav.so

%files commander
%doc %{geany_plug_docdir}/commander
%{_libdir}/geany/commander.so

#%%files debugger
#%%defattr(-,root,root,-)
#%%doc %{geany_plug_docdir}/debugger
#%%{_datadir}/%{name}/debugger/
#%%{_libdir}/geany/debugger.so

%files defineformat
%doc %{geany_plug_docdir}/defineformat
%{_libdir}/geany/defineformat.so

#%files devhelp
#%defattr(-,root,root,-)
#%doc %{geany_plug_docdir}/devhelp
#%{_datadir}/%{name}/devhelp/
#%{_libdir}/geany/devhelp.so

%files geanyctags
%doc %{geany_plug_docdir}/geanyctags
%{_libdir}/geany/geanyctags.so

%files geanydoc
%doc %{geany_plug_docdir}/geanydoc/
%{_libdir}/geany/geanydoc.so

%files geanyextrasel
%doc %{geany_plug_docdir}/geanyextrasel/
%{_libdir}/geany/geanyextrasel.so

%files geanygendoc
%doc %{geany_plug_docdir}/geanygendoc/
%{_libdir}/geany/geanygendoc.so
%{_datadir}/%{name}/geanygendoc/

%files geanyinsertnum
%doc %{geany_plug_docdir}/geanyinsertnum/
%{_libdir}/geany/geanyinsertnum.so

%files latex
%doc %{geany_plug_docdir}/latex/
%{_libdir}/geany/latex.so

#%files geanylua
#%defattr(-,root,root,-)
#%doc %{geany_plug_docdir}/geanylua/
#%{_libdir}/geany/geanylua.so
#%{_datadir}/%{name}/geanylua/
#%{_libdir}/%{name}/geanylua/

%files geanymacro
%doc %{geany_plug_docdir}/geanymacro/
%{_libdir}/geany/geanymacro.so

%files geanyminiscript
%doc %{geany_plug_docdir}/geanyminiscript/
%{_libdir}/geany/geanyminiscript.so

%files geanynumberedbookmarks
%doc %{geany_plug_docdir}/geanynumberedbookmarks/
%{_libdir}/geany/geanynumberedbookmarks.so

%files geanypg
%doc %{geany_plug_docdir}/geanypg/
%{_libdir}/geany/geanypg.so

%files geanyprj
%doc %{geany_plug_docdir}/geanyprj/
%{_libdir}/geany/geanyprj.so

#%files geanypy
#%defattr(-,root,root,-)
#%doc %{geany_plug_docdir}/geanypy/
#%{_libdir}/geany/geanypy.so
#%{_libdir}/geany/geanypy/*
#%{_libdir}/geany/*.py*

%files geanyvc
%doc %{geany_plug_docdir}/geanyvc/
%{_libdir}/geany/geanyvc.so

%files geniuspaste
%doc %{geany_plug_docdir}/geniuspaste/
%{_libdir}/geany/geniuspaste.so
%{_datadir}/%{name}/geniuspaste/

#%%files git-changebar
#%%doc %{geany_plug_docdir}/git-changebar/
#%%{_libdir}/geany/git-changebar.so
#%%{_datadir}/%{name}/git-changebar/

%files keyrecord
%doc %{geany_plug_docdir}/keyrecord/
%{_libdir}/geany/keyrecord.so

%files lineoperations
%doc %{geany_plug_docdir}/lineoperations/
%{_libdir}/geany/lineoperations.so

%files lipsum
%doc %{geany_plug_docdir}/lipsum/
%{_libdir}/geany/lipsum.so

#%%files markdown
#%%defattr(-,root,root,-)
#%%doc %{geany_plug_docdir}/markdown/
#%%{_libdir}/geany/markdown.so

#%files multiterm
#%defattr(-,root,root,-)
#%doc %{geany_plug_docdir}/multiterm/
#%{_libdir}/geany/multiterm.so

%files overview
%doc %{geany_plug_docdir}/overview/
%{_libdir}/geany/overview.so
%{_datadir}/geany-plugins/overview/*.ui

%files pairtaghighlighter
%doc %{geany_plug_docdir}/pairtaghighlighter/
%{_libdir}/geany/pairtaghighlighter.so

%files pohelper
%doc %{geany_plug_docdir}/pohelper/
%{_libdir}/geany/pohelper.so
%{_datadir}/geany-plugins/pohelper/*.ui

%files pretty-printer
%{_libdir}/geany/pretty-printer.so

%files projectorganizer
%doc %{geany_plug_docdir}/projectorganizer/
%{_libdir}/geany/projectorganizer.so

#%%files scope
#%%defattr(-,root,root,-)
#%%doc %{geany_plug_docdir}/scope/
#%%{_datadir}/geany-plugins/scope/
#%%{_libdir}/geany/scope.so

%files sendmail
%doc %{geany_plug_docdir}/sendmail/
%{_libdir}/geany/sendmail.so

%files shiftcolumn
%doc %{geany_plug_docdir}/shiftcolumn/
%{_libdir}/geany/shiftcolumn.so

%files spellcheck
%doc %{geany_plug_docdir}/spellcheck/
%{_libdir}/geany/spellcheck.so

%files tableconvert
%doc %{geany_plug_docdir}/tableconvert/
%{_libdir}/geany/tableconvert.so

%files treebrowser
%doc %{geany_plug_docdir}/treebrowser/
%{_libdir}/geany/treebrowser.so

%files updatechecker
%doc %{geany_plug_docdir}/updatechecker/
%{_libdir}/geany/updatechecker.so

%files vimode
%doc %{geany_plug_docdir}/vimode/
%{_libdir}/geany/vimode.so

#%files webhelper
#%doc %{geany_plug_docdir}/webhelper/
#%{_libdir}/geany/webhelper.so

#%%files workbench
#%%doc %{geany_plug_docdir}/workbench/
#%%{_libdir}/geany/workbench.so

%files xmlsnippets
%doc %{geany_plug_docdir}/xmlsnippets/
%{_libdir}/geany/xmlsnippets.so


%changelog
* Tue May 04 2021  HAL <notes2@gmx.de> - 1.37-1
- builds on Irix 6.5 with sgug-rse gcc 9.2.

* Sun Oct 25 2020 Dominic Hopf <dmaphy@fedoraproject.org> 1.37-1
- New upstream release: Geany-Plugins 1.37

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Apr 15 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.36-4
- Rebuild for libgit2 1.0.0

* Tue Mar 03 2020 Igor Raits <ignatenkobrain@fedoraproject.org> - 1.36-3
- Rebuild for libgit2 0.99

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.36-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sun Nov 03 2019 Dominic Hopf <dmaphy@fedoraproject.org> 1.36-1
- New upstream release: Geany-Plugins 1.36
- Re-enable debugger plugin

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.35-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 06 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.35-2
- Rebuild for libgit2 0.28.x

* Sat May 04 2019 Dominic Hopf <dmaphy@fedoraproject.org> 1.35-1
- New upstream release: Geany-Plugins 1.35

* Tue Mar 12 2019 Dominic Hopf <dmaphy@fedoraproject.org> - 1.34-3
- Add provides to geany-plugins-markdown and geany-plugins-scope

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.34-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Mon Dec 31 2018 Dominic Hopf <dmaphy@fedoraproject.org> 1.34-1
- New upstream release: Geany-Plugins 1.34
- New plugin: vimode
- Re-enabled plugins which now support GTK3: Markdown, Scope

* Fri Aug 10 2018 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 1.33-3
- Rebuild for libgit2 0.27.x

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.33-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Mar 03 2018 Dominic Hopf <dmaphy@fedoraproject.org> 1.33-1
- New upstream release: Geany-Plugins 1.33
- Rename plugin GeanyLaTeX to latex 

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.32-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Fri Dec 01 2017 Dominic Hopf <dmaphy@fedoraproject.org> 1.32-1
- New upstream release: Geany-Plugins 1.32

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Mon Jul 31 2017 Florian Weimer <fweimer@redhat.com> - 1.31-4
- Rebuild with binutils fix for ppc64le (#1475636)

* Thu Jul 27 2017 Dominic Hopf <dmaphy@fedoraproject.org> 1.31-3
- Build Geany-Plugins with GTK3 (RHBZ#1368632)
- Re-enabled plugins: Devhelp
- Disabled plugins: Debugger, Geanypy, Markdown, Multiterm, Scope, Webhelper
- Thanks very much to Rok Mandeljc for his efforts on this!

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Jul 22 2017 Dominic Hopf <dmaphy@fedoraproject.org> 1.31-1
- New upstream release: Geany-Plugins 1.31
- New Plugin: keyrecord

* Sat Jul 08 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.30-3
- Rebuild for libgit2 0.26.x

* Sun Mar 19 2017 Dominic Hopf <dmaphy@fedoraproject.org> 1.30-2
- Fix upgrade path for disabled Geany-Plugins (RHBZ#1433188)

* Sun Mar 05 2017 Dominic Hopf <dmaphy@fedoraproject.org> 1.30-1
- New upstream release: Geany-Plugins 1.30

* Tue Feb 07 2017 Igor Gnatenko <ignatenko@redhat.com> - 1.29-7
- Rebuild for libgit2-0.25.x

* Sun Dec 18 2016 Dominic Hopf <dmaphy@fedoraproject.org> 1.29-6
- Recommend tex(latex) for geanylatex (RHBZ#1346073)

* Sat Dec 10 2016 Igor Gnatenko <i.gnatenko.brain@gmail.com> - 1.29-4
- Rebuild for gpgme 1.18

* Sun Nov 13 2016 Dominic Hopf <dmaphy@fedoraproject.org> 1.29-3
- New upstream release: Geany-Plugins 1.29
- Renamed Plugin: geanysendmail -> lipsum
- Temporary disable plugin devhelp (RHBZ#1375807)
- Temporary disable plugin markdown (RHBZ#1375807)
- Temporary disable plugin webhelper (RHBZ#1375807)

* Sun Jul 10 2016 Dominic Hopf <dmaphy@fedoraproject.org> 1.28-1
- New upstream release: Geany-Plugins 1.28
- Renamed Plugin: geanysendmail -> sendmail

* Tue Mar 29 2016 Oliver Haessler <oliver@redhat.com> - 1.27-1
- New upstream release: Geany-Plugins 1.27
- new plugins: LineOperations, git-changebar
- Updated package description to include all available AddOns
- Updated geanypy directory

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.26-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 19 2015 Oliver Haessler <oliver@redhat.com> - 1.26-1
- New upstream release: Geany-Plugins 1.26

* Thu Aug 20 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.25-4
- remove obsolete references to lua

* Thu Aug 20 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.25-3
- fix Provides and Obsoletes for renamed/removed plugins

* Sat Aug 08 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.25-2
- build without --enable-gtk3

* Mon Jul 27 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.25-1
- New upstream release: Geany-Plugins 1.25
- new plugins: Automark, Geanyctags, Overview
- renamed plugins: gproject -> projectorganizer
- plugins gone: geanylua

* Sun Jun 28 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.24-6
- run gtk-update-icon-cache in %%post and %%postun for gproject only

* Thu Jun 25 2015 Dominic Hopf <dmaphy@fedoraproject.org> - 1.24-5
- run gtk-update-icon-cache in %%post and %%postun

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Tue Apr 15 2014 Dominic Hopf <dmaphy@fedoraproject.org> - 1.24-1
- New upstream release: Geany-Plugins 1.24
- remove geanygdb from specfile
- fix bogus date warnings
- new plugins: autoclose, defineformat, geanypy, pairtaghighlighter and pohelper

* Fri Jul 26 2013 Ville Skyttä <ville.skytta@iki.fi> - 1.23-3
- Install docs to %%{_pkgdocdir} where available.

* Wed May 15 2013 Tom Callaway <spot@fedoraproject.org> - 1.23-2
- rebuild for lua 5.2
- enable devhelp

* Sun Mar 10 2013 Dominic Hopf <dmaphy@fedoraproject.org> - 1.23-1
- New upstream release: Geany-Plugins 1.23
- New plugins: commander, markdown, multiterm, scope

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Aug 02 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.22-3
- add Obsoletes and Provides for pretty-print(er)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 16 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 1.22-1
- New upstream release: Geany-Plugins 1.22
- this release deprecates the geanygdb plugin
- pretty-print has been renamed to pretty-printer
- new plugins: geanyminiscript and geniuspaste

* Sun Jun 24 2012 Dominic Hopf <dmaphy@fedoraproject.org> - 0.21-4
- require and build against Geany 1.22

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Oct 25 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.21-2
- fix a dependency issue for geanygendoc

* Mon Oct 24 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.21-1
- New upstream release: Geany-Plugins 0.21
- 0.21 adds seven new plugins: debugger, geanymacro, geanynumberedbookmarks,
  geanypg, gproject, tableconvert, xmlsnippets

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jan 17 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.20-1
- New upstream release: Geany-Plugins 0.20
- remove unnecessary patches since the got applied upstream
- 0.20 brings two new plugins: updatechecker and webhelper
- order the plugins alphabetically (inspired by the output of ls)

* Sat Jan 08 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19-7
- apply patch from upstream SVN to fix geanylua build

* Thu Jan 06 2011 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19-6
- require and build against Geany 0.20

* Tue Oct 26 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19-5
- backport upstream changes for geanygendoc to work with CTPL 0.3

* Sat Oct 09 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19-4
- remove Requires: geany >= %%{req_geany_ver} from plugins, since Geany is
  required by geany-plugins-common, and any plugin requires the common
  package
- add missing dependency for ctpl-libs to geanygendoc plugin

* Sat Jul 31 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19-3
- enable or rather add geanygendoc to the specfile
- remove zero-length documentation files
- fix various spelling errors

* Thu Jul 15 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19-2
- correct license to GPLv3+
- fix build of pretty print plugin
- be more particular with BuildRequires

* Sat Jun 19 2010 Dominic Hopf <dmaphy@fedoraproject.org> - 0.19-1
- New upstream release: Geany-Plugins 0.19
- redordered plugins according to Geany's plugin manager dialog
- added new plugins: codenav, treebrowser, geanyextrasel, geanyinsertnum and
  pretty print

* Sun Jan 17 2010 Dominic Hopf <dmaphy@fedoraproject.org> 0.18-2
- Build against and require Geany 0.18.1

* Sat Oct 31 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.18-1
- update to new upstream release

* Sat Aug 15 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17.1-6
- build against and require geany 0.18

* Mon Aug 10 2009 Ville Skyttä <ville.skytta@iki.fi> - 0.17.1-5
- Use bzipped upstream tarball.

* Sat Jul 25 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17.1-4
- write BuildRequires at the beginning of this file

* Wed Jul 22 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17.1-3
- remove Requires: geany from the main package
- change Group to Development/Tools
- add release to the geanyvc Provides
- entirely remove %%files stanza for the main package

* Wed Jul 22 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17.1-2
- fix the required geany version also in the subpackages
- remove the requires to sub-packages to avoid building the metapackage since
  all geany plugins also can be installed by something like
  'yum install geany-plugins-*'
- fix the requires of geany-plugins-common to include the release

* Wed Jul 22 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17.1-1
- bump upstream version to 0.17.1
- fix required geany version to be 0.16 at the present

* Sat Jul 18 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17-5
- add Requires for metapackage
- rename subpackages back to geany-plugins-* instead of geany-plugin-*

* Fri Jul 17 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17-4
- readd the geany_plug_docdir global to fix the versioned directory issue for
  documentation files
- replace geany-plugins with %%{name} to be more consistent with macro usage
- remove zero-length documentation files
- fix the changelog
- remove static *.la-files
- split up packages

* Wed Jul 15 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17-3
- add %%{_datadir}/geany-plugins/geanylua/ to %%files-section

* Wed Jul 15 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17-2
- fix %%files-section again, thanks to Jonathan for the hint.

* Tue Jul 14 2009 Dominic Hopf <dmaphy@fedoraproject.org> 0.17-1
- update URL to plugins.geany.org

* Tue Jul 14 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.17-0.2
- Add Obsoletes for geanyvc
- Add more BuildRequires and Requires

* Tue Jul 14 2009 Jonathan G. Underwood <jonathan.underwood@gmail.com> - 0.17-0.1
- Update to 0.17 (first upstream release of tarball)
- Fix handling of docs
- Spec file cleanups

* Mon Jun 22 2009 Pingou <pingou@pingoured.fr> 0.1-1
- First RPM for Fedora
