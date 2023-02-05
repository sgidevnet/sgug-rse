Name:           fedora-bookmarks
Version:        28
Release:        6%{?dist}
Summary:        Fedora bookmarks
License:        GFDL
URL:            http://fedoraproject.org/
# I had to strip the embedded icons out of the bookmarks file, because they are not 
# distributable under the GFDL. See https://bugzilla.redhat.com/show_bug.cgi?id=433471
Source0:        default-bookmarks.html
BuildArch:      noarch
Provides:       system-bookmarks


%description
This package contains the default bookmarks for Fedora.

%prep
# We are nihilists, Lebowski.  We believe in nassing.

%build
# We are nihilists, Lebowski.  We believe in nassing.

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks



%files
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html

%changelog
* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 28-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org>
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat Jul 03 2018 Matthew Miller <mattdm@fedoraproject.org> - 28-3
- defattr no longer needed

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Mon Sep 25 2017 Martin Stransky <stransky@redhat.com> - 28-1
- Put Fedora forum under https://

* Sat Aug 26 2017 Matthew Miller <mattdm@fedoraproject.org> - 27-1
- put magazine link directly on toolbar
- add social media communities to new folder
- siteicons saved in file for prettier menus

* Sat Aug 26 2017 Matthew Miller <mattdm@fedoraproject.org> - 27-0
- starting a series of edits and additions

* Sat Aug 26 2017 Matthew Miller <mattdm@fedoraproject.org> - 25-4
- Fix spelling error

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 25-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Sep  8 2016 Paul W. Frields <stickster@gmail.com> - 25-1
- Move Fedora Forum bookmark to http
- Use network location for release notes

* Thu May 19 2016 Paul W. Frields <stickster@gmail.com> - 24-1
- Updated Fedora Magazine and added Community Blog

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Oct  8 2015 Jan Horak <jhorak@redhat.com> - 22-3
- Use https:// whenever it is possible

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 22-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sun Apr 12 2015 Chris Roberts <chris.roberts@croberts.org> - 22-1
- Updated TOSW and Join Fedora page urls

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Wed Nov 27 2013 Martin Stransky <stransky@redhat.com> - 15-4
- Updated bookmarks (rhbz#1030577)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May  3 2013 Jan Horak <jhorak@redhat.com> - 15-2
- Updated bookmarks

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-0.5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct 29 2012 Jan Horak <jhorak@redhat.com> - 15-0.4
- Added new bookmarks and removed obsolete

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-0.3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 15-0.2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 16 2011 Nick Bebout <nb@fedoraproject.org> 15-0.1
- Change release notes to just link to Fedora Documentation

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 13-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Mar 22 2010 Christopher Aillon <caillon@redhat.com> 13-1
- Minor updates from marketing

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri May  1 2009 Christopher Aillon <caillon@redhat.com> - 11-1
- Refresh Fedora Project link set
- Add new Free Content link
- Remove obsolete links

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 10-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Sep  2 2008 Tom "spot" Callaway <tcallawa@redhat.com> 10-1
- fix bookmarks.html to not have embedded icons, they aren't usable under the GFDL.
  resolves bz 433471

* Wed Oct 17 2007 Matthias Clasen <mclasen@redhat.com> 8-1
- Update the link to the Fedora project homepage  (#291851)

* Tue Oct  2 2007 Matthias Clasen <mclasen@redhat.com> 7-2
- Remove reference to 'Core' from summary.  (#247362)

* Sun Apr 15 2007 Christopher Aillon <caillon@redhat.com> 7-1
- FC7 bookmarks based on http://fedoraproject.org/wiki/Releases/7/Bookmarks

* Tue Mar 20 2007 Christopher Aillon <caillon@redhat.com> 6-2
- Package review updates

* Wed Oct 18 2006 Christopher Aillon <caillon@redhat.com> 6-1
- Initial version

