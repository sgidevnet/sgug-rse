Summary: POP3, IMAP4 and SDPS mail retriever with Maildir delivery
Name: getmail
Version: 5.13
Release: 2%{?dist}
License: GPLv2
URL: http://pyropus.ca/software/getmail/

Source0: http://pyropus.ca/software/getmail/old-versions/getmail-%{version}.tar.gz
BuildArch: noarch
BuildRequires: python2-devel

%description
getmail is a secure, flexible, reliable and easy-to-use
mail retriever for POP3, IMAP4 and SDPS.
It delivers mail into a Maildir or mbox file.
It is designed to replace other mail retrievers such as fetchmail.
Getmail is written entirely in python.

%prep
%setup -q
sed -i 's/#!\/usr\/bin\/env.*$/#!\/usr\/bin\/python2/' getmail getmailcore/*.py

%build

%install
python2 setup.py install --root="%{buildroot}"
chmod a+x %{buildroot}/%{python2_sitelib}/getmailcore/*.py
chmod a-x %{buildroot}/%{python2_sitelib}/getmailcore/imap_utf7.py
rm docs/*.1
rm -rf %{buildroot}/%{_docdir}/%{name}-%{version}

%files
%doc docs/BUGS docs/CHANGELOG docs/COPYING docs/THANKS docs/TODO
%doc docs/configuration.html docs/documentation.html
%doc docs/faq.html docs/getmaildocs.css
%doc docs/getmailrc-examples docs/troubleshooting.html
%{_mandir}/man1/getmail.1*
%{_mandir}/man1/getmail_fetch.1*
%{_mandir}/man1/getmail_maildir.1*
%{_mandir}/man1/getmail_mbox.1*
%{_bindir}/getmail
%{_bindir}/getmail_fetch
%{_bindir}/getmail_maildir
%{_bindir}/getmail_mbox
%{_bindir}/getmail-gmail-xoauth-tokens
%{python2_sitelib}/getmail*.egg-info
%{python2_sitelib}/getmailcore/

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Mar 07 2019 Markus Mayer <lotharlutz@gmx.de> - 5.13-1
- upstream 5.13 release

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 5.6-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Oct 25 2018 Markus Mayer <lotharlutz@gmx.de> - 5.6-1
- upstream 5.6 release

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Feb 15 2018 Markus Mayer <lotharlutz@gmx.de> - 5.5-1
- upstream 5.5 release

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 5.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Oct 12 2017 Markus Mayer <lotharlutz@gmx.de> - 5.4-1
- upstream 5.4 release

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.54.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Wed Apr 26 2017 Markus Mayer <lotharlutz@gmx.de> - 4.54.0-1
- Upstream 4.54.0 release

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 4.51.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep 22 2016 Markus Mayer <lotharlutz@gmx.de> - 4.51.0-1
- Upstream 4.51.0 release


* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.49.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Fri May 13 2016 Markus Mayer <lotharlutz@gmx.de> - 4.49.0-1
- Upstream 4.49.0 release

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.48.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.48.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 06 2015 Markus Mayer <lotharlutz@gmx.de> - 4.48.0-1
- Upstream 4.48.0 release

* Mon Mar 02 2015 Markus Mayer <lotharlutz@gmx.de> - 4.47.0-1
- Upstream 4.47.0 release.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.46.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Apr 13 2014 Markus Mayer <lotharlutz@gmx.de> - 4.46.0-1
- Upstream 4.46.0 release.

* Sat Mar 15 2014 Markus Mayer <lotharlutz@gmx.de> - 4.43.0-2
- spec file cleanups

* Sat Sep 07 2013 Markus Mayer <lotharlutz@gmx.de> - 4.43.0-1
- Upstream 4.43.0 release.

* Sun Aug 11 2013 Markus Mayer <lotharlutz@gmx.de> - 4.42.0-1
- Upstream 4.42.0 release.
- Fix for https://fedoraproject.org/wiki/Changes/UnversionedDocdirs

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.40.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed May 22 2013 Markus Mayer <lotharlutz@gmx.de> - 4.40.3-1
- Upstream 4.40.3 release.

* Wed Apr 24 2013 Markus Mayer <lotharlutz@gmx.de> - 4.40.1-1
- Upstream 4.40.1 release.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.30.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.30.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Jun 24 2012 Ricky Zhou <ricky@fedoraproject.org> - 4.30.1-1
- Upstream 4.30.1 release.

* Tue Apr 17 2012 Ricky Zhou <ricky@fedoraproject.org> - 4.26.0-1
- Upstream 4.26.0 release.

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.24.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Dec 28 2011 Ricky Zhou <ricky@fedoraproject.org> - 4.24.0-1
- Upstream 4.24.0 release.

* Tue May 31 2011 Ricky Zhou <ricky@fedoraproject.org> - 4.20.3-1
- Upstream 4.20.3 release.

* Mon May 02 2011 Ricky Zhou <ricky@fedoraproject.org> - 4.20.2-1
- Upstream 4.20.2 release.

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.20.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jul 21 2010 David Malcolm <dmalcolm@redhat.com> - 4.20.0-2
- Rebuilt for https://fedoraproject.org/wiki/Features/Python_2.7/MassRebuild

* Sat Jul 03 2010 Dean Mander <knolderpoor@gmail.com> - 4.20.0-1
- update to release 4.20.0
* Thu Jan 21 2010 Dean Mander <knolderpoor@gmail.com> - 4.16.0-1
- update to release 4.16.0
* Sat Nov 28 2009 Dean Mander <knolderpoor@gmail.com> - 4.14.0-1
- update to release 4.14.0

* Sat Oct 24 2009 Dean Mander <knolderpoor@gmail.com> - 4.13.0-2
- update to release 4.13.0

* Mon Aug 10 2009 Dean Mander <knolderpoor@gmail.com> - 4.11.0-2
- update to release 4.11.0

* Sat Jul 18 2009 Dean Mander <knolderpoor@gmail.com> - 4.9.2-1
- Update to release 4.9.2

* Thu Apr 09 2009 Dean Mander <knolderpoor@gmail.com> - 4.9.0-1
- Update to release 4.9.0

* Mon Nov 10 2008 Dean Mander <knolderpoor@gmail.com> - 4.8.4-1
- Update to release 4.8.4

* Sun May 18 2008 Dean Mander <knolderpoor@gmail.com> - 4.8.1-2
- Updated python_sitelib header to build on rawhide

* Sat Apr 05 2008 Dean Mander <knolderpoor@gmail.com> - 4.8.1-1
- Updated to release 4.8.1
- remove setup.py patch (fixed upstream)

* Mon Mar 03 2008 Dean Mander <knolderpoor@gmail.com> - 4.8.0-1
- Updated to release 4.8.0
- Add python egg
- Patch setup.py (specfile missing)

* Wed Nov 21 2007 Dean Mander <knolderpoor@gmail.com> - 4.7.7-2
- escaping %% characters

* Tue Nov 20 2007 Dean Mander <knolderpoor@gmail.com> - 4.7.7-1
- no longer need to convert CHANGELOG
- added -q to %%setup
- more readable %%doc lines

* Mon Nov 05 2007 Dean Mander <knolderpoor@gmail.com> - 4.7.6-2
- Updated summary and description.
- Don't include manpages in documentation
- Correct license (GPLv2)
- convert CHANGELOG to UTF-8

* Mon Aug 13 2007 Dries Verachtert <dries@ulyssis.org> - 4.7.6-1
- Updated to release 4.7.6.

* Thu Jun 07 2007 Dries Verachtert <dries@ulyssis.org> - 4.7.5-1
- Updated to release 4.7.5.

* Wed May 09 2007 Dries Verachtert <dries@ulyssis.org> - 4.7.4-1
- Updated to release 4.7.4.

* Mon Mar 19 2007 Dries Verachtert <dries@ulyssis.org> - 4.7.3-1
- Updated to release 4.7.3.

* Sun Mar 04 2007 Dag Wieers <dag@wieers.com> - 4.7.2-1
- Initial package. (using DAR)
